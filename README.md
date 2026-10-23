# Personal Code Agents

A small, traceable Codex library for retrieval, model evaluation, multimodal research, data pipelines and scientific writing: **five agents and seventeen skills**.

## What to use

| Component | Job |
|---|---|
| reviewer | Correctness/regression review, reproductions and scoped fixes |
| scientific-literature-researcher | Primary-source research and durable literature artifacts |
| eval-engineer | Design, implement, run and interpret research evaluations |
| data-engineer | Scoped ingestion/transformation work, replay behavior and data contracts |
| performance-engineer | Profile, optimize and verify performance and resource use |
| literature-survey | Bounded search, screening records and cross-paper evidence synthesis |
| paper-reading | Paper mechanisms, derivations and personal comprehension exercises |
| research-knowledge-map | OKF project wiki, research knowledge and scoped task-end upkeep |
| hypothesis-generation | Rival explanations and discriminating experiments |
| get-available-resources | Read-only process/allocation resource inventory and advisory planning |
| train-sentence-transformers | Retrieval/reranker training contracts and leakage-aware evaluation |
| hf-mem | Model-weight and optional KV-cache memory estimates |
| ml-paper-writing | Evidence-linked manuscripts, verified citations and venue-aware preparation |
| jupyter-notebook | Reproducible notebook scaffolds that write into the working project |

All five custom agents use `sandbox_mode = "workspace-write"`. Agents define responsibilities and task scope; they can write artifacts, implement assigned changes and run relevant checks without routine confirmation. They preserve an explicit planning-only or review-only request. Actual writes remain subject to the active host/profile permissions.

Agents define responsibilities and execution boundaries. Skills supply procedures. Keep existing project guidance, CBM exploration agents and ordinary Codex workers; there is no requirement to invoke every component for every task.

See the [research workflow guide](review/research-workflow.md) for literature → experiments → paper preparation and the expanded company/author review. The three added research-note skills are original procedures; the earlier imported baseline remains unchanged in history.


## Engineering, figures and UI additions (2026-10-05)

- `codebase-design`: module boundaries and caller complexity.
- `improve-codebase-architecture`: scoped architecture survey and optional system-design checklist.
- `diagnosing-bugs`: reproduction, hypothesis testing and original-scenario verification.
- `property-based-testing`: invariant and generated-input testing.
- `scientific-visualization`: scientific plots, export helpers and figure QA.
- `archify`: typed architecture/dataflow diagrams with standalone rendering; Node >=18.
- `frontend-design`: intentional UI design that preserves existing product conventions.
- `web-performance`: measured web responsiveness and loading analysis.

The manuscript and OKF skills gain scoped evidence-review and domain-vocabulary references; the reviewer gains separate requirements/standards checks and behavior-facing test guidance. See [compatibility](review/2026-10-05-compatibility.md) and the engineering, research and visual import reports beside it. Original source snapshots retain `SKILL.md.txt` filenames to prevent accidental discovery. Install selected `skills/`, `agents/` and referenced `guidance/` into their appropriate discovery locations; do not install review snapshots as runtime components.

## Autonomous work and server storage

Use existing task authorization and let agents resolve routine details; ask only when a real blocker or missing consequential authorization prevents progress. Coordinate ownership when multiple agents edit the same project. Instructions use headings and bullets for maintainability.

Vulcan NFS is shared across nodes; NVMe is node-local. Keep durable project source, knowledge notes and final results on shared storage. Use a verified suitable local NVMe path for staging, scratch work and caches, then preserve required outputs before allocation/node loss. Check mount permissions, available space and actual allocations. Existing CBM/runtime locations are not relocated by this library.

See [current design and upstream differences](review/current-design.md) for the permission, automation and formatting changes and the exact scope retained or removed.

## Prepare another laptop

Follow [docs/team-laptop-setup.md](docs/team-laptop-setup.md) for the correct branch, seventeen skills, five specialist agents, three [guidance files](guidance/README.md), adapted global/project instructions, helper dependencies, [optional CBM integration](integrations/codebase-memory/README.md), plugin installation and target-machine verification. The knowledge-map skill includes its full OKF and project-setup references. [Plugin inventory](docs/plugin-inventory.json) records public bundled/runtime IDs explicitly enabled in the source config; it does not bundle their runtimes or transfer account access.

## Project instructions and deployment alignment

- Start a new project guide from [templates/project-AGENTS.example.md](templates/project-AGENTS.example.md), then merge only relevant sections into the existing project-root `AGENTS.md`.
- Follow [instruction layers](docs/instruction-layers.md) for global/project/skill responsibilities, model routing, local versus shared storage, and separate Git/CBM documentation policies.
- [Actual instruction snapshots](instructions/README.md) preserve owner-authorized global, workspace and project AGENTS files with source metadata for history and team review. The portable example remains separate; snapshots require environment-specific review before reuse.
- [2026-10-23 alignment review](review/2026-10-23-deployment-alignment.md) records what matches the Mac and both node-local profiles, what is separately managed, and what the checks do not prove.

## OKF project wiki setup

The existing `research-knowledge-map` skill now supports Google OKF v0.2 project wikis. Follow its [setup guide](skills/research-knowledge-map/references/project-setup.md) to install the shared skill in the appropriate profiles, merge the project maintenance rule, and initialize a bounded source set. [Format conventions](skills/research-knowledge-map/references/okf-conventions.md) distinguish the OKF standard from our research conventions.

Routine upkeep happens during active tasks under project instructions; bulk ingestion stays explicitly scoped. No hook, background writer, database or Google service is required. This repository update does not install the skill or create wikis on the Mac or servers.

## Provenance and changes

The first commit, [fcf3ff0](https://github.com/amitbcp/personal_code_agents/commit/fcf3ff0), preserves 136 imported files unchanged. It is an **upstream baseline, not the version to install**. The adaptation commit makes changes visible in Git.

- [provenance.json](provenance.json): exact upstream revisions, original paths and licenses for every import.
- [CHANGES.md](CHANGES.md): adaptations and removed material.
- [2026-10-02 refresh](review/2026-10-02-research-helper-refresh.md): targeted upstream helper fixes, compatibility changes and offline validation.
- [review/README.md](review/README.md): coverage, decisions, exclusions and limitations.
- `licenses/`: original license texts; package-specific notices remain in place.

No Astra-specific performance advantage is claimed. Agent settings follow the owner's Astra/low starting policy; measure on representative tasks before changing models or reasoning. The catalogs supply procedures, not trained specialist models.

## Use and deployment

Cloning this repository does not install anything. To try a skill, point Codex at its `skills/<name>/SKILL.md`. To use a custom agent, install its TOML into a supported discovery directory and start a fresh task.

For persistent installation, select only wanted components, check for an existing same-named component, then copy or symlink it. Do not overwrite existing definitions or merge entire config files blindly. Typical native locations:

- Personal agents: `~/.codex/agents/`; project agents: `.codex/agents/`.
- Personal skills: `~/.agents/skills/`; project skills: `.agents/skills/`.

Custom CODEX_HOME wrappers and older clients can expose different paths. Confirm discovery from the actual execution host/profile before rollout. Existing installations using `~/.codex/skills` should not acquire duplicate copies under another scanned directory.

Mac and SSH environments need separate discovery setup. Reviewed instruction files can be shared on NFS independently of conversation history. Keep executables, Python environments, runtime caches and live index databases in the appropriate host-local location. Owner-authorized AGENTS snapshots under `instructions/` may contain their original host/project paths. Credentials, runtime databases and conversations remain outside this repository; referenced private companions are not included automatically.

Skills do not install dependencies or run jobs merely because they are present. Use the target project's environment and current official documentation. External publishing/paid compute requires authorization for that action and destination; training, reviewing or writing does not imply publishing.

Official references: [custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [skills and discovery](https://learn.chatgpt.com/docs/build-skills).

## Final predeployment review

The [predeployment audit snapshot](review/final-predeployment.md) documents the earlier review and fixes. The [current design](review/current-design.md) supersedes its permissions, formatting and size table. This collection includes substantial rewrites as well as light adaptations; it is not an unchanged upstream mirror.

## Maintain and validate

Fetch upstream changes into a separate checkout, compare selected paths against the recorded revision, and update deliberately. Keep provenance/license changes and adaptations reviewable. Do not auto-sync upstream instructions into active profiles.

Local checks using Python 3.11+:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Use Codex's Skill Creator validator for frontmatter too. Syntax/fixture checks do not prove better model behavior; the review report records what was tested. No GPU training, paid evaluation or deployment is part of these checks.

Imported material retains its respective upstream license. This is not a blanket relicense of the catalogs or their nested assets.
