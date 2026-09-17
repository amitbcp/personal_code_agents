# Adaptations from the upstream baseline

Baseline: fcf3ff0 (2026-09-16). Original files are recoverable from that commit; provenance.json points to upstream revisions. This document identifies changes to imported material, including Apache-licensed files.

## Agents

The five VoltAgent definitions use the owner's Astra/low policy and explicit read-only versus implementation boundaries. Adaptations cover evidence-based code review, retrieval/multimodal evaluation, primary-source research, reliable pipelines and measured performance. Remove exceptions permitting omitted contrary evidence or unsupported claims. Agent invocation does not authorize deployments, publishing, resource changes or termination of another task.

## Skills

- **train-sentence-transformers:** replaced the entrypoint and broad training recipes with a focused workflow and two evaluation/CrossEncoder references. Removed default public Hub publishing, prescribed trackers/verdicts, fixed loss/activation/early-stopping recipes and cloud-job defaults. Preserve project model family/environment/trainer; check installed APIs, split hygiene, real candidate pools, paired uncertainty and checkpoint reload. Distinguish sigmoid monotonicity from finite-precision saturation.
- **hf-mem:** added limits of estimates, allocation/unified-memory interpretation, runtime overhead and credential handling. Tool versions must be recorded if installed; this skill does not launch jobs.
- **jupyter-notebook:** resolve the helper relative to the loaded skill instead of rewriting CODEX_HOME. Default output now derives from the working project, not the skill checkout. Preserve overwrite protection; test output location, notebook shape and overwrite behavior. Clarify compute/execution boundaries.
- **hypothesis-generation:** compact ML rival-test workflow with conditional domain-specific gates and existing authorization; retained local validators are optional aids, not scientific proof.
- **get-available-resources:** compact allocation-aware guidance; planning is advisory and never authorizes terminating healthy work. A memory-budget warning is not a safe-to-launch decision. Retained scripts remain unchanged.
- **ml-paper-writing:** narrow, model-neutral paper workflow with verified citations and current venue requirements. Retained three focused writing/citation/checklist references and a portable MIT license; removed dated conference templates and redundant reference catalogs. Acquire the official current template only for an actual venue task.

Whole upstream catalogs, installers, invented agent histories, cloud orchestration layers and duplicate artifact tools are not bundled as active components. The baseline retains removed material for provenance, not recommended execution.

## Expanded research workflow review

Add three original project procedures: literature-survey, paper-reading, and research-knowledge-map. These are not unchanged upstream imports; their conceptual sources are identified in the research workflow guide. No new runtime, watcher, index database or cloud dependency is introduced.

Add an ML ablation design reference to hypothesis-generation, covering matched budgets, component interactions, retraining versus inference removal, independent final evaluation, preserved run records and shared-server execution boundaries. Clarify author-side writing versus assigned confidential peer review in ml-paper-writing. Keep the existing five agent roles.
