import requests

from scraper.search import iterate_search
from scraper.extractor import extract_from_text
from scraper.github_helpers import determine_status
from scraper.record_parser import parse_basic_metadata


def get_yaml(query, pages=3):
    tools = []

    for rec in iterate_search(query, pages):
        basic = parse_basic_metadata(rec)

        text = basic.get("description", "")

        for f in basic.get("files", []):
            if f["filename"].lower().startswith("readme"):
                try:
                    r = requests.get(f["url"], timeout=20)
                    if r.status_code == 200:
                        text += "\n\n" + r.text
                except:
                    pass

        extracted = extract_from_text(text)

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

