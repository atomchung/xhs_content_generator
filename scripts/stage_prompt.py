#!/usr/bin/env python3
"""Stage one or more prompt files: commit, push, print GitHub blob URL(s).

Typical use (after editing a prompt file):

    python scripts/stage_prompt.py demo_posts/<slug>/prompts/cover_prompt.md

Multiple files and a custom message are also OK:

    python scripts/stage_prompt.py path1.md path2.md -m "prompts: tatum v5 defense pose"

The script:
  1. git add <files>
  2. git commit (only if there are staged changes for those files)
  3. git push -u origin <current-branch>
  4. prints one GitHub blob URL per file — paste these into the chat reply
     so the user can click straight into the ```text``` code block and copy.

Design notes:
  - Branch is whatever `git rev-parse --abbrev-ref HEAD` reports. No auto
    branch creation — if you need a feature branch, create it yourself first.
  - If nothing changed, skips commit but still pushes (in case a prior commit
    wasn't pushed) and still prints URLs. This keeps the chat reply stable
    even when re-running on an unchanged file.
  - Remote URL is normalized from git@github.com:org/repo(.git) to
    https://github.com/org/repo so the blob link is clickable.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], check: bool = True) -> str:
    """Run a command, return stdout stripped. Raises on non-zero when check=True."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=check)
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(f"command failed: {' '.join(cmd)}\n")
        if exc.stdout:
            sys.stderr.write(exc.stdout)
        if exc.stderr:
            sys.stderr.write(exc.stderr)
        raise
    return result.stdout.strip()


def git_branch() -> str:
    return run(["git", "rev-parse", "--abbrev-ref", "HEAD"])


def git_repo_root() -> Path:
    return Path(run(["git", "rev-parse", "--show-toplevel"]))


def git_remote_blob_base() -> str:
    """Return https base for blob URLs, e.g. https://github.com/owner/repo."""
    url = run(["git", "config", "--get", "remote.origin.url"])
    if url.startswith("git@github.com:"):
        url = "https://github.com/" + url[len("git@github.com:") :]
    if url.startswith("ssh://git@github.com/"):
        url = "https://github.com/" + url[len("ssh://git@github.com/") :]
    if url.endswith(".git"):
        url = url[:-4]
    return url


def has_staged_changes(rel_paths: list[str]) -> bool:
    """Return True if the given paths have staged changes vs HEAD."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet", "--", *rel_paths],
        capture_output=True,
    )
    # --quiet: exit code 1 means diff exists, 0 means no diff
    return result.returncode != 0


def derive_commit_message(rel_paths: list[str]) -> str:
    if len(rel_paths) == 1:
        return f"prompts: update {Path(rel_paths[0]).name}"
    return f"prompts: update {len(rel_paths)} prompt files"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Commit, push, and print GitHub blob URLs for prompt files.",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Prompt file path(s), relative to repo root or absolute.",
    )
    parser.add_argument(
        "-m",
        "--message",
        help="Custom commit message. Defaults to 'prompts: update <name>'.",
    )
    parser.add_argument(
        "--no-push",
        action="store_true",
        help="Skip the push step (still commits). Use when iterating locally.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would happen, do not run git commands.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()

    repo_root = git_repo_root()

    # Resolve inputs to repo-relative paths, validate existence and scope.
    rel_paths: list[str] = []
    for raw in args.paths:
        p = Path(raw).resolve()
        if not p.exists():
            sys.stderr.write(f"error: {p} does not exist\n")
            return 1
        try:
            rel = p.relative_to(repo_root)
        except ValueError:
            sys.stderr.write(f"error: {p} is outside repo {repo_root}\n")
            return 1
        rel_paths.append(str(rel))

    branch = git_branch()
    blob_base = git_remote_blob_base()

    if args.dry_run:
        print("DRY RUN — no git commands executed")
        print(f"  branch: {branch}")
        print(f"  would add: {rel_paths}")
        print(f"  would commit: {args.message or derive_commit_message(rel_paths)}")
        if not args.no_push:
            print(f"  would push: origin {branch}")
        print()
        for rel in rel_paths:
            print(f"  {blob_base}/blob/{branch}/{rel}")
        return 0

    run(["git", "add", "--", *rel_paths])

    if has_staged_changes(rel_paths):
        message = args.message or derive_commit_message(rel_paths)
        run(["git", "commit", "-m", message])
    else:
        sys.stderr.write("no new changes in given files; skipping commit\n")

    if not args.no_push:
        run(["git", "push", "-u", "origin", branch])

    # Blank line before URLs so they're easy to spot in terminal output.
    print()
    for rel in rel_paths:
        print(f"{blob_base}/blob/{branch}/{rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
