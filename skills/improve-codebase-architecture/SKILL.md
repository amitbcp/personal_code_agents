---
name: improve-codebase-architecture
description: Find and rank concrete architecture friction, then carry authorized refactors through implementation and verification. Use for architecture audits or scoped improvements to module boundaries, caller complexity and testability.
---

# Improve Codebase Architecture

## Establish scope and evidence

- Distinguish an audit from an implementation request. Finish an audit with ranked findings; an audit alone does not authorize refactoring.
- Read existing canonical architecture docs, glossary, task context and relevant ADRs. Preserve established vocabulary and knowledge locations.
- Read [codebase-design](../codebase-design/SKILL.md) for interface obligations, depth, deletion tests and testable seams.
- Start with the user’s named pain point. Otherwise inspect recent change history for recurring hotspots; widen only if history gives no useful focus.
- Use codebase-memory when available for structural evidence, with coverage/freshness checks and caller/callee context. Confirm consequential conclusions in current source; use source search when the graph is unavailable or incomplete. Fan-out alone is not an architecture defect.
- Delegate bounded independent exploration when authorized and useful. Give each explorer concrete paths, evidence questions and ownership; avoid duplicate whole-repository scans.

- For service/data-boundary changes or substantial system design, use the optional [system design checklist](references/system-design.md).

## Discover candidates

- Look for concepts that require repeatedly moving among small modules, large caller obligations, leaked ordering/configuration/error constraints, and tightly coupled changes across seams.
- Check whether extracted pure functions conceal the real integration failure: tests of individual pieces may miss their call sequence or shared state.
- Identify untested behavior and seams that prevent realistic failure tests; do not merge modules merely because they are small.
- Apply the deletion test: if deleting a wrapper removes complexity, it may be unnecessary; if it distributes useful hidden behavior among callers, it earns its keep.
- Classify dependencies with [deepening guidance](../codebase-design/DEEPENING.md); account for ownership, lifecycle and production semantics.

## Rank and decide

- For each supported candidate record concrete files, observed friction, proposed change, caller/test impact, risks and confidence: strong, worth exploring, or speculative.
- Ground benefits in locality and reduced caller obligations, not line counts. Explain what a test will be able to exercise after the change.
- Mark ADR conflicts explicitly with evidence that warrants reopening the decision. Do not silently overturn a standing decision.
- Recommend the strongest candidate within the authorized scope. Use [alternative designs](../codebase-design/DESIGN-IT-TWICE.md) for consequential uncertainty, not routine changes.
- Use a small before/after diagram when it clarifies relationships. A concise Markdown report is sufficient; HTML/CDN dependencies and temporary-only artifacts are not required.
- Ask only for a genuinely blocking correctness, scope or authorization decision. Do not force a candidate-selection interview when implementation is already authorized and the supported choice is clear.

## Complete authorized implementation

- Implement the selected scoped change, preserving observable behavior unless a change is explicitly intended.
- Map and preserve meaningful tests, add realistic failure coverage at the proper seam, and run focused checks plus project-required integration gates.
- Update existing canonical docs/ADRs for accepted durable changes; do not create a competing glossary or knowledge tree automatically.
- Preserve useful investigation scripts and evidence in project locations. Report implemented changes, commands actually run, outcomes and remaining uncertainty.

See [attribution](ATTRIBUTION.md) for upstream source and license.
