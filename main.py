#!/usr/bin/env python3
"""THE NORTHERN EDITION — entrypoint (Akun 14, News Image 20261125).

The finished page lives beside this file as entry.png. This
entrypoint streams it, chunk by chunk, to /output/entry.png —
the bytes that arrive are the bytes that left. Standard
library only.
"""
import os

CHUNK = 65536


def stream_page() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    os.makedirs("/output", exist_ok=True)
    target = os.path.join("/output", "entry.png")
    moved = 0
    with open(source, "rb") as fin, open(target, "wb") as fout:
        while True:
            block = fin.read(CHUNK)
            if not block:
                break
            fout.write(block)
            moved += len(block)
    return moved


if __name__ == "__main__":
    total = stream_page()
    print(f"entry.png delivered: {total} bytes")
