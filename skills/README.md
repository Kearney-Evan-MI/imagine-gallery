# Grok Imagine skills

Session-active copies live in Grok under `/home/workdir/.grok/skills/`.
This folder is the GitHub canonical copy for the Imagine cluster.

## Cluster

| Skill | Use when |
|-------|----------|
| `imagine-restyle` | Edit or restyle an existing frame or prompt while locking phenotype, bone structure, and camera distance |
| `photoreal-phenotype-prompts` | Write a new photoreal prompt with a British / Dutch / French / North Italian lock |
| `pretty-women-photorealism` | Keep attractiveness photographic instead of filter/stock/plastic |
| `pg13-topless-photorealism` | New-generation PG-13 documentary topless still |
| `pg13-topless-restyle` | Same register as an identity-locked edit of an existing adult frame |

API execution, video, hyperframe, and cost logging stay in `integrations/grok-imagine-toolkit/`.
Character UUIDs and bibles stay in `characters/`.

## Sync back into a Grok session

Copy a skill directory into `/home/workdir/.grok/skills/<name>/` so the agent can load `SKILL.md`.

Do not put dating, PEP8, or other non-Imagine skills here unless they are deliberately part of this gallery.
