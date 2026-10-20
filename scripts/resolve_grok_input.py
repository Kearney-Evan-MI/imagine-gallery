#!/usr/bin/env python3
"""Resolve Grok Imagine input into the JSON payload Grok needs.

Accepts a UUID, @tag, grok.com/imagine URL, character slug/name, frame id,
or skill name. Prints a single JSON object on stdout.

Examples:
    python3 scripts/resolve_grok_input.py "kate"
    python3 scripts/resolve_grok_input.py "@ff0116d1-7647-49a9-a4a1-7c05b5e80c7f"
    python3 scripts/resolve_grok_input.py "https://grok.com/imagine/post/ff0116d1-7647-49a9-a4a1-7c05b5e80c7f"
    python3 scripts/resolve_grok_input.py --list
    python3 scripts/resolve_grok_input.py --write-catalog
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Optional
from urllib.parse import parse_qs, urlparse

REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_VERSION = 1
UUID_RE = re.compile(
    r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}"
)
FRAME_ID_RE = re.compile(r"`([A-Za-z0-9]{4,8})`")
FIELD_RE = re.compile(r"^\*\*(.+?):\*\*\s*(.*)$")
PAGES_CATALOG = "https://kearney-evan-mi.github.io/imagine-gallery/grok.json"
REPO_BLOB = "https://github.com/Kearney-Evan-MI/imagine-gallery/blob/main"

DEFAULT_SKILLS = [
    "imagine-restyle",
    "photoreal-phenotype-prompts",
    "pretty-women-photorealism",
]
INTENT_SKILLS = {
    "restyle": ["imagine-restyle", "photoreal-phenotype-prompts", "pretty-women-photorealism"],
    "generate": ["photoreal-phenotype-prompts", "pretty-women-photorealism"],
    "video": ["grok-imagine"],
    "animate": ["grok-imagine"],
    "api": ["grok-imagine"],
}


def repo_root() -> Path:
    return REPO_ROOT


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _field_map(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in text.splitlines():
        m = FIELD_RE.match(line.strip())
        if m:
            out[m.group(1).strip().lower()] = m.group(2).strip()
    return out


def _section_bullets(text: str, heading: str) -> list[str]:
    lines = text.splitlines()
    capture = False
    bullets: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.lower().startswith(f"**{heading.lower()}") or stripped.lower().startswith(
            f"# {heading.lower()}"
        ):
            capture = True
            continue
        if capture:
            if stripped.startswith("**") or (stripped.startswith("#") and not stripped.startswith("# ")):
                if not stripped.lower().startswith(f"**{heading.lower()}"):
                    break
            if stripped.startswith("- "):
                bullets.append(stripped[2:].strip())
            elif stripped.startswith("#") or (stripped.startswith("**") and stripped.endswith("**") and ":" not in stripped):
                break
    return bullets


def _backticks_after(text: str, heading: str) -> list[str]:
    lines = text.splitlines()
    capture = False
    found: list[str] = []
    for line in lines:
        stripped = line.strip()
        if heading.lower() in stripped.lower() and stripped.startswith("**"):
            capture = True
            found.extend(FRAME_ID_RE.findall(stripped))
            continue
        if capture:
            if stripped.startswith("**") and heading.lower() not in stripped.lower():
                break
            found.extend(FRAME_ID_RE.findall(stripped))
            if stripped.startswith("#"):
                break
    return found


def _uuids_in(text: str) -> list[str]:
    seen: list[str] = []
    for match in UUID_RE.findall(text):
        value = match.lower()
        if value not in seen:
            seen.append(value)
    return seen


def _skill_entry(name: str, path: Path) -> dict[str, Any]:
    rel = path.relative_to(repo_root()).as_posix()
    description = ""
    if path.exists():
        text = _read(path)
        m = re.search(r"^description:\s*(.+)$", text, re.M)
        if m:
            description = m.group(1).strip()
    session = (
        f"/home/workdir/.grok/skills/{name}/"
        if name != "grok-imagine"
        else "/home/workdir/.grok/skills/grok-imagine/"
    )
    return {
        "name": name,
        "path": rel,
        "github": f"{REPO_BLOB}/{rel}",
        "session_copy": session,
        "description": description,
    }


def load_skills() -> list[dict[str, Any]]:
    skills: list[dict[str, Any]] = []
    skills_dir = repo_root() / "skills"
    if skills_dir.is_dir():
        for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
            name = skill_md.parent.name
            skills.append(_skill_entry(name, skill_md))
    toolkit = repo_root() / "integrations" / "grok-imagine-toolkit" / "SKILL.md"
    if toolkit.exists():
        skills.append(_skill_entry("grok-imagine", toolkit))
    return skills


def _generation_rows(slug: str) -> list[dict[str, str]]:
    gen_readme = repo_root() / "characters" / slug / "generations" / "README.md"
    if not gen_readme.exists():
        return []
    rows: list[dict[str, str]] = []
    for line in _read(gen_readme).splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        if cells[0].lower() in {"uuid", "------", ""} or set(cells[0]) <= {"-"}:
            continue
        uuid = cells[0].lower()
        if not UUID_RE.fullmatch(uuid):
            continue
        rows.append(
            {
                "uuid": uuid,
                "description": cells[1] if len(cells) > 1 else "",
                "source": cells[2] if len(cells) > 2 else "",
                "post_url": f"https://grok.com/imagine/post/{uuid}",
            }
        )
    return rows


def load_characters() -> list[dict[str, Any]]:
    characters: list[dict[str, Any]] = []
    root = repo_root() / "characters"
    if not root.is_dir():
        return characters
    for bible in sorted(root.glob("*/character-bible.md")):
        slug = bible.parent.name
        text = _read(bible)
        fields = _field_map(text)
        name = fields.get("character") or fields.get("name / alias") or slug
        name = re.sub(r"\(unnamed.*", "", name).strip() or slug.replace("-", " ")
        aliases = [
            slug,
            slug.replace("-", " "),
            name,
            fields.get("name / alias", ""),
        ]
        if slug == "green-eyed-woman":
            aliases.extend(["green eyed woman", "green-eyed woman", "the green-eyed woman"])
        if slug == "new-forest-spunk":
            aliases.extend(["new forest", "new forest spunk"])
        aliases = [a.strip() for a in aliases if a and a.strip() and "unnamed" not in a.lower()]
        frame_ids = _backticks_after(text, "Frame ids")
        uuids = _uuids_in(text)
        generations = _generation_rows(slug)
        for row in generations:
            if row["uuid"] not in uuids:
                uuids.append(row["uuid"])
        if slug == "green-eyed-woman":
            readme = repo_root() / "README.md"
            if readme.exists():
                for uid in _uuids_in(_read(readme)):
                    if uid not in uuids:
                        uuids.append(uid)
        tags = [f"@{uid}" for uid in uuids] + [f"@{fid}" for fid in frame_ids]
        characters.append(
            {
                "slug": slug,
                "name": name,
                "status": fields.get("status", "Active"),
                "version": fields.get("current version", ""),
                "regional_lock": fields.get("regional lock", ""),
                "aliases": list(dict.fromkeys(aliases)),
                "core_look": _section_bullets(text, "Core Look"),
                "signature_clothing": _section_bullets(text, "Signature Clothing")
                or _section_bullets(text, "Signature Outfit")
                or _section_bullets(text, "Signature Clothing & State"),
                "settings": _section_bullets(text, "Recurring Settings")
                or _section_bullets(text, "Recurring Settings & Theme"),
                "frame_ids": frame_ids,
                "uuids": uuids,
                "imagine_tags": tags,
                "generations": generations,
                "bible_path": bible.relative_to(repo_root()).as_posix(),
                "bible": text,
                "github": f"{REPO_BLOB}/{bible.relative_to(repo_root()).as_posix()}",
            }
        )
    return characters


def normalize_query(raw: str) -> dict[str, Any]:
    text = (raw or "").strip()
    parsed: dict[str, Any] = {
        "raw": raw,
        "text": text,
        "uuid": None,
        "frame_id": None,
        "skill": None,
        "url": None,
        "slug_hint": None,
    }
    if not text:
        return parsed
    uuid_match = UUID_RE.search(text)
    if uuid_match:
        parsed["uuid"] = uuid_match.group(0).lower()
    if text.startswith("http://") or text.startswith("https://"):
        parsed["url"] = text
        url = urlparse(text)
        qs = parse_qs(url.query)
        if "skill" in qs:
            parsed["skill"] = qs["skill"][0]
        path = url.path.rstrip("/")
        if "/imagine/post/" in path:
            parsed["uuid"] = path.rsplit("/", 1)[-1].lower()
    if text.lower().startswith("characters/"):
        parsed["slug_hint"] = text.split("/", 1)[1].strip("/").split("/")[0]
    if text.startswith("@") and not parsed["uuid"]:
        token = text[1:].strip()
        if UUID_RE.fullmatch(token):
            parsed["uuid"] = token.lower()
        else:
            parsed["frame_id"] = token
    if re.fullmatch(r"[A-Za-z0-9]{4,8}", text) and not parsed["uuid"]:
        parsed["frame_id"] = text
    return parsed


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _score_character(query: dict[str, Any], character: dict[str, Any]) -> int:
    score = 0
    if query.get("uuid") and query["uuid"] in character["uuids"]:
        score += 100
    if query.get("frame_id"):
        fid = query["frame_id"]
        if fid in character["frame_ids"]:
            score += 90
        elif fid.lower() in [f.lower() for f in character["frame_ids"]]:
            score += 80
    hint = query.get("slug_hint") or query.get("text") or ""
    n_hint = _norm(hint.lstrip("@"))
    if not n_hint:
        return score
    if n_hint == _norm(character["slug"]):
        score += 70
    if n_hint == _norm(character["name"]):
        score += 65
    for alias in character["aliases"]:
        n_alias = _norm(alias)
        if n_hint == n_alias:
            score += 60
        elif n_hint and n_hint in n_alias:
            score += 25
        elif n_alias and n_alias in n_hint:
            score += 20
    return score


def _skill_by_name(name: str, skills: list[dict[str, Any]]) -> Optional[dict[str, Any]]:
    key = _norm(name)
    for skill in skills:
        if _norm(skill["name"]) == key:
            return skill
    return None


def _skills_for_intent(intent: str, skills: list[dict[str, Any]]) -> list[dict[str, Any]]:
    names = INTENT_SKILLS.get(intent or "restyle", DEFAULT_SKILLS)
    out: list[dict[str, Any]] = []
    for name in names:
        entry = _skill_by_name(name, skills)
        if entry:
            out.append(entry)
    return out


def _identity_instruction(character: dict[str, Any]) -> str:
    tags = ", ".join(character["imagine_tags"][:8]) or character["slug"]
    lock = character.get("regional_lock") or "existing identity"
    look = "; ".join(character.get("core_look") or [])
    parts = [
        f"Use the {character['name']} lock from imagine-gallery (`{character['slug']}`).",
        f"Identity tags: {tags}.",
        f"Regional lock: {lock}.",
    ]
    if look:
        parts.append(f"Core look: {look}.")
    parts.append("Do not invent a new face. Follow the character bible.")
    return " ".join(parts)


def grok_return_for_character(
    character: dict[str, Any],
    *,
    intent: str,
    skills: list[dict[str, Any]],
    matched_on: str,
) -> dict[str, Any]:
    chosen = _skills_for_intent(intent, skills)
    post_url = None
    if character["uuids"]:
        post_url = f"https://grok.com/imagine/post/{character['uuids'][0]}"
        for row in character.get("generations") or []:
            if "new post" in (row.get("description") or "").lower():
                post_url = row["post_url"]
                break
    return {
        "kind": "character",
        "matched_on": matched_on,
        "slug": character["slug"],
        "name": character["name"],
        "imagine_tags": character["imagine_tags"],
        "frame_ids": character["frame_ids"],
        "uuids": character["uuids"],
        "identity_instruction": _identity_instruction(character),
        "bible_path": character["bible_path"],
        "bible": character["bible"],
        "skills": chosen,
        "toolkit_path": "integrations/grok-imagine-toolkit/",
        "post_url": post_url,
        "next_actions": [
            "Load the listed skills into the Grok session.",
            "Tag the imagine_tags (or re-upload refs) before generating.",
            "Keep phenotype, bone structure, and camera distance locked.",
        ],
    }


def grok_return_for_skill(skill: dict[str, Any]) -> dict[str, Any]:
    return {
        "kind": "skill",
        "matched_on": "skill",
        "name": skill["name"],
        "path": skill["path"],
        "session_copy": skill["session_copy"],
        "instruction": (
            f"Load `{skill['path']}` into {skill['session_copy']} and follow that skill. "
            "For a character lock, resolve a slug or UUID with this same script."
        ),
        "skills": [skill],
        "next_actions": [
            f"Copy {skill['path']} to {skill['session_copy']}",
            "Run scripts/resolve_grok_input.py with a character slug or UUID when identity lock is required.",
        ],
    }


def resolve(raw: str, *, intent: str = "restyle") -> dict[str, Any]:
    skills = load_skills()
    characters = load_characters()
    query = normalize_query(raw)
    text = query["text"]

    if query.get("skill"):
        skill = _skill_by_name(query["skill"], skills)
        if skill:
            return {
                "ok": True,
                "query": raw,
                "intent": intent,
                "catalog": PAGES_CATALOG,
                "grok_return": grok_return_for_skill(skill),
            }

    if text:
        skill = _skill_by_name(text, skills) or _skill_by_name(text.replace("_", "-"), skills)
        if skill and not query.get("uuid") and not query.get("frame_id"):
            return {
                "ok": True,
                "query": raw,
                "intent": intent,
                "catalog": PAGES_CATALOG,
                "grok_return": grok_return_for_skill(skill),
            }

    ranked = sorted(
        ((_score_character(query, c), c) for c in characters),
        key=lambda item: item[0],
        reverse=True,
    )
    if ranked and ranked[0][0] > 0:
        score, character = ranked[0]
        matched_on = "text"
        if query.get("uuid") and query["uuid"] in character["uuids"]:
            matched_on = "uuid"
        elif query.get("frame_id"):
            matched_on = "frame_id"
        elif query.get("slug_hint"):
            matched_on = "slug"
        return {
            "ok": True,
            "query": raw,
            "intent": intent,
            "catalog": PAGES_CATALOG,
            "score": score,
            "grok_return": grok_return_for_character(
                character, intent=intent, skills=skills, matched_on=matched_on
            ),
        }

    suggestions = [
        {"slug": c["slug"], "name": c["name"], "imagine_tags": c["imagine_tags"][:4]}
        for c in characters
    ]
    return {
        "ok": False,
        "query": raw,
        "intent": intent,
        "catalog": PAGES_CATALOG,
        "error": "No character, UUID, frame id, or skill matched that input.",
        "suggestions": suggestions,
        "grok_return": {
            "kind": "unresolved",
            "instruction": (
                "Ask for a character slug (characters/kate-hampshire), a Grok Imagine "
                "UUID/@tag, a grok.com/imagine URL, or a skill name. Catalog: "
                f"{PAGES_CATALOG}"
            ),
            "skills": _skills_for_intent(intent, skills),
        },
    }


def catalog_payload() -> dict[str, Any]:
    skills = load_skills()
    characters = load_characters()
    compact = []
    for c in characters:
        compact.append(
            {
                "slug": c["slug"],
                "name": c["name"],
                "regional_lock": c["regional_lock"],
                "aliases": c["aliases"],
                "frame_ids": c["frame_ids"],
                "uuids": c["uuids"],
                "imagine_tags": c["imagine_tags"],
                "bible_path": c["bible_path"],
                "github": c["github"],
                "core_look": c["core_look"],
            }
        )
    return {
        "version": CATALOG_VERSION,
        "owner": "Kearney-Evan-MI",
        "repository": "Kearney-Evan-MI/imagine-gallery",
        "catalog_url": PAGES_CATALOG,
        "how_to_use": (
            "Pass a UUID, @tag, grok.com/imagine URL, character slug/name, frame id, "
            "or skill to `python3 scripts/resolve_grok_input.py`. Return the JSON "
            "`grok_return` object to Grok unchanged."
        ),
        "resolver": "scripts/resolve_grok_input.py",
        "characters": compact,
        "skills": [
            {"name": s["name"], "path": s["path"], "session_copy": s["session_copy"]}
            for s in skills
        ],
        "toolkit_path": "integrations/grok-imagine-toolkit/",
    }


def write_catalog(path: Optional[Path] = None) -> Path:
    dest = path or (repo_root() / "docs" / "grok.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(catalog_payload(), indent=2) + "\n", encoding="utf-8")
    return dest


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("query", nargs="?", default="", help="UUID, @tag, URL, slug, name, frame id, or skill")
    parser.add_argument("--intent", default="restyle", choices=sorted(set(INTENT_SKILLS) | {"restyle"}))
    parser.add_argument("--list", action="store_true", help="Print the compact catalog JSON")
    parser.add_argument("--write-catalog", action="store_true", help="Write docs/grok.json")
    args = parser.parse_args(argv)

    if args.write_catalog:
        dest = write_catalog()
        print(json.dumps({"ok": True, "wrote": dest.relative_to(repo_root()).as_posix()}, indent=2))
        return 0
    if args.list or not args.query:
        print(json.dumps(catalog_payload(), indent=2))
        return 0

    result = resolve(args.query, intent=args.intent)
    print(json.dumps(result, indent=2))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
