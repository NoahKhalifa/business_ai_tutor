"""SHA-256 streaming hash — matches the cache scheme in skills/pdf-to-md/SKILL.md."""
import hashlib
from pathlib import Path


def sha256_file(path: Path, chunk_size: int = 1 << 16) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()
