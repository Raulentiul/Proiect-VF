import requests
import zipfile
import io
import tempfile

def fetch_text_file(url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.text or ""
    except:
        pass
    return ""

def fetch_pdf_text(url):
    try:
        from pdfminer.high_level import extract_text as pdf_extract_text
        r = requests.get(url, timeout=30)
        if r.status_code == 200:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(r.content)
                tmp_path = tmp.name
            return pdf_extract_text(tmp_path) or ""
    except:
        pass
    return ""

def fetch_zip_text(url):
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            return ""
        z = zipfile.ZipFile(io.BytesIO(r.content))
        text = ""
        for name in z.namelist():
            lower_name = name.lower()
            if lower_name.endswith((".txt", ".md", ".rst")):
                try:
                    text += "\n\n" + z.read(name).decode("utf-8", errors="ignore")
                except:
                    pass
            elif lower_name.endswith(".pdf"):
                try:
                    import tempfile
                    from pdfminer.high_level import extract_text as pdf_extract_text
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                        tmp.write(z.read(name))
                        tmp_path = tmp.name
                    text += "\n\n" + (pdf_extract_text(tmp_path) or "")
                except:
                    pass
        return text
    except:
        return ""

