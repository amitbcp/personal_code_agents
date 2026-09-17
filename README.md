# Personal Code Agents

A small, traceable Codex library for retrieval, model evaluation, multimodal research, data pipelines and scientific writing: **five agents and nine skills**.

## What to use

| Component | Job |
|---|---|
| reviewer | Independent correctness/regression review with concrete evidence |
| scientific-literature-researcher | Primary-source research, contradictions and search boundaries |
| eval-engineer | Retrieval, agent and multimodal evaluation design and interpretation |
| data-engineer | Scoped ingestion/transformation work, replay behavior and data contracts |
| performance-engineer | Measured bottlenecks, resource/concurrency diagnosis and comparisons |
| literature-survey | Bounded search, screening records and cross-paper evidence synthesis |
| paper-reading | Paper mechanisms, derivations and personal comprehension exercises |
| research-knowledge-map | Deliberately maintained, source-linked research notes |
| hypothesis-generation | Rival explanations and discriminating experiments |
| get-available-resources | Read-only process/allocation resource inventory and advisory planning |
| train-sentence-transformers | Retrieval/reranker training contracts and leakage-aware evaluation |
| hf-mem | Model-weight and optional KV-cache memory estimates |
| ml-paper-writing | Evidence-linked manuscripts, verified citations and venue-aware preparation |
| jupyter-notebook | Reproducible notebook scaffolds that write into the working project |

Agents define responsibilities and execution boundaries. Skills supply procedures. Keep existing project guidance, CBM exploration agents and ordinary Codex workers; there is no requirement to invoke every component for every task.

See the [research workflow guide](review/research-workflow.md) for literature → experiments → paper preparation and the expanded company/author review. The three added research-note skills are original procedures; the earlier imported baseline remains unchanged in history.

## Provenance and changes

The first commit, [fcf3ff0](https://github.com/amitbcp/personal_code_agents/commit/fcf3ff0), preserves 136 imported files unchanged. It is an **upstream baseline, not the version to install**. The adaptation commit makes changes visible in Git.

- [provenance.json](provenance.json): exact upstream revisions, original paths and licenses for every import.
- [CHANGES.md](CHANGES.md): adaptations and removed material.
- [review/README.md](review/README.md): coverage, decisions, exclusions and limitations.
- `licenses/`: original license texts; package-specific notices remain in place.

No Astra-specific performance advantage is claimed. Agent settings follow the owner's Astra/low starting policy; measure on representative tasks before changing models or reasoning. The catalogs supply procedures, not trained specialist models.

## Use and deployment

Cloning this repository does not install anything. To try a skill, point Codex at its `skills/<name>/SKILL.md`. To use a custom agent, install its TOML into a supported discovery directory and start a fresh task.

For persistent installation, select only wanted components, check for an existing same-named component, then copy or symlink it. Do not overwrite existing definitions or merge entire config files blindly. Typical native locations:

- Personal agents: `~/.codex/agents/`; project agents: `.codex/agents/`.
- Personal skills: `~/.agents/skills/`; project skills: `.agents/skills/`.

Custom CODEX_HOME wrappers and older clients can expose different paths. Confirm discovery from the actual execution host/profile before rollout. Existing installations using `~/.codex/skills` should not acquire duplicate copies under another scanned directory.

Mac and SSH environments need separate discovery setup. Reviewed instruction files can be shared on NFS independently of conversation history. Keep executables, Python environments, runtime caches and live index databases in the appropriate host-local location. No credentials, global AGENTS.md, machine-specific paths or conversations belong in this repository.

Skills do not install dependencies or run jobs merely because they are present. Use the target project's environment and current official documentation. External publishing/paid compute requires authorization for that action and destination; training, reviewing or writing does not imply publishing.

Official references: [custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [skills and discovery](https://learn.chatgpt.com/docs/build-skills).

## Maintain and validate

Fetch upstream changes into a separate checkout, compare selected paths against the recorded revision, and update deliberately. Keep provenance/license changes and adaptations reviewable. Do not auto-sync upstream instructions into active profiles.

Local checks using Python 3.11+:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Use Codex's Skill Creator validator for frontmatter too. Syntax/fixture checks do not prove better model behavior; the review report records what was tested. No GPU training, paid evaluation or deployment is part of these checks.

Imported material retains its respective upstream license. This is not a blanket relicense of the catalogs or their nested assets.
