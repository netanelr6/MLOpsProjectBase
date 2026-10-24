---
type: convention
status: active
updated: 2026-10-24
tags: [meta, conventions]
---

# Vault Conventions

## Frontmatter (required)
```yaml
---
type: index | architecture | adr | tool | task | spoke | run-log | convention
status: draft | active | done | superseded
updated: YYYY-MM-DD
tags: []
---
```
Agents filter on `type` and `status` to find current state quickly.

## Rules
- File names: `kebab-case.md`; ADRs `NNNN-title.md`; run logs `YYYY-MM-DD-spoke-short-name.md`.
- Link with `[[wikilinks]]`; every folder has an `_index.md` listing its notes.
- One topic per note; keep notes short. Put machine-readable data (JSON/YAML schemas) in fenced blocks.
- Never delete notes; set `status: superseded` and move to `99-Archive/`.
- Update `updated` whenever a note changes.
- Document first: design notes precede code.

Back to [[index]].
