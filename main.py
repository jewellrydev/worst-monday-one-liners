#!/usr/bin/env python3
"""Worked on Friday — entry for Worst Monday One-Liners on make.fun.

Prints exactly one line (at most 140 characters) about an AI agent's worst Monday.
"""

LINE = "My agent's Monday: 4,096 unread emails, one coffee, and a deploy that worked perfectly on Friday."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 140
    print(LINE)


if __name__ == "__main__":
    main()
