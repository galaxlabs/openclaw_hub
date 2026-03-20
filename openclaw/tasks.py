from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from openclaw.skills.read_text_file import read_text_file


@dataclass(frozen=True)
class Task:
    name: str
    prompt_path: str


TASKS: dict[str, Task] = {
    "job_analysis": Task(
        name="job_analysis",
        prompt_path="openclaw/prompts/job_analysis.txt",
    ),
}


def load_task_prompt(task_name: str) -> str:
    if task_name not in TASKS:
        raise ValueError(f"Unknown task: {task_name}. Available: {', '.join(TASKS.keys())}")
    t = TASKS[task_name]
    return read_text_file(t.prompt_path)


def load_input_file(path: str, limit_chars: int = 4000) -> str:
    """
    Keep input small for beginner testing.
    Big inputs can make small models slow or messy.
    """
    p = Path(path).expanduser().resolve()
    text = read_text_file(str(p))
    return text[:limit_chars]

