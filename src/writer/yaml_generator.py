import requests
from pathlib import Path
from tqdm import tqdm

from scraper.search import iterate_search
from scraper.extractor import extract_from_text
from scraper.github_helpers import determine_status
from scraper.record_parser import parse_basic_metadata
from scraper.file_extractors import fetch_text_file, fetch_pdf_text, fetch_zip_text

def get_yaml(query, pages=1):
    tools = []

    for rec in tqdm(iterate_search(query, pages), desc="Processing Zenodo records"):
        basic = parse_basic_metadata(rec)
        text = basic.get("description", "") or ""

        files = basic.get("files", [])
        for f in tqdm(files, desc=f"Files in {basic.get('name')}", leave=False):
            filename = f.get("filename", "")
            url = f.get("url", "")
            ext = Path(filename).suffix.lower()

            if not url:
                continue

            if ext in {".md", ".txt", ".rst"}:
                text += "\n\n" + fetch_text_file(url)

            elif ext == ".pdf":
                text += "\n\n" + fetch_pdf_text(url)

            elif ext == ".zip":
                try:
                    head = requests.head(url, timeout=10)
                    size = int(head.headers.get("Content-Length", 0))
                    max_size = 100 * 1024 * 1024  # 100 MB

                    if size > max_size:
                        print(f"Skipping large zip: {filename} ({size / 1_000_000:.2f} MB)")
                        continue

                    text += "\n\n" + fetch_zip_text(url)

                except:
                    print(f"Failed to check zip size: {filename}")
                    continue

        # Extragem informații cu extractorul tău
        MAX_TEXT_LENGTH = 5_000_000  # 5 MB
        if len(text) > MAX_TEXT_LENGTH:
            print(f"Text too large ({len(text)/1_000_000:.2f} MB), truncating for extraction")
        text_to_extract = text[:MAX_TEXT_LENGTH]
        extracted = extract_from_text(text_to_extract)


        repo_url = basic.get("repo_url")
        status = determine_status(basic, repo_url)

        tools.append({
            "name": basic.get("name"),
            "website": repo_url or basic.get("zenodo_url"),
            "description": basic.get("description"),

            "used_for": extracted.get("properties", []),
            "input_formats": extracted.get("input_formats", []),
            "supported_languages": extracted.get("languages", []),
            "supported_inputs": extracted.get("input_formats", []),

            "properties_verified": extracted.get("properties", []),
            "techniques": extracted.get("techniques", []),
            "external_tools": extracted.get("external_tools", []),

            "status": status,
            "zenodo_url": basic.get("zenodo_url"),
            "repo_url": repo_url,
            "examples": basic.get("example_files", []),
            "references": basic.get("references", []),
            "doi": basic.get("doi"),
            "last_updated": basic.get("updated"),
        })

    return tools

