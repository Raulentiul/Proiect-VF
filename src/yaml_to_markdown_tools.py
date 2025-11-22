#!/usr/bin/env python3
"""
Generează un fișier Markdown dintr-un YAML cu lista de tool-uri.
Formatul rezultat este stil documentație (varianta 1).
"""

import yaml
import html
import re
from pathlib import Path


def html_to_text(html_content: str) -> str:
    """Convertește HTML minimal în text simplu."""
    if not html_content:
        return ""

    # Eliminăm tagurile HTML
    text = re.sub(r"<[^>]+>", "", html_content)

    # Decode HTML entities (&nbsp;, &mdash;, etc.)
    text = html.unescape(text)

    return text.strip()


def list_to_md(lst):
    """Transformă o listă într-o listă Markdown."""
    if not lst:
        return "(none)\n"
    return "\n".join(f"- {item}" for item in lst) + "\n"


def field(value):
    """Returnează valoarea sau 'N/A'."""
    if value in (None, "", []):
        return "N/A"
    return str(value)


def generate_markdown(tools):
    md = ["# Tools\n"]

    for tool in tools:
        md.append(f"## {field(tool.get('name'))}\n")

        md.append(f"- **Website:** {field(tool.get('website'))}")
        md.append(f"- **DOI:** {field(tool.get('doi'))}")
        md.append(f"- **Status:** {field(tool.get('status'))}")
        md.append(f"- **Last updated:** {field(tool.get('last_updated'))}\n")

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


def main():
    input_path = r"C:\Users\reD0xcs\Documents\GitHub\Proiect-VF\src\output\tools.yml"
    output_path = "TOOLS.md"

    # FIX: specificăm UTF-8
    yaml_text = Path(input_path).read_text(encoding="utf-8")
    data = yaml.safe_load(yaml_text)

    md = generate_markdown(data["tools"])

    Path(output_path).write_text(md, encoding="utf-8")
    print(f"Markdown generat: {output_path}")


if __name__ == "__main__":
    main()
