#!/usr/bin/env python3
"""Check Agent Skills (SKILL.md folders) against the layout rules in Anthropic's skill best-practices page.

Works for skills aimed at Claude, Codex, Pi, Hermes or any tool that reads SKILL.md.
Rules that only Claude enforces are reported as NOTE and never fail a skill.

Usage: python3 skill_lint.py <skill folder | folder of skills> [...]
Standard library only. Prints one line per finding; exits 1 if any FAIL.
"""
import ast
import re
import sys
from pathlib import Path

BODY_MAX = 500        # SKILL.md body lines
TOC_OVER = 100        # reference files longer than this need a contents list
NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
LINK_RE = re.compile(r"\(([^)\s]+\.md)\)|`([^`\s]+\.md)`|(?<![\w/.-])([\w./-]+\.md)\b")
TOC_RE = re.compile(r"^#{1,6}\s*(contents|table of contents|sommaire|index)\b", re.I)
STDLIB = set(getattr(sys, "stdlib_module_names", ()))


def frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end < 0:
        return None, text
    meta, key = {}, None
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if m:
            key, value = m.group(1), m.group(2).strip()
            # A YAML block scalar (description: >-) continues on the indented lines below.
            meta[key] = "" if re.fullmatch(r"[>|][+-]?", value) else value.strip("\"'")
        elif key and line[:1] in (" ", "\t") and line.strip():
            meta[key] = (meta[key] + " " + line.strip()).strip()
    return meta, text[end + 4:].lstrip("\n")


def links(path, root):
    found = set()
    for m in LINK_RE.finditer(path.read_text(encoding="utf-8", errors="replace")):
        ref = next(g for g in m.groups() if g)
        if "://" in ref:
            continue
        for base in (path.parent, root):
            target = (base / ref).resolve()
            if target.is_file():
                found.add(target)
                break
    return found


def third_party_imports(path):
    try:
        tree = ast.parse(path.read_text(encoding="utf-8", errors="replace"))
    except SyntaxError:
        return set()
    mods = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            mods |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
            mods.add(node.module.split(".")[0])
    return {m for m in mods if m not in STDLIB}


def check(skill):
    out = []
    add = lambda level, msg: out.append((level, msg))
    main = skill / "SKILL.md"
    if not main.is_file():
        add("FAIL", "no SKILL.md")
        return out
    text = main.read_text(encoding="utf-8", errors="replace")
    meta, body = frontmatter(text)
    if meta is None:
        add("FAIL", "SKILL.md has no frontmatter block")
        meta = {}
    name, desc = meta.get("name", ""), meta.get("description", "")
    if not name:
        add("FAIL", "frontmatter has no name")
    elif not NAME_RE.match(name):
        add("FAIL", f"name '{name}': use lowercase letters, digits and hyphens, max 64")
    elif "anthropic" in name or "claude" in name:
        add("NOTE", f"name '{name}' contains 'anthropic' or 'claude': fine for Codex, Pi, Hermes and other tools, but an upload to claude.ai or the Claude API rejects it")
    if not desc:
        add("FAIL", "frontmatter has no description, so the assistant cannot know when to use the skill")
    elif len(desc) > 1024:
        add("FAIL", f"description is {len(desc)} characters, the limit is 1024")
    n = len(body.splitlines())
    if n > BODY_MAX:
        add("FAIL", f"SKILL.md body is {n} lines; keep it under {BODY_MAX} and move detail to reference files")

    # Only files the assistant can reach from SKILL.md count: a README or CHANGELOG for humans is not its.
    direct = links(main, skill) - {main.resolve()}
    reach, frontier = dict.fromkeys(direct, main), list(direct)
    while frontier:
        f = frontier.pop()
        if f.suffix == ".md":
            for t in links(f, skill):
                if t not in reach and t != main.resolve():
                    reach[t] = f
                    frontier.append(t)
    root = skill.resolve()
    for ref in sorted(reach):
        rel = ref.relative_to(root) if ref.is_relative_to(root) else ref
        lines = ref.read_text(encoding="utf-8", errors="replace").splitlines()
        if len(lines) > TOC_OVER and not any(TOC_RE.match(l) for l in lines[:40]):
            add("WARN", f"{rel} is {len(lines)} lines with no contents list at the top")
        if ref not in direct:
            via = reach[ref].relative_to(root) if reach[ref].is_relative_to(root) else reach[ref]
            add("WARN", f"{rel} is reached only through {via}; link it from SKILL.md (the assistant may read only its first lines)")

    local = {p.stem for p in skill.rglob("*.py")} | {d.name for d in skill.rglob("*") if d.is_dir()}
    missing = {}
    for script in sorted(skill.rglob("*.py")):
        if script.resolve() == Path(__file__).resolve() or "test" in script.relative_to(skill).parts[0]:
            continue
        for mod in third_party_imports(script) - local:
            if not re.search(rf"install[^\n]*\b{re.escape(mod)}\b", text, re.I):
                missing.setdefault(mod, script.relative_to(skill))
    for mod, script in sorted(missing.items()):
        add("WARN", f"'{mod}' is imported ({script}) but SKILL.md has no install line for it")
    return out


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 2
    skills = []
    for arg in argv:
        p = Path(arg).expanduser()
        if (p / "SKILL.md").is_file():
            skills.append(p)
        elif p.is_dir():
            skills += sorted(d for d in p.iterdir() if (d / "SKILL.md").is_file())
    if not skills:
        print("no skill found (a skill is a folder holding SKILL.md)")
        return 2
    failed = False
    for skill in skills:
        found = check(skill)
        failed |= any(level == "FAIL" for level, _ in found)
        print(f"{skill.name}: {'ok' if not found else ''}")
        for level, msg in found:
            print(f"  {level}  {msg}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
