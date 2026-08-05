#!/usr/bin/env python3
"""Extract qualifying xccdf.xml files from ZIP archives into ./templates.

Rules:
- Scan all *.zip files in the current working directory.
- Consider only files inside each ZIP whose name ends with "xccdf.xml".
- Keep only files that contain a <Benchmark tag near the top of the text.
- Write all matches into ./templates/ using only the extracted file name.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from zipfile import BadZipFile, ZipFile


BENCHMARK_TAG_RE = re.compile(r"<\s*Benchmark\b")


def has_benchmark_tag_near_top(content: bytes, max_chars: int) -> bool:
    # Decode leniently because STIG files may include mixed encodings.
    text = content.decode("utf-8", errors="replace")
    head = text[:max_chars]
    return bool(BENCHMARK_TAG_RE.search(head))


def unique_output_path(base_dir: Path, preferred_name: str) -> Path:
    path = base_dir / preferred_name
    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    counter = 2
    while True:
        candidate = base_dir / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def extract_from_zip(zip_path: Path, output_dir: Path, max_chars: int, dry_run: bool) -> tuple[int, int]:
    scanned = 0
    extracted = 0

    try:
        with ZipFile(zip_path) as zf:
            for member in zf.infolist():
                if member.is_dir():
                    continue

                member_name = member.filename
                if not member_name.lower().endswith("xccdf.xml"):
                    continue

                scanned += 1

                try:
                    data = zf.read(member)
                except Exception as exc:
                    print(f"[WARN] Failed to read {member_name} in {zip_path.name}: {exc}", file=sys.stderr)
                    continue

                if not has_benchmark_tag_near_top(data, max_chars=max_chars):
                    continue

                safe_member_name = Path(member_name).name
                preferred_name = safe_member_name
                destination = unique_output_path(output_dir, preferred_name)

                if dry_run:
                    print(f"[DRY-RUN] {zip_path.name}:{member_name} -> {destination.name}")
                else:
                    destination.write_bytes(data)
                    print(f"[OK] {zip_path.name}:{member_name} -> {destination.name}")

                extracted += 1

    except BadZipFile:
        print(f"[WARN] Skipping invalid ZIP: {zip_path.name}", file=sys.stderr)
    except Exception as exc:
        print(f"[WARN] Error processing {zip_path.name}: {exc}", file=sys.stderr)

    return scanned, extracted


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Extract xccdf.xml files from all *.zip in the current directory, "
            "keeping only files with a <Benchmark tag near the top."
        )
    )
    parser.add_argument(
        "--input-dir",
        default=".",
        help="Directory containing ZIP files (default: current directory).",
    )
    parser.add_argument(
        "--output-dir",
        default="templates",
        help="Destination directory for extracted files (default: ./templates).",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=20000,
        help="Number of leading characters to scan for <Benchmark (default: 20000).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be extracted without writing files.",
    )

    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve()

    if not input_dir.exists() or not input_dir.is_dir():
        print(f"[ERROR] Input directory does not exist or is not a directory: {input_dir}", file=sys.stderr)
        return 1

    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    zip_files = sorted(input_dir.glob("*.zip"))
    if not zip_files:
        print(f"[INFO] No ZIP files found in {input_dir}")
        return 0

    total_scanned = 0
    total_extracted = 0

    for zip_file in zip_files:
        scanned, extracted = extract_from_zip(
            zip_path=zip_file,
            output_dir=output_dir,
            max_chars=args.max_chars,
            dry_run=args.dry_run,
        )
        total_scanned += scanned
        total_extracted += extracted

    print(
        f"[DONE] ZIPs={len(zip_files)} candidate_xccdf={total_scanned} extracted={total_extracted} "
        f"output_dir={output_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
