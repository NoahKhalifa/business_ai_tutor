"""Transcribe MP3 files using Whisper base model with word-level timestamps.

Writes per-file .txt + .json outputs into exercises/md/ (temp), which the
agent then formats into proper _transcript.md files with front-matter.

Usage:
    python tools/transcribe_units.py <file1.mp3> [file2.mp3 ...]
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import static_ffmpeg
static_ffmpeg.add_paths()

import whisper


def transcribe(audio_path: Path, model) -> dict:
    t0 = time.time()
    result = model.transcribe(
        str(audio_path),
        language="en",
        verbose=False,
        fp16=False,
    )
    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s ({len(result['segments'])} segments)", flush=True)
    return result


def main() -> int:
    paths = [Path(p) for p in sys.argv[1:]]
    if not paths:
        print("Usage: transcribe_units.py <file1.mp3> [file2.mp3 ...]")
        return 1

    print("Loading whisper base model...", flush=True)
    model = whisper.load_model("base")
    print("Model loaded.", flush=True)

    for p in paths:
        if not p.exists():
            print(f"MISSING: {p}", flush=True)
            continue
        print(f"Transcribing {p.name} ({p.stat().st_size / 1_000_000:.1f} MB)...", flush=True)
        result = transcribe(p, model)

        out_dir = p.parent.parent / "md"
        out_dir.mkdir(exist_ok=True)
        stem = p.stem

        # Full text
        (out_dir / f"{stem}_raw.txt").write_text(result["text"], encoding="utf-8")

        # Segments with timestamps
        segs = [
            {"start": s["start"], "end": s["end"], "text": s["text"].strip()}
            for s in result["segments"]
        ]
        (out_dir / f"{stem}_segments.json").write_text(
            json.dumps(segs, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"  -> {out_dir / (stem + '_raw.txt')}", flush=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())
