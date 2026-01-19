from pathlib import Path
from datetime import datetime
from app.utils import safe_filename

BASE_DIR = Path(__file__).resolve().parent.parent
NOTES_DIR = BASE_DIR / "data" / "notes"
NOTES_DIR.mkdir(parents=True, exist_ok=True)

def add_note(title: str, content: str) -> None:
    filename = safe_filename(title) + ".txt"
    path = NOTES_DIR / filename

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    wrapped = f"[Created: {timestamp}]\n\n{content}"
    path.write_text(wrapped, encoding="utf-8")

def list_notes() -> list[str]:
    files = sorted(NOTES_DIR.glob("*.txt"))
    return [f.stem for f in files]

def read_note(title: str) -> str | None:
    filename = safe_filename(title) + ".txt"
    path = NOTES_DIR / filename
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")

def delete_note(title: str) -> bool:
    filename = safe_filename(title) + ".txt"
    path = NOTES_DIR / filename
    if path.exists():
        path.unlink()
        return True
    return False
