"""Generate cover/character/atmosphere images via the higgs-audio image API.

The Windows-side service exposes:
- POST /api/image/generate     (prompt + negative_prompt + width + height + steps + seed)
- GET  /api/image/status/{id}  (returns "pending" | "running" | "done" + image metadata)
- GET  /api/image/view         (filename + subfolder + type → image bytes)

Auth via the shared TTS_API_KEY (Bearer token); same key used by audiobook.py.

Usage:
    python build/imagegen.py "RV Nansen at Punta Arenas pier, ice-class research submarine, soft September morning light, photorealistic" \
        --slug nansen-departure-cover --category covers --width 1024 --height 768 --steps 30

    python build/imagegen.py --batch chapters/book-2/_image-prompts.yaml

Each generation:
  1. POSTs the prompt; receives prompt_id
  2. Polls /api/image/status/{prompt_id} until done (or timeout)
  3. Downloads the image via /api/image/view
  4. Saves to build/output/images/<category>/<slug>.png (gitignored)
  5. Auto-copies to ~/Dropbox/the-inverted-stack/images/<category>/<slug>.png
     (silent skip if Dropbox not present; mirror of audiobook.py auto-sync)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path
from typing import Any

import httpx

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "build" / "output" / "images"

DEFAULT_BASE_URL = "http://desktop-umt08rn:8881"
DEFAULT_CATEGORY = "misc"

DROPBOX_BASE_DEFAULT = (
    Path.home() / "Library" / "CloudStorage" / "Dropbox"
    / "the-inverted-stack"
)

# Category → Dropbox subfolder mapping. Matches the vol-N audiobook pattern.
CANONICAL_CATEGORIES = {
    "covers",       # cover-art concepts
    "characters",   # per-character reference sketches
    "settings",     # ice shelf; Punta Arenas; the Nansen exterior; compartment interiors
    "atmosphere",   # mood / lighting / non-character mission stills
    "misc",         # uncategorized
}


def slugify(text: str, max_len: int = 64) -> str:
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:max_len] or "untitled"


def post_generate(client: httpx.Client, prompt: str, *, negative_prompt: str = "",
                  width: int = 1024, height: int = 768, steps: int = 30,
                  seed: int = -1) -> str:
    """Submit a generation request; return the prompt_id."""
    body = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": width,
        "height": height,
        "steps": steps,
        "seed": seed,
    }
    r = client.post("/api/image/generate", json=body, timeout=30.0)
    r.raise_for_status()
    return r.json()["prompt_id"]


def poll_status(client: httpx.Client, prompt_id: str, *, max_wait: float = 300.0,
                poll_interval: float = 1.5, verbose: bool = True) -> dict[str, Any]:
    """Poll until the generation is done (or timeout). Returns the final status payload."""
    start = time.time()
    last_status = None
    while True:
        r = client.get(f"/api/image/status/{prompt_id}", timeout=15.0)
        r.raise_for_status()
        data = r.json()
        status = data.get("status")
        if verbose and status != last_status:
            print(f"  status: {status}")
            last_status = status
        if status == "done":
            return data
        if status == "error" or "error" in data:
            raise RuntimeError(f"Image generation failed: {data}")
        if time.time() - start > max_wait:
            raise TimeoutError(f"Generation did not complete within {max_wait}s; last status={data}")
        time.sleep(poll_interval)


def download_image(client: httpx.Client, image_meta: dict[str, Any], dest: Path) -> int:
    """Download a generated image to `dest`. Returns bytes written."""
    params = {
        "filename": image_meta["filename"],
        "subfolder": image_meta.get("subfolder", ""),
        "type": image_meta.get("type", "output"),
    }
    r = client.get("/api/image/view", params=params, timeout=60.0)
    r.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(r.content)
    return len(r.content)


def sync_to_dropbox(out_path: Path, category: str, *, verbose: bool = True) -> bool:
    """Copy the generated image to ~/Dropbox/the-inverted-stack/images/<category>/."""
    base = Path(os.environ.get("DROPBOX_AUDIOBOOK_BASE", str(DROPBOX_BASE_DEFAULT)))
    if not base.exists():
        return False
    dest_dir = base / "images" / category
    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / out_path.name
        shutil.copy2(out_path, dest)
        if verbose:
            kb = out_path.stat().st_size / 1024
            print(f"  → Dropbox: images/{category}/{out_path.name}  ({kb:.0f} KB)")
        return True
    except Exception as e:
        if verbose:
            print(f"  → Dropbox sync skipped ({type(e).__name__}: {e})", file=sys.stderr)
        return False


def generate_one(client: httpx.Client, prompt: str, *, slug: str, category: str,
                 negative_prompt: str = "", width: int = 1024, height: int = 768,
                 steps: int = 30, seed: int = -1, verbose: bool = True) -> Path:
    """End-to-end generation: submit → poll → download → save → sync."""
    if category not in CANONICAL_CATEGORIES:
        print(f"  warning: category {category!r} not in canonical set "
              f"{sorted(CANONICAL_CATEGORIES)}; using anyway", file=sys.stderr)

    if verbose:
        print(f"Generating: {slug} ({category}, {width}×{height}, {steps} steps)")
        print(f"  prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")

    t0 = time.time()
    prompt_id = post_generate(client, prompt,
                              negative_prompt=negative_prompt,
                              width=width, height=height,
                              steps=steps, seed=seed)
    if verbose:
        print(f"  prompt_id: {prompt_id}")

    final = poll_status(client, prompt_id, verbose=verbose)
    images = final.get("images", [])
    if not images:
        raise RuntimeError(f"Generation done but no images returned: {final}")

    # Use first image; multi-image batches surface only the first by default.
    out_path = OUT_DIR / category / f"{slug}.png"
    n_bytes = download_image(client, images[0], out_path)
    elapsed = time.time() - t0
    if verbose:
        print(f"  saved: {out_path.relative_to(REPO)}  ({n_bytes / 1024:.0f} KB; {elapsed:.1f}s)")
    sync_to_dropbox(out_path, category, verbose=verbose)
    return out_path


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Generate images via the higgs-audio /api/image/generate endpoint.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("prompt", nargs="?", help="The image generation prompt.")
    ap.add_argument("--negative-prompt", default="text, watermark, signature, blurry, low quality",
                    help="Negative prompt; default targets common artefacts.")
    ap.add_argument("--slug", default=None,
                    help="Output filename slug (without .png). Default: derived from prompt.")
    ap.add_argument("--category", default=DEFAULT_CATEGORY,
                    choices=sorted(CANONICAL_CATEGORIES),
                    help=f"Output subdirectory category. Default: {DEFAULT_CATEGORY}.")
    ap.add_argument("--width", type=int, default=1024)
    ap.add_argument("--height", type=int, default=768)
    ap.add_argument("--steps", type=int, default=30)
    ap.add_argument("--seed", type=int, default=-1, help="-1 = random.")
    ap.add_argument("--base-url", default=os.environ.get("IMAGE_API_BASE", DEFAULT_BASE_URL))
    ap.add_argument("--api-key", default=os.environ.get("TTS_API_KEY"),
                    help="Bearer token; default: TTS_API_KEY env (shared with audiobook.py).")
    ap.add_argument("--no-dropbox-sync", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not args.prompt:
        ap.error("prompt is required")
    if not args.api_key:
        ap.error("API key required: set TTS_API_KEY env or pass --api-key")

    slug = args.slug or slugify(args.prompt)
    verbose = not args.quiet

    headers = {"Authorization": f"Bearer {args.api_key}"}
    with httpx.Client(base_url=args.base_url, headers=headers,
                      timeout=httpx.Timeout(60.0, connect=10.0)) as client:
        generate_one(client, args.prompt,
                     slug=slug,
                     category=args.category,
                     negative_prompt=args.negative_prompt,
                     width=args.width, height=args.height,
                     steps=args.steps, seed=args.seed,
                     verbose=verbose)


if __name__ == "__main__":
    main()
