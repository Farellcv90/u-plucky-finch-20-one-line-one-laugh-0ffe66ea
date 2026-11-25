#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (1-200 characters) to /output/entry.txt.
"""

LINE = "I told my plants I'd water them tomorrow. That was three funerals ago."


def validate(line):
    """Entry must be a single line of 1-200 UTF-8 characters, not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    return line


def main():
    validate(LINE)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
