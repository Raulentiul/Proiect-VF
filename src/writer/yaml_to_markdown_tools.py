import yaml
import html
import re
from pathlib import Path

def html_to_text(html_content: str) -> str:
    if not html_content:
        return ""

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", html_content)

    # Decode HTML entities (&nbsp;, &mdash;, etc.)
    text = html.unescape(text)

    return text.strip()


def list_to_md(lst):
    if not lst:
        return "(none)\n"
    return "\n".join(f"- {item}" for item in lst) + "\n"


def get_field(value):
    if value in (None, "", []):
        return "N/A"
    return str(value)


def generate_markdown(tools):
    md = ["# Tools\n"]

    for tool in tools:
        md.append(f"## {get_field(tool.get('name'))}\n")

        md.append(f"- **Website:** {get_field(tool.get('website'))}")
        md.append(f"- **DOI:** {get_field(tool.get('doi'))}")
        md.append(f"- **Status:** {get_field(tool.get('status'))}")
        md.append(f"- **Last updated:** {get_field(tool.get('last_updated'))}\n")

        # Description
        desc = html_to_text(tool.get("description", ""))
        md.append("### Description")
        md.append(desc if desc else "(none)")
        md.append("")

        # Used for
        md.append("### Used for")
        md.append(list_to_md(tool.get("used_for")))

        # Input formats
        md.append("### Input formats")
        md.append(list_to_md(tool.get("input_formats")))

        # Supported languages
        md.append("### Supported languages")
        md.append(list_to_md(tool.get("supported_languages")))

        # Supported inputs
        md.append("### Supported inputs")
        md.append(list_to_md(tool.get("supported_inputs")))

        # Properties verified
        md.append("### Properties verified")
        md.append(list_to_md(tool.get("properties_verified")))

        # Techniques
        md.append("### Techniques")
        md.append(list_to_md(tool.get("techniques")))

        # External tools
        md.append("### External tools")
        md.append(list_to_md(tool.get("external_tools")))

        # Examples
        md.append("### Examples")
        md.append(list_to_md(tool.get("examples")))

        # References
        md.append("### References")
        md.append(list_to_md(tool.get("references")))

        md.append("\n---\n")

    return "\n".join(md)


def write_markdown_file():
    input_path = r"../../output/tools.yml"
    output_path = "TOOLS.md"

    yaml_text = Path(input_path).read_text(encoding="utf-8")
    data = yaml.safe_load(yaml_text)

    if "tools" not in data:
        print("No 'tools' key found in the YAML file.")
        return

    md = generate_markdown(data["tools"])

    Path(output_path).write_text(md, encoding="utf-8")
    print(f"Markdown generat: {output_path}")