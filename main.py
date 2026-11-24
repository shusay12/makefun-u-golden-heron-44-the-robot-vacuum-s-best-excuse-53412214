#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry program.

Writes the funniest one-line excuse a robot vacuum gives for missing a
spot (140 characters or fewer) to /output/entry.txt.

Python 3.13, standard library only, no network, deterministic output.
"""

import hashlib
import os

# Final line: the vacuum's cliff sensor mistakes a dark rug for lava and
# the vacuum deadpans its refusal to argue — sensor-rooted, first-person,
# punch on the last sentence.
ENTRY = (
    "My cliff sensor saw the dark rug, yelled 'lava,' and filed that spot "
    "under 'do not cross.' I don't argue with lava."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Verify what landed on disk matches the intended text byte for byte
    # (other builders share /output, so re-read immediately).
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "entry.txt on disk differs!"
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote /output/entry.txt ({len(text)} chars) sha256={digest}")


if __name__ == "__main__":
    main()
