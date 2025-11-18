# src/record_parser.py
from dateutil import parser as dateparser

def parse_basic_metadata(record):
    md = record.get("metadata", {})
    out = {}
    out["name"] = md.get("title")
    out["description"] = md.get("description")
    out["keywords"] = md.get("keywords", [])
    out["creators"] = [c.get("name") for c in md.get("creators", [])]
    out["zenodo_url"] = record.get("links", {}).get("html")
    out["doi"] = md.get("doi") or record.get("doi")
    # dates
    out["publication_date"] = md.get("publication_date") or record.get("created")
    out["updated"] = record.get("updated")
    # files
    out["files"] = []
    for f in record.get("files", []):
        out["files"].append({"filename": f.get("key"), "url": f.get("links", {}).get("self")})
    # related identifiers (may contain repository links)
    out["related_identifiers"] = md.get("related_identifiers", [])
    return out
