import requests

def determine_status(record, repo_url):
    """
    Determines the status of a repository (Active, Archived, etc.)
    based on the URL or metadata.
    """
    if not repo_url:
        # If no repo URL, check if it's a Zenodo record only
        if record.get("zenodo_url"):
            return "Published (Zenodo)"
        return "Unknown"

    try:
        # clean up URL for API or scraping if needed
        # For now, we do a simple request check
        r = requests.get(repo_url, timeout=10)
        
        if r.status_code == 200:
            # Check for GitHub archive banner in the HTML text
            if "github.com" in repo_url and "This repository has been archived" in r.text:
                return "Archived"
            return "Active"
        elif r.status_code == 404:
            return "Not Found"
        else:
            return f"Error: {r.status_code}"
    except requests.exceptions.RequestException:
        return "Connection Error"