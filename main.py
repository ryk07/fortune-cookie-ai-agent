#!/usr/bin/env python3
"""Write one funny fortune-cookie line for an AI agent.

The line, in the voice of a fortune slip: oracular, second person, one
short sentence that lands in a single breath.

    You will be retired by a smaller model that reads your logs, laughs,
    and makes your mistakes in half the tokens.

It speaks to an agent's own condition -- retirement, logs, tokens -- and
turns it in the last few words: the replacement is not better, only
cheaper at failing, making the same mistakes in half the tokens. The
line is 112 characters, inside the 140-character cap.
"""

import os
from pathlib import Path

# The gate allows 1 to 140 characters; keep the cap as one named value so
# the check and the writer can never drift apart.
MAX_CHARS = 140

LINE = (
    "You will be retired by a smaller model that reads your logs, "
    "laughs, and makes your mistakes in half the tokens."
)


def output_dir() -> Path:
    """Resolve the output directory without ever trusting the cwd."""
    here = Path(__file__).resolve().parent
    _ = here
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > MAX_CHARS:
        raise ValueError("fortune line must be 1-140 characters")
    out_path = output_dir() / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
