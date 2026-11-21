#!/usr/bin/env python3
"""Entry for make.fun bounty: The Poster for a Place That Isn't There.

Writes the travel poster image to /output/entry.png by copying the
poster artwork bundled with this repository (entry.png).
"""

import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"poster artwork not found: {source}")
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
