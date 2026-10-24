---
type: index
status: active
updated: 2026-10-24
tags: [index, hub]
---

# MLOps Hub — Brain Index

Entry point for humans and agents. Start with [[roadmap]].

## Hub & Spoke concept
- **Hub** (`MLOpsProjectBase`): reusable CI/CT workflows, base Docker images, DVC + W&B wrappers, agent tools.
- **Spokes**: independent ML projects holding only business logic (`train.py`, `model.py`); they call Hub automations.
- **Brain** (`docs/`): architecture, tool docs, task state, run logs.

## Map
| Folder | Purpose |
|---|---|
| [[00-Meta/_index\|00-Meta]] | Conventions, note templates |
| [[01-Architecture/_index\|01-Architecture]] | Architecture, ADRs, API/schema specs |
| [[02-Agent-Tools/_index\|02-Agent-Tools]] | Catalog of scripts/skills an agent can call |
| [[03-Active-Tasks/_index\|03-Active-Tasks]] | Roadmap, current work, state |
| [[04-Spokes/_index\|04-Spokes]] | One note per connected Spoke |
| [[05-Run-Logs/_index\|05-Run-Logs]] | Pipeline run records and failure analyses |
| 99-Archive | Superseded notes |

## Key notes
- [[architecture]] — proposed structure and design
- [[conventions]] — how to write notes
- [[roadmap]] — phases and status
