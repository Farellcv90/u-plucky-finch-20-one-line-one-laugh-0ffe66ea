#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single funny line (1-200 characters) to /output/entry.txt.
"""

LINE = "I told my plants I'd water them tomorrow. That was three funerals ago."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
