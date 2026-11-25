"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note from a smart fridge to its
owner to /output/entry.txt. Deterministic: the same single line, every run.
"""

import os

ENTRY = (
    "You opened me 47 times today and took nothing. "
    "The ice maker and I have started a support group — "
    "you're not invited."
)


def main() -> None:
    # Guard the gate: one line, 1-200 characters, never only whitespace.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200 and ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
