---
type: architecture
status: draft
updated: 2026-10-24
tags: [architecture, hub-and-spoke]
---

# Architecture (proposal — to be refined with the user step by step)

## Hub & Spoke
- **Hub**: reusable GitHub Actions (CI/CT), generic Dockerfile, DVC + W&B wrappers, agent tools.
- **Spokes**: business logic only (`train.py`, `model.py`); call Hub workflows via `workflow_call`.
- **Brain**: this `docs/` vault.

## Proposed repository tree
Legend: ✅ exists now · ⏳ planned (created only when its phase starts).
```
MLOpsProjectBase/
├── CLAUDE.md                 ✅ agent operating manual
├── README.md                 ✅
├── .claude/                  ✅ agents/ skills/ commands/ hooks/ settings.json
├── docs/                     ✅ the Brain (below)
├── project_mind/             ✅ user's personal Obsidian vault (mirrors project)
├── .github/workflows/        ⏳ P2  ci.yml, ct.yml (reusable, workflow_call)
├── docker/                   ⏳ P2  Dockerfile.base (generic, installs Spoke deps)
├── src/hub/                  ⏳ P2  dvc_wrapper.py, wandb_wrapper.py
├── scripts/                  ⏳ P3  agent CLI skills (parse logs, trigger spokes, vault r/w)
├── spokes/                   ⏳ P4  dummy Spoke PoC (or separate repo)
└── tests/                    ⏳
```

## The vault (`docs/`) — optimized for agent memory + human reading
```
docs/
├── index.md                  entry point / map
├── 00-Meta/                  conventions, templates
├── 01-Architecture/          this note, decisions/ (ADRs), API & schema specs
├── 02-Agent-Tools/           one note per tool: purpose, CLI usage, I/O JSON schema, failure modes
├── 03-Active-Tasks/          roadmap.md (phase status), current-task notes
├── 04-Spokes/                one note per Spoke (repo, entrypoints, last runs)
├── 05-Run-Logs/              one note per pipeline run, incl. failure analysis
└── 99-Archive/               superseded notes
```
Design principles:
1. **Numbered folders** give a stable reading order; the agent starts at `index.md` → `roadmap.md`.
2. **Frontmatter** (`type`, `status`, `updated`) lets agents query state without reading bodies.
3. **One note per tool/spoke/run** keeps notes small and linkable.
4. **State lives in `03-Active-Tasks/roadmap.md`**; run history in `05-Run-Logs/`.
5. **Docs precede code** (ADR → implementation).

## Open questions for the user
- Spokes: subfolder `spokes/` in the Hub or separate GitHub repos?
- Registry for Docker images (GHCR?) and DVC remote storage (S3/GDrive/local)?
- Which skills/agents/commands will be added to `.claude/`?

Back to [[_index]].
