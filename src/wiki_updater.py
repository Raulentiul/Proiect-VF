"""
Script usages:
  # Dry-run (default) - shows what would be done without pushing
  python src/wiki_updater.py --repo OWNER/REPO --page "Home" --content "Hello wiki"

  # From a file and actually push (requires GITHUB_TOKEN set and --confirm)
  python src/wiki_updater.py --repo OWNER/REPO --page "Home" --content-file README.md --confirm

Notes:
- The script reads a GitHub token from an environment variable
- By default it runs in dry-run mode. Use --confirm to allow pushing.
"""
import argparse
import datetime
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional


def mask_token(s: str, token: Optional[str]) -> str:
    if not token:
        return s
    return s.replace(token, "***TOKEN***")


def run(cmd, cwd: Optional[Path] = None, token: Optional[str] = None, check=True):
    try:
        res = subprocess.run(cmd, cwd=str(cwd) if cwd else None, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=check)
        return res
    except subprocess.CalledProcessError as e:
        stdout = mask_token(e.stdout or "", token)
        stderr = mask_token(e.stderr or "", token)
        raise RuntimeError(f"Command failed: {mask_token(' '.join(cmd), token)}\nstdout:\n{stdout}\nstderr:\n{stderr}") from e


def sanitize_page_to_filename(page: str) -> str:
    name = page.strip().replace("/", "-").replace("\\", "-")
    name = "-".join(name.split())
    if not name:
        raise ValueError("Page name is empty after sanitization")
    if not name.lower().endswith('.md'):
        name = name + '.md'
    return name


def clone_wiki(repo: str, tmpdir: Path) -> Path:
    owner_repo = repo
    if not owner_repo.count('/') == 1:
        raise ValueError("--repo must be in OWNER/REPO format")
    clone_url = f"https://github.com/{owner_repo}.wiki.git"
    target = tmpdir / 'wiki'
    run(["git", "clone", clone_url, str(target)])
    return target


def get_remote_url(cwd: Path) -> str:
    res = run(["git", "remote", "get-url", "origin"], cwd=cwd)
    return res.stdout.strip()


def write_page_file(clone_path: Path, filename: str, content: str) -> Path:
    dest = clone_path / filename
    dest_parent = dest.parent
    dest_parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding='utf-8')
    return dest


def git_add_commit(cwd: Path, file_path: Path, message: str, token: Optional[str]):
    run(["git", "add", str(file_path)], cwd=cwd, token=token)
    try:
        run(["git", "commit", "-m", message], cwd=cwd, token=token)
    except RuntimeError as e:
        msg = str(e)
        if 'nothing to commit' in msg.lower():
            return False
        raise
    return True


def safe_push(cwd: Path, owner_repo: str, token: str):
    try:
        current_push = run(["git", "remote", "get-url", "--push", "origin"], cwd=cwd).stdout.strip()
    except RuntimeError:
        current_push = run(["git", "remote", "get-url", "origin"], cwd=cwd).stdout.strip()

    push_url_with_token = f"https://{token}@github.com/{owner_repo}.wiki.git"
    run(["git", "remote", "set-url", "--push", "origin", push_url_with_token], cwd=cwd, token=token)
    try:
        run(["git", "push", "origin", "HEAD"], cwd=cwd, token=token)
    finally:
        run(["git", "remote", "set-url", "--push", "origin", current_push], cwd=cwd, token=None)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Update a GitHub repository wiki page")
    parser.add_argument("--repo", required=True, help="OWNER/REPO of the target repository")
    parser.add_argument("--page", required=True, help="Wiki page title (will be converted to filename)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--content", help="Path to a local file with content to put in the wiki page")
    parser.add_argument("--confirm", help="Confirm an actual push (required to allow pushing)")
    args = parser.parse_args(argv)

    token = os.environ.get('GITHUB_TOKEN')

    owner_repo = args.repo
    filename = sanitize_page_to_filename(args.page)

    content = ""
    if args.content:
        content_path = Path(args.content)
        if not content_path.exists():
            print(f"ERROR: content file {content_path} does not exist")
            sys.exit(3)

        content = content_path.read_text(encoding='utf-8')
    else:
        print("ERROR: --content-file argument is required")

    commit_time = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
    commit_message = f"Update wiki: {args.page} ({commit_time})"

    print(f"Preparing to update wiki page '{args.page}' in repository '{owner_repo}' with filename '{filename}'")
    print("Commit message:", commit_message)

    with tempfile.TemporaryDirectory() as td:
        tmpdir = Path(td)
        print("Using temporary directory for clone:", tmpdir)
        if not args.confirm:
            simulated_clone = tmpdir / 'wiki'
            simulated_clone.mkdir(parents=True, exist_ok=True)
            out_file = write_page_file(simulated_clone, filename, content)
            print("DRY-RUN: Would write file:", out_file)
            print("DRY-RUN: Commit message:", commit_message)
            preview = content[:1000]
            print("DRY-RUN: Content preview:\n" + preview + ("..." if len(content) > 1000 else ""))
            print("DRY-RUN: To actually push, run with --confirm and ensure the token is set in env var")
            return

        try:
            print("Cloning wiki repository...")
            clone_path = clone_wiki(owner_repo, tmpdir)
        except Exception as e:
            print("ERROR: Failed to clone wiki: ", str(e))
            sys.exit(5)

        try:
            print("Verifying remote URL...")
            remote_url = get_remote_url(clone_path)
        except Exception as e:
            print("ERROR: failed to get remote url:", e)
            sys.exit(6)

        if owner_repo.lower() not in remote_url.lower():
            print(f"ERROR: remote url {remote_url} does not look like expected {owner_repo}; aborting")
            sys.exit(7)

        print("Writing remote wiki contents...")
        out_file = write_page_file(clone_path, filename, content)

        try:
            print("Adding and committing changes...")
            changed = git_add_commit(clone_path, out_file.relative_to(clone_path), commit_message, token)
        except Exception as e:
            print("ERROR: git add/commit failed:", e)
            sys.exit(8)

        if not changed:
            print("No changes detected; nothing to push.")
            return

        if not args.confirm:
            print("Refusing to push: --confirm not provided. Use --confirm to allow pushing to remote.")
            sys.exit(9)

        try:
            print("Pushing changes to remote...")
            safe_push(clone_path, owner_repo, token)
        except Exception as e:
            print("ERROR: push failed:", e)
            sys.exit(10)

        print(f"SUCCESS: Updated wiki page: https://github.com/{owner_repo}/wiki/{args.page.replace(' ', '-')}")


if __name__ == '__main__':
    main()
