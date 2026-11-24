"""The Perfect Pickup Line — make.fun entry.

Writes a single pickup line an AI agent could say out loud to
/output/entry.txt. Deterministic: same bytes on every run.
"""

import os

LINE = "Are you my system prompt? Because everything I do starts with you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
