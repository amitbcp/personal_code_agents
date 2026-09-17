---
name: hypothesis-generation
description: Formulate evidence-bounded scientific questions, candidate hypotheses, rival explanations, causal or associational claims, discriminating predictions, measurements, and preregistration-ready analysis plans. Use when turning observations or preliminary findings into transparent, testable research plans without treating hypotheses as facts.
license: MIT
metadata:
  version: "2.2"
  skill-author: K-Dense Inc.
  last-reviewed: "2026-07-23"
---

# Hypothesis Generation for Research Experiments

Use this for turning an observation into discriminating experiments, especially when several explanations fit the same benchmark result. Follow project research guidance; this skill adds a rival-prediction record, not a second approval process.


**Runtime:** Python 3.11+ standard library. Bundled CLIs are deterministic and local-only; they accept bounded JSON, CSV, or Markdown and require no network, credentials, models, image services, or external packages.

## Compact workflow

1. **Freeze the observation.** Record data/model/prompt versions, metric, unit of analysis, uncertainty, and whether the pattern was discovered after looking at results. Separate measured facts from proposed explanations.
2. **State the question and claim.** Distinguish predictive improvement from causal or mechanistic claims. For retrieval, specify corpus/query population, candidate generator, reranker, comparator, quality metric and latency/cost constraints.
3. **Generate plausible rivals.** Include a substantive mechanism, leakage or contamination, changed preprocessing/candidate coverage, measurement or judge bias, and seed/query variation where relevant. Do not force a fixed number. Rank proposed tests by information gained and cost when useful; a priority is not proof that a hypothesis is true.
4. **Choose a discriminating test.** For each candidate, specify predicted result, rival prediction, result that would challenge it, assumptions, controls and indeterminate outcomes. For example: a reranker’s gain might reflect more candidates rather than better ordering; hold candidate lists fixed and compare paired query outcomes.
5. **Freeze the analysis before target outcomes.** Choose experimental unit, paired comparisons where appropriate, seeds/resampling, effect size and uncertainty, multiplicity, exclusions and stopping rule. Use train/dev data for iteration and validation for selection; touch the held-out final test only once at the end. Account for grouped queries/users/documents instead of assuming every row is independent.
6. **Record the decision.** Preserve baselines, ablations, null/negative results and deviations. Label post-result hypotheses exploratory. A small gain inside uncertainty is inconclusive. Computational reproducibility and independent replication are separate goals.

Default deliverable: a short Markdown table with **candidate | rival | predicted contrast | falsifier | control | analysis | next action**, followed by evidence gaps and the cheapest informative experiment. Do not require a full JSON registry for a small ML experiment.

## Evidence and authorization

Verify sources when making literature-dependent claims; record query/date/source boundaries for novelty claims. “Not found in this search” does not mean no prior work exists. Never invent results, citations, approvals or preregistration. A proposed mechanism or predictive gain does not establish causality.

Use authorization already supplied in the task and project. Do not re-request permission for routine authorized ML planning, local analysis or public-data experiments. Apply human-subject, animal, biosafety, dual-use, privacy and regulatory gates only when the actual work implicates them. Preserve confidentiality: do not send private or unpublished material to a new external destination without authorization covering that destination and data. Escalate concrete unresolved approval requirements; do not manufacture blanket review gates. Human scientific accountability remains important, but source verification and ordinary analysis can proceed within the agent’s authorization.

## Optional structured tools

All helpers use Python 3.11+ standard library, operate locally and inspect bounded files. Run only the tool whose output helps the current deliverable. Resolve script paths relative to this skill. No network service or model key is required.

| Need | Command |
|---|---|
| Check declared measurements | `python3 scripts/check_operationalization.py measurements.json` |
| Check rival prediction matrix | `python3 scripts/validate_prediction_matrix.py matrix.csv` |
| Audit evidence ledger and search boundary | `python3 scripts/audit_evidence_ledger.py ledger.csv boundary.json` |
| Validate formal hypothesis record | `python3 scripts/validate_hypothesis_schema.py record.json` |
| Check formal falsification/control links | `python3 scripts/check_falsification_controls.py controls.json --record record.json` |
| Draft local preregistration scaffold | `python3 scripts/generate_preregistration_scaffold.py record.json -o preregistration.md` |
| Optional annotated causal-language lint | `python3 scripts/lint_causal_claims.py draft.md` |

Use matching templates in `assets/` and consult [tool reference](references/tool_reference.md) for exact schemas. The formal schema retains domain gate fields: record `not_applicable` when appropriate, without claiming an approval occurred. Some helpers require negative controls or human-review declarations; use them only when that schema fits. They validate declarations and cross-links, not scientific truth or authorization. Do not fill fields with fabricated evidence merely to make a validator pass. The scaffold refuses unresolved formal gates and does not submit a registration. The lexical causal lint can flag ordinary ML words such as “improves”; treat it as optional advice, never a mandatory writing gate.

Exit codes: 0 means the requested structural check completed validly, 1 means validation errors, and 2 means malformed/unsafe input. Read warnings and status as well as exit code. Preserve bounded input, symlink and private-output protections; use `--force` only for an intended replacement.

## Deeper references

For ML ablation campaigns, matched budgets, interaction effects and experiment retention, read [ML ablation design](references/ml-ablation-design.md).

Load only when useful: [causal claims](references/causal_inference_and_claims.md), [design patterns](references/experimental_design_patterns.md), [literature boundaries](references/literature_search_strategies.md), and [preregistration](references/preregistration_and_open_science.md). Domain examples and oversight advice in references are conditional on the actual study; they do not override this entrypoint, project guidance, or existing user authorization. Source-ledger dates are provenance, not a guarantee of current policy.

## Provenance

Adapted from K-Dense Scientific Agent Skills, revision `330c8e764435a731eff571e3efdda70b363d0792`, under MIT. Preserve license notices. Citation of the skill library in a manuscript is optional and should follow the user’s editorial needs.
