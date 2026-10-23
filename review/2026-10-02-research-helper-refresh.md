# Research helper refresh — 2026-10-02

## Outcome

Keep the existing five specialist agents and nine general research skills. Refresh selected K-Dense helpers against revision `154988403bb5a18e9d3c0ce4e6d5e2e4b184a298`, preserving the locally adapted research workflow, authorization boundaries and storage guidance. No additional agent catalog or background service is needed for these fixes.

The original import mappings remain unchanged in `provenance.json`; its `maintenance_updates` section records the files refreshed here. This is a selective backport, not a claim that the whole installed skill mirrors the new upstream revision.

## Fixed behavior

- **Resource planning:** a valid 512 MiB available-memory snapshot with a 1 GiB per-worker estimate and no reserve previously recommended one worker despite its warning. It now recommends zero workers/threads with `insufficient_memory`. Unknown CPU capacity or memory produces `review_required`; positive counts remain provisional estimates. Planning does not launch or terminate work.
- **Resource inventory:** use visible cgroup mount roots and ancestor limits, current-node Slurm counts, current nested AMD memory records and separate filesystem free/user-available blocks. Do not add an unresolved GPU memory pool to RAM or claim it is dedicated VRAM. Hidden cgroup ancestors, quotas and accelerator runtime usability remain limitations.
- **Resource file handling:** reject unsafe/nonregular outputs and hard-linked forced targets before truncation. Validation also rejects missing required snapshot fields and extreme invalid numbers.
- **Hypothesis helpers:** reject nonstandard JSON constants, excessive nesting, floating-point overflow and noncalendar date forms. Generated scaffolds preserve the source record's date rather than presenting generation time as verification time. The float-overflow rejection is a local addition beyond upstream's constant guard.
- **Experiment guidance:** preserve a frozen, nonadaptive confirmation protocol. Predeclared comparisons and disclosed evaluator corrections do not automatically invalidate a holdout. Invalidate affected generation stages after behavior changes; evaluator-only corrections may regrade compatible immutable raw outputs with verified provenance, preserving the old scores.

## Compatibility

- Resource schema remains upstream `1.1`, but `recommendation.status` is added and worker counts can be zero. Consumers must inspect status and warnings before execution.
- AMD device `reported_total_bytes` carries the observed memory pool; `dedicated_total_bytes` can intentionally remain null.
- Strict snapshot validation may reject previously accepted incomplete records. These helpers have no runtime consumer in this library outside their own skill scripts; external callers should observe the documented contract.
- Skill names, invocation policy, model selection, specialist responsibilities, OKF conventions and the existing project-specific skill suite are unchanged.

## Validation

- Repository validator: five agent TOMLs, fourteen Python sources and eleven original import mappings valid.
- Full offline unit suite: **30 passing tests**, comprising twenty resource cases, seven hypothesis cases and three notebook cases.
- All nine skill entrypoints pass the installed Codex Skill Creator frontmatter validator.
- Two independent scoped reviews found no blocking defect; the resource API changes above are intentional and documented.
- No GPU job, model-backed benchmark, training run, paid evaluation or publishing operation was used. Fixture tests establish helper behavior, not an improvement in model research quality.

## Upstream review coverage

The selected paths from VoltAgent, Hugging Face, Orchestra Research and OpenAI were also compared with their current upstreams. None of those selected agent/skill paths required a refresh at this check. The broader Agency catalog changed, but no additional permanent role was justified by these research needs. Revisit statistical power or specialized experimental-design tooling for a concrete study rather than installing a whole catalog preemptively.

Relevant sources: [K-Dense revision](https://github.com/K-Dense-AI/scientific-agent-skills/commit/154988403bb5a18e9d3c0ce4e6d5e2e4b184a298), [original baseline](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792), and this repository's [provenance](../provenance.json).
