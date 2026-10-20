---
name: grok-input
description: Resolve Imagine Gallery input (UUID, @tag, grok.com/imagine URL, character slug/name, frame id, or skill) into the JSON Grok needs. Use whenever Grok is asked to reuse a gallery character or post. Return grok_return unchanged.
---

# Grok input

Canonical copy: `skills/grok-input/` in Kearney-Evan-MI/imagine-gallery.
Session copy: `/home/workdir/.grok/skills/grok-input/`.

## What to return

Do not invent frame ids, UUIDs, or bibles. Run:

```bash
python3 scripts/resolve_grok_input.py "<input>"
```

Print the JSON. Hand `grok_return` back to Grok as the identity/skill payload.

| Input | Example |
|-------|---------|
| Character name or slug | `kate`, `characters/kate-hampshire` |
| Frame id | `LlvFU` |
| UUID or @tag | `@ff0116d1-7647-49a9-a4a1-7c05b5e80c7f` |
| Imagine post | `https://grok.com/imagine/post/ff0116d1-7647-49a9-a4a1-7c05b5e80c7f` |
| Skill URL | `https://grok.com/imagine?skill=imagine-restyle` |

Flags:

- `--intent restyle|generate|video|animate|api` — skill set in `grok_return.skills`
- `--list` — compact catalog
- `--write-catalog` — refresh `docs/grok.json`

Live catalog: https://kearney-evan-mi.github.io/imagine-gallery/grok.json

## After a match

1. Load the skills listed in `grok_return.skills` (copy `path` → `session_copy`).
2. Tag `imagine_tags` or re-upload refs before generating.
3. Follow `identity_instruction` and the character bible.
4. For API / video / hyperframe, use `integrations/grok-imagine-toolkit/`.
