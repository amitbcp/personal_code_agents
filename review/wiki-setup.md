# OKF wiki update validation — 2026-09-16

Expanded research-knowledge-map in place; added format and project setup references. The collection stays at five agents and nine skills. This is an instruction-only implementation of the public Karpathy workflow using Google OKF v0.2. No upstream skill code/text or runtime was imported, and no profile or project wiki was deployed.

## Checks

- Skill Creator frontmatter validation passed.
- Repository validator passed: five agent definitions, fourteen retained Python files, eleven import mappings.
- README/skill local reference checks, example YAML parsing and example source-path resolution passed.
- Independent source review of the three skill files against canonical OKF v0.2 found no actionable conformance or upkeep-scope defects. Clarified the root index's sole optional version key.
- Independent execution on a small synthetic fixture updated the wiki note, index and log. Inputs: run A had 0.72 nDCG with oracle candidates, run B 0.65 with retrieved candidates on the same development queries, no final-test run, and a personal note about candidate recall. The agent correctly declined to infer ranker improvement, preserved that annotation verbatim, left the source unchanged and proposed rather than executed further evaluation. The resulting metadata parsed and local links resolved.

This is one maintenance smoke case, not an efficacy benchmark, full interoperability certification or NFS concurrency test. Live discovery checks and a real project pilot remain deployment work. An unauthenticated open-PR API check returned HTTP 403; no absence of overlapping PRs is claimed. The remote branch was fetched and matched the local base before committing.

Sources: [OKF specification](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md), [Karpathy idea](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [project instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
