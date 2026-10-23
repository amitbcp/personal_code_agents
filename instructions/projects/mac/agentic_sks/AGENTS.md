# Working in SKS

This repository uses AI Driven Engineering (AIDE) guidance.
Repository discovery: Before broad search, read the manifest below and open the smallest task-relevant routes first. If no route fits or a material question remains, expand the search narrowly.
AIDE repository manifest: .aplat/aide/repository.yaml
SKS (Oracle Shared Knowledge Store) ingests developer knowledge and serves
governed retrieval through REST and MCP. Source systems remain the authority
for their content; SKS is the retrieval layer. Ingestion runs as a batch
workload; serving handles online requests.

Security, availability, and performance are core requirements. Consider their
impact when changing a shared service contract or operational path.

## Find the relevant context

Start with the affected component below, its tests, and any applicable
`openspec/specs/` baseline or selected `openspec/changes/` change. Read nearby
instructions before editing. Search within that area before widening the search.

| Change area | Start here |
| --- | --- |
| Deployment profiles, route visibility, OpenAPI | `sks/api/capabilities.py`, `sks/api/main.py`, `tests/test_route_capability_registry.py` |
| Classic REST and retrieval | `sks/api/routes/`, `sks/api/mcp_knowledge.py`, `sks/retrieval/`, `sks/models/search.py`, `tests/test_api_main.py` |
| Support REST, MCP, retrieval, generation | `sks/support/serving/`, `tests/test_support_api_contracts.py`, `tests/test_support_generation.py` |
| Classic ingestion and connectors | `sks/ingestion/`, `sks/connectors/`, `tests/test_ingestion/` |
| Support ingestion and shared data contracts | `sks/support/ingestion/`, `sks/support/contracts/`, `tests/test_support_ingestion_boundary.py` |
| Configuration and backends | `config/README.md`, `config/REFERENCE.md`, `sks/index/`, `sks/graph/` |
| Gateway | [Gateway build and configuration](sks-gateway/README.md), `sks-gateway/pom.xml` |
| Packaging and deployment | `Dockerfile.api`, `Dockerfile.support.ingestion`, `Dockerfile.gateway`, `helm/sks/`, `ocibuild.conf` |
| Validation | [Test selection and prerequisites](docs/guides/test-suite.md), `tox.ini`, `pyproject.toml` |
| Packaged local REST/MCP checks | [Support and Classic local testing](docs/aipioneering/support/local-testing.md) |

Python code targets 3.11+ and uses FastAPI, Pydantic, and FastMCP. Backend and
model choices come from configuration; inspect the affected profile rather
than assuming every deployment uses the same services. The Java gateway has
its own build requirements in its README.

## Preserve the shared contracts

- Classic and Support are separate trusted deployment profiles. Requests must
  not select a profile, backend credentials, cluster, or unrestricted index
  catalog. Use `sks/api/capabilities.py` for route enforcement and
  profile-specific OpenAPI visibility. Preserve wrong-profile rejection before
  downstream work and the bounded `unsupported_capability` error.
- Keep Support serving, ingestion, and shared contracts within their package
  boundaries. Use the dependency checks in `tests/test_support_architecture.py`;
  do not couple Support serving to Classic routes or ingestion internals.
- Corresponding REST and MCP operations share contracts and public response
  projection. Check actual serialization, optional-field omission, errors,
  and discovery schemas when changing either interface. FastAPI/Pydantic
  generate OpenAPI; do not introduce a hand-maintained OpenAPI YAML copy.
- Preserve existing Classic `/knowledge/search` consumers unless a reviewed
  change explicitly changes that contract. For public field changes, inspect
  callers and sibling operations before deciding compatibility behavior.
- Keep request bounds, profile isolation, and sanitized errors covered by
  negative tests. Raw provider responses and deployment credentials must not leak
  into public payloads or logs.

Baseline specs in `openspec/specs/` record accepted behavior for covered
capabilities; active changes describe intended differences. Compare both with
current code and approved requirements.
Record conflicts and consequential decisions instead of treating old design
documents or current implementation as automatic product approval.

## Shared workflow and change scope

Use the team's AIDE workflow and its supported OpenSpec integration once the
repository setup is initialized. Keep generic proposal and implementation
procedures in the upstream skills; keep SKS rules here and in
`openspec/config.yaml`. Personal skills and private notes are not prerequisites
for working in this repository.

1. Inspect applicable instructions, code, configuration, tests, and worktree
   state. Preserve unrelated edits and resume the selected change rather than
   starting a competing one.
2. Keep the change within the requested outcome. Resolve consequential public
   behavior or compatibility decisions before implementing dependent work.
   Routine implementation choices do not need a new approval step.
3. For an OpenSpec change, follow the selected change's requirements and task
   list. Link requirements to meaningful tests or other verification evidence.
   Leave unexecuted tasks unchecked, and preserve baseline specs and archived
   history until the workflow calls for synchronization or archive.
4. Keep generated helpers owned by their generator. Change durable SKS guidance
   in shared instructions/configuration instead of patching generated skills or
   copying personal workflow skills into the repository.
5. Use existing patterns and dependencies. Use `apply_patch` for source and
   documentation edits. Update affected examples and consumers with a contract
   change; avoid unrelated cleanup.
6. Run the narrowest relevant checks, then the applicable regressions in the
   [test guide](docs/guides/test-suite.md). Artifact validation and passing
   unit tests do not prove packaged or live behavior.

## Coding and validation

- Prefer the Python standard library when it meets the need. Follow PEP 8,
  local naming patterns, and the existing Pydantic/dataclass model choice.
- Use type hints where practical, descriptive names, and f-strings. Document
  public functions and non-obvious side effects; comments should explain a
  reason or invariant rather than restate the code.
- Use pytest function-style tests, descriptive names, fixtures, and direct
  assertions. Add meaningful regression tests for behavior changes; avoid tests
  that merely assert documentation wording or mirror implementation details.
- Test the affected boundary: HTTP routing/serialization, MCP dispatch and
  schemas, or exact provider requests when those contracts change. Use
  controlled dependencies for unit tests rather than requiring live services.
- Record failed checks, meaningful skips, and environmental limitations. Do not
  broaden the change to fix unrelated failures or present skipped integration
  checks as successful integration evidence.

## Security and operational safety

- Never commit, print, or hardcode credentials, tokens, OCI wallets, private
  keys, kubeconfig contents, or `.env` values. Redact sensitive identifiers and
  values from examples, logs, fixtures, and handoffs.
- Do not run `kubectl apply`, `kubectl delete`, Helm upgrades, OCI
  create/update/delete operations, or production deployment commands unless
  the user explicitly requests that action. Confirm the intended target before
  running an authorized operational procedure.
- Treat `k8s/`, Helm values, and deployment scripts as potentially
  production-affecting. Inspect them and explain the operational effect of a
  change. Do not modify generated artifacts, snapshots, or externally managed
  source data unless the request explicitly requires it.
- Implementation is separate from deployment, merge, external document
  publication, and messages. Follow the authorization for each action.

## Handoff

Report the outcome, changed files, checks and results, and any unrun checks or
remaining compatibility, operational, or release work. Distinguish local edits,
commits, pushed branches, PRs, and deployed behavior. Keep task completion and
verification evidence consistent with what actually ran.
