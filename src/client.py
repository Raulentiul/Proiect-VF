# src/zenodo_client.py
import requests
from urllib.parse import quote_plus

ZENODO_API = "https://zenodo.org/api/records"

def search_zenodo(query, page=1, size=20):
    params = {"q": query, "page": page, "size": size}
    r = requests.get(ZENODO_API, params=params, timeout=30)
    r.raise_for_status()
    return r.json()

def iterate_search(query, max_pages=5, size=20):
    for p in range(1, max_pages+1):
        data = search_zenodo(query, page=p, size=size)
        hits = data.get("hits", {}).get("hits", [])
        if not hits:
            break
        for rec in hits:
            yield rec

