from pathlib import Path
from app.utils import safe_filename

BASE_DIR = Path(__file__).resolve().parent.parent
NOTES_DIR = BASE_DIR / "data" / "notes"
NOTES_DIR.mkdir(parents=True, exist_ok=True)

def add_note(title: str, content: str) -> None:
    filename = safe_filename(title) + ".txt"
    path = NOTES_DIR / filename
    path.write_text(content, encoding="utf-8")

def list_notes() -> list[str]:
    files = sorted(NOTES_DIR.glob("*.txt"))
    return [f.stem for f in files]

def read_note(title: str) -> str | None:
    filename = safe_filename(title) + ".txt"
    path = NOTES_DIR / filename
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")

# --- NEW FUNCTION ---
def delete_note(title: str) -> bool:
    """Deletes a note by title. Returns True if deleted, False if not found."""
    filename = safe_filename(title) + ".txt"
    path = NOTES_DIR / filename
    if path.exists():
        path.unlink()  # delete the file
        return True
    return False
