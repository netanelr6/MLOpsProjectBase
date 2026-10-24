---
type: task
status: active
updated: 2026-10-24
tags: [roadmap, state]
---

# Roadmap

| Phase | Scope | Status |
|---|---|---|
| 1 | Foundation: `.claude/` structure, vault, CLAUDE.md, README | 🟡 in progress |
| 2 | Core engine: generic Dockerfile, reusable CI/CT workflows, DVC + W&B wrappers | ⬜ not started |
| 3 | Agent tooling: log parser, spoke trigger, vault read/write scripts | ⬜ not started |
| 4 | Spoke PoC: dummy Spoke, end-to-end run documented in vault | ⬜ not started |

## Phase 1 checklist
- [x] `.claude/agents`, `skills`, `commands` folders
- [x] Obsidian skills installed, Stop hook mirroring to `project_mind`
- [x] `docs/` vault skeleton, conventions, templates
- [x] `CLAUDE.md`, `README.md`
- [x] Git repo initialised, `origin` set (no push yet)
- [ ] User supplies skills / agents / commands / connections (incremental)
- [ ] Create `src/`, `scripts/`, `.github/workflows/` when the user approves

Back to [[_index]].
