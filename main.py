#!/usr/bin/env python3
"""Make the AI Judge Laugh entry: one office-life joke, written to entry.txt."""

import os

JOKE = "We hired a consultant to tell us what the intern already said, but in a font we respect."


def output_path():
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    data = JOKE.encode("utf-8")
    if not 1 <= len(data) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(data))
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
