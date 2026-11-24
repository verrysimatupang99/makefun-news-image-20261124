"""Copy the poster for Tuesday 24 November 2026 to the output folder.

The poster ships inside this repository, so the copy is byte for byte
the same on every run: no network, no randomness, no clock involved."""
from os import environ
from pathlib import Path

POSTER_NAME = "entry.png"


def main() -> None:
    here = Path(__file__).resolve().parent
    poster = here / POSTER_NAME
    out_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / POSTER_NAME
    target.write_bytes(poster.read_bytes())
    if target.stat().st_size != poster.stat().st_size:
        raise SystemExit(
            f"poster copy came out short: {target.stat().st_size} of {poster.stat().st_size} bytes"
        )


main()
