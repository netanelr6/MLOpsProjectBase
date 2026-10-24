# MLOpsProjectBase — Agent-Driven MLOps Hub

A central Hub that manages distributed ML projects (Spokes) with reusable CI/CT, Docker, DVC and Weights & Biases automation, operated by LLM agents and documented in an Obsidian knowledge base.

- **Hub**: this repo — workflows, base images, scripts.
- **Spokes**: independent ML projects (`train.py`, `model.py`) calling the Hub.
- **Brain**: [docs/index.md](docs/index.md) — architecture, tools, tasks, run logs.

**Status:** Phase 1 (foundation). See [docs/03-Active-Tasks/roadmap.md](docs/03-Active-Tasks/roadmap.md).
Agent instructions: [CLAUDE.md](CLAUDE.md).
