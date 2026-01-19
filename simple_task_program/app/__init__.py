import re

def safe_filename(name: str) -> str:
    """
    Turns a title into a safe filename:
    - lowercases
    - replaces spaces with underscores
    - removes weird symbols
    """
    name = name.strip().lower()
    name = name.replace(" ", "_")
    name = re.sub(r"[^a-z0-9_\-]", "", name)
    return name or "untitled"
