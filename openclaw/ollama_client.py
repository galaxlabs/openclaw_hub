import requests

def ollama_generate(model: str, user_prompt: str, host: str = "http://localhost:11434") -> str:
    """
    Send a prompt to Ollama and return the text between markers.
    This reduces "extra talking" from small models.
    """
    url = f"{host}/api/generate"

    prompt = (
        "You must follow the output rules.\n"
        "Return ONLY the text between <FINAL> and </FINAL>.\n"
        "Do not add anything else.\n\n"
        f"{user_prompt}\n\n"
        "<FINAL>\n"
    )

    payload = {"model": model, "prompt": prompt, "stream": False}
    r = requests.post(url, json=payload, timeout=300)
    r.raise_for_status()
    text = (r.json().get("response") or "")

    # Try to extract content after <FINAL>
    if "<FINAL>" in text:
        text = text.split("<FINAL>", 1)[1]
    # If model forgot closing tag, we still take whatever we got
    if "</FINAL>" in text:
        text = text.split("</FINAL>", 1)[0]

    return text.strip()
