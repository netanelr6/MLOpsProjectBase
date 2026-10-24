#!/usr/bin/env python3
"""Stop hook: mirror project files into the Obsidian vault.

Diffs the project tree against a manifest (.claude/vault-sync-state.json) to
find created / edited / deleted files since the last run, then updates the
matching notes under <vault>/Project Mirror/. Markdown files are copied as-is
(links untouched; folder layout is mirrored so relative links still resolve).
Other text files become `<name>.<ext>.md` notes wrapping the content in a code
block. The vault folder itself is never scanned, so syncing cannot loop.
"""
import hashlib
import json
import os
import sys
from pathlib import Path

PROJECT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()).resolve()
VAULT = Path(os.environ.get("VAULT_DIR") or PROJECT / "project_mind").resolve()
MIRROR_NAME = "Project Mirror"
MIRROR = VAULT / MIRROR_NAME
STATE = PROJECT / ".claude" / "vault-sync-state.json"

SKIP_DIRS = {".git", ".claude", ".obsidian", "node_modules", "__pycache__", ".venv", "dist", "build"}
TEXT_EXT = {".py", ".js", ".ts", ".tsx", ".jsx", ".json", ".yaml", ".yml", ".toml", ".sh",
            ".html", ".css", ".txt", ".csv", ".sql", ".ini", ".cfg", ".java", ".c", ".cpp",
            ".go", ".rs", ".ps1", ".bat"}
MAX_BYTES = 1_000_000


def inside_vault(p: Path) -> bool:
    try:
        p.resolve().relative_to(VAULT)
        return True
    except ValueError:
        return False


def scan() -> dict:
    found = {}
    for root, dirs, files in os.walk(PROJECT):
        rp = Path(root)
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not inside_vault(rp / d)]
        for f in files:
            p = rp / f
            ext = p.suffix.lower()
            if ext != ".md" and ext not in TEXT_EXT:
                continue
            try:
                if p.stat().st_size > MAX_BYTES:
                    continue
                found[p.relative_to(PROJECT).as_posix()] = hashlib.sha1(p.read_bytes()).hexdigest()
            except OSError:
                pass
    return found


def target_for(rel: str) -> Path:
    return MIRROR / (rel if rel.lower().endswith(".md") else rel + ".md")


def write_note(rel: str):
    src = PROJECT / rel
    text = src.read_text(encoding="utf-8", errors="replace")
    dst = target_for(rel)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if rel.lower().endswith(".md"):
        out = text  # keep wikilinks / markdown links exactly as written
    else:
        fence = "```"
        while fence in text:
            fence += "`"
        lang = src.suffix.lstrip(".")
        out = (f"---\nsource: {rel}\ntags:\n  - project-file\n---\n\n"
               f"# {src.name}\n\n{fence}{lang}\n{text.rstrip()}\n{fence}\n")
    dst.write_text(out, encoding="utf-8", newline="\n")


def remove_note(rel: str):
    dst = target_for(rel)
    if dst.exists():
        dst.unlink()
    d = dst.parent
    while d != MIRROR and d.is_dir() and not any(d.iterdir()):
        d.rmdir()
        d = d.parent


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    if payload.get("stop_hook_active"):
        return
    if not VAULT.is_dir():
        print(f"vault-sync: vault not found: {VAULT}", file=sys.stderr)
        return

    try:
        old = json.loads(STATE.read_text(encoding="utf-8"))
    except Exception:
        old = {}
    new = scan()

    changed = [r for r, h in new.items() if old.get(r) != h]
    deleted = [r for r in old if r not in new]
    for r in changed:
        write_note(r)
    for r in deleted:
        remove_note(r)

    STATE.write_text(json.dumps(new, indent=1, ensure_ascii=False), encoding="utf-8")
    if changed or deleted:
        print(f"vault-sync: {len(changed)} updated, {len(deleted)} removed", file=sys.stderr)


if __name__ == "__main__":
    main()
