#!/usr/bin/env python3
"""
Download player reference photos for AI appearance description.

This script fetches player photos from multiple sources (ESPN headshot,
Wikipedia, Google image search) so Claude Code can Read the images and
auto-generate appearance descriptions for image prompts.

Usage:
    # With known ESPN ID (fastest, most reliable):
    python scripts/fetch_player_photo.py "Cameron Boozer" \
        --espn-id 5041935 \
        --output references/players/cameron-boozer

    # Auto-search (slower, tries multiple sources):
    python scripts/fetch_player_photo.py "AJ Dybantsa" \
        --school BYU \
        --output references/players/aj-dybantsa

    # Batch mode with a JSON manifest:
    python scripts/fetch_player_photo.py --batch players.json

Designed to be called by Claude Code in local environments where network
access is unrestricted. In cloud/sandboxed environments, the user should
manually place photos in the output directory instead.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Known ESPN player ID patterns for college basketball headshots
ESPN_HEADSHOT_URL = (
    "https://a.espncdn.com/combiner/i"
    "?img=/i/headshots/mens-college-basketball/players/full/{espn_id}.png"
    "&w=350&h=254"
)

# ESPN action photo (larger, shows more of the player)
ESPN_ACTION_URL = (
    "https://a.espncdn.com/combiner/i"
    "?img=/i/headshots/mens-college-basketball/players/full/{espn_id}.png"
    "&w=600&h=436"
)

# Wikipedia API for page thumbnail
WIKIPEDIA_API_URL = (
    "https://en.wikipedia.org/w/api.php"
    "?action=query&titles={title}&prop=pageimages"
    "&format=json&pithumbsize=800"
)

# User agent to avoid blocks
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def _download(url: str, output_path: Path) -> bool:
    """Download a URL to a local file. Returns True on success."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            if len(data) < 1000:
                # Too small — probably an error page or placeholder
                return False
            output_path.write_bytes(data)
            return True
    except (urllib.error.URLError, urllib.error.HTTPError, OSError) as e:
        print(f"  ↳ Download failed: {e}", file=sys.stderr)
        return False


def fetch_espn_headshot(espn_id: str, output_dir: Path) -> list[Path]:
    """Download ESPN headshot and action photo."""
    results = []
    for label, url_template in [
        ("headshot", ESPN_HEADSHOT_URL),
        ("action", ESPN_ACTION_URL),
    ]:
        url = url_template.format(espn_id=espn_id)
        out = output_dir / f"espn_{label}.png"
        print(f"  Trying ESPN {label} (ID {espn_id})...")
        if _download(url, out):
            print(f"  ✅ {out}")
            results.append(out)
    return results


def fetch_wikipedia_image(player_name: str, output_dir: Path) -> list[Path]:
    """Fetch player image via Wikipedia API."""
    title = player_name.replace(" ", "_")
    url = WIKIPEDIA_API_URL.format(title=urllib.parse.quote(title))
    print(f"  Trying Wikipedia ({title})...")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            thumb_url = page.get("thumbnail", {}).get("source")
            if thumb_url:
                ext = Path(urllib.parse.urlparse(thumb_url).path).suffix or ".jpg"
                out = output_dir / f"wikipedia{ext}"
                if _download(thumb_url, out):
                    print(f"  ✅ {out}")
                    return [out]
        print("  ↳ No image on Wikipedia page")
    except Exception as e:
        print(f"  ↳ Wikipedia API error: {e}", file=sys.stderr)
    return []


def fetch_school_roster(
    player_name: str, school: str | None, output_dir: Path
) -> list[Path]:
    """Try to fetch from school athletics site (best-effort)."""
    if not school:
        return []

    # Known school roster URL patterns
    school_urls: dict[str, str] = {
        "duke": "https://goduke.com/sports/mens-basketball/roster",
        "byu": "https://byucougars.com/sports/mens-basketball/roster",
        "kansas": "https://kuathletics.com/sports/mens-basketball/roster",
        "unc": "https://goheels.com/sports/mens-basketball/roster",
        "north carolina": "https://goheels.com/sports/mens-basketball/roster",
    }

    school_lower = school.lower()
    if school_lower not in school_urls:
        return []

    # School roster pages are hard to scrape reliably.
    # This is a placeholder for future improvement.
    print(f"  ⏭️  School roster scraping ({school}) not yet implemented")
    return []


def find_espn_id_from_search(player_name: str, school: str | None) -> str | None:
    """
    Try to find ESPN player ID by searching Google for the ESPN profile page.
    Parses the ID from the URL pattern: /player/_/id/{ID}/...

    This uses a simple HTTP request to Google search — may be rate-limited.
    """
    query = f"{player_name} {school or ''} ESPN college basketball player"
    search_url = (
        "https://www.google.com/search?"
        + urllib.parse.urlencode({"q": query, "num": 5})
    )
    try:
        req = urllib.request.Request(search_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
        # Look for ESPN player URL pattern
        match = re.search(
            r"espn\.com/mens-college-basketball/player/_/id/(\d+)", html
        )
        if match:
            return match.group(1)
    except Exception:
        pass
    return None


def fetch_player(
    player_name: str,
    output_dir: Path,
    espn_id: str | None = None,
    school: str | None = None,
) -> list[Path]:
    """
    Fetch photos for a player from all available sources.
    Returns list of successfully downloaded file paths.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    all_photos: list[Path] = []

    # 1. ESPN headshot (if ID known or discoverable)
    if not espn_id:
        print(f"  No ESPN ID provided, trying to auto-detect...")
        espn_id = find_espn_id_from_search(player_name, school)
        if espn_id:
            print(f"  Found ESPN ID: {espn_id}")

    if espn_id:
        all_photos.extend(fetch_espn_headshot(espn_id, output_dir))

    # 2. Wikipedia
    all_photos.extend(fetch_wikipedia_image(player_name, output_dir))

    # 3. School roster (future)
    all_photos.extend(fetch_school_roster(player_name, school, output_dir))

    return all_photos


def run_single(args: argparse.Namespace) -> int:
    """Fetch photos for a single player."""
    print(f"\n🔍 Fetching photos: {args.player_name}")
    output_dir = Path(args.output)
    photos = fetch_player(
        args.player_name,
        output_dir,
        espn_id=args.espn_id,
        school=args.school,
    )

    if photos:
        print(f"\n✅ {len(photos)} photo(s) saved to {output_dir}/")
        print("   Next step: Claude Code runs Read on each photo → generates appearance.md")
        return 0
    else:
        print(f"\n❌ No photos found for {args.player_name}")
        print(f"   Fallback: manually save a photo to {output_dir}/photo.jpg")
        return 1


def run_batch(args: argparse.Namespace) -> int:
    """
    Fetch photos for multiple players from a JSON manifest.

    Manifest format:
    [
        {
            "name": "Cameron Boozer",
            "school": "Duke",
            "espn_id": "5041935",
            "output": "references/players/cameron-boozer"
        },
        ...
    ]
    """
    manifest_path = Path(args.batch)
    if not manifest_path.exists():
        print(f"❌ Manifest not found: {manifest_path}", file=sys.stderr)
        return 1

    players = json.loads(manifest_path.read_text())
    total = len(players)
    success = 0

    for i, player in enumerate(players, 1):
        name = player["name"]
        print(f"\n[{i}/{total}] {name}")
        photos = fetch_player(
            name,
            Path(player["output"]),
            espn_id=player.get("espn_id"),
            school=player.get("school"),
        )
        if photos:
            success += 1

    print(f"\n{'='*40}")
    print(f"Done: {success}/{total} players with photos")
    if success < total:
        print(f"Missing {total - success} — manually add photos or provide ESPN IDs")
    return 0 if success == total else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch player reference photos for AI appearance description"
    )
    # Single player mode
    parser.add_argument("player_name", nargs="?", help="Player full name")
    parser.add_argument("--espn-id", help="ESPN player ID (fastest source)")
    parser.add_argument("--school", help="School name (e.g. Duke, BYU)")
    parser.add_argument("--output", help="Output directory")
    # Batch mode
    parser.add_argument("--batch", help="JSON manifest for batch downloads")

    args = parser.parse_args()

    if args.batch:
        return run_batch(args)
    elif args.player_name and args.output:
        return run_single(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
