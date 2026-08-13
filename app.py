"""Minimal app used to verify local, mobile Remote, and GitHub workflows."""

from __future__ import annotations

import sys


DEFAULT_MESSAGE = "북5에서 생성 완료"


def format_message(message: str = DEFAULT_MESSAGE) -> str:
    """Return the stable output used by the integration test."""
    return f"ChatGPT Remote Test: {message}"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    message = " ".join(args).strip() or DEFAULT_MESSAGE
    print(format_message(message))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

