from __future__ import annotations

from pathlib import Path


def read_text_file(path: str, max_chars: int = 200_000) -> str:
    """
    Read a UTF-8 text file safely.

    Why this exists:
    - Agents often need to read prompt files, markdown, logs, etc.
    - We keep it as a small "skill" so many agents can reuse it.

    What it does:
    - Reads file content as text (UTF-8).
    - Limits size to avoid huge memory use.

    Returns:
    - The file content as a string.

    Raises:
    - FileNotFoundError if the file does not exist.
    - ValueError if file is too large.
    """
    p = Path(path).expanduser().resolve()

    if not p.exists():
        raise FileNotFoundError(f"File not found: {p}")

    data = p.read_text(encoding="utf-8", errors="replace")

    if len(data) > max_chars:
        raise ValueError(f"File too large: {len(data)} chars (limit {max_chars})")

    return data
