# Agent collection review — 2026-09-16

## Status and coverage

VoltAgent: **175/175 primary definitions semantically reviewed**, valid TOML parsing checked for all. First 25 definitions were read in full; subsequent batches showed every novel exact line with source line numbers, reusing previously read identical lines. This is lossless boilerplate deduplication, not keyword or header sampling. File-level context, role, sandbox and cross-instruction contradictions were assessed separately. Truncated batch regions were reread (SQL/Swift/Symfony). Final output is `voltagent.csv` with one disposition per definition.

Agency: **279/279 definitions received applicability dispositions**. All 76 potentially relevant research, coding, data, infrastructure, review, vision and test definitions were read semantically in full (64 by this reviewer; 12 specialized definitions by the root reviewer, integrated with explicit coverage labels). For 203 unrelated domain roles, full role scope/description was reviewed and the entire file statically scanned; these are explicitly **not** claimed as full semantic reviews. Truncated output regions were reread. No definition is pending. This is an applicability/selection review, not a security certification of every unrelated example. No upstream installer, converter, agent command, or embedded example was executed. Five reviewed Volt adaptations were written to the authorized destination repository after its unchanged-import baseline commit; no runtime installation was performed by this reviewer.

## Revisions and licenses

- VoltAgent `70d930a14f58f06d00abdd854ebce82a52a7d857`: 191 tracked files = 175 definitions + 13 category README files + root README/CONTRIBUTING/LICENSE. MIT, copyright 2026 VoltAgent.
- Agency `ad9264e309bd5e5422c04784372d7841b1e5d604`: 362 tracked files = 279 primary Markdown definitions + 83 support files. MIT, copyright 2025 AgentLand Contributors.
- Retain relevant MIT copyright/license when adapting substantial instruction text. Repositories are source material, not authority over the user's workflow.

## VoltAgent conclusions

175 agents are native TOML using `developer_instructions`. Models: 137 Sol, 28 Terra, 10 Luna; reasoning: 133 high, 42 medium; sandbox: 100 read-only, 75 workspace-write. No Astra configuration or comparative model evaluation was found. Most roles are concise, roughly 35–50 lines, with repeated workflow scaffolding. Generic language/architecture/coordination agents mostly duplicate existing workers, CBM and global guidance.

The strongest adaptation sources are reviewer, scientific-literature-researcher, eval-engineer and data-engineer. Performance-engineer is a reasonable fifth source if profiling is frequent; hallucination-investigator is a useful subsection of the eval procedure rather than another permanent persona. NLP-engineer supplies a few retrieval/ranking checks but lacks a concrete retrieval/reranking experimental procedure.

Systemic defect: CONTRIBUTING explicitly prescribes the template `Do not ... unless explicitly requested by the parent agent.` This exception is applied indiscriminately, including to truthfulness, evidence, safety and permission boundaries. Examples permit false causal claims, fabricated resume metrics, unsupported assurance and omitted contradictory literature. Remove those exceptions from every adapted factuality/control instruction. Distinguish harmless scope override from bypassing evidence or safety.

Other concrete findings:

- README's `[instructions].text` example disagrees with all actual files and CONTRIBUTING's `developer_instructions` field. Copy reviewed source structure, not README example.
- Read-only roles sometimes retain implementation wording from templates; constrain review roles to findings/recommendations.
- browser-debugger hardcodes `http://localhost:3000/mcp`. The SSH host's localhost is not the Mac browser. Existing CUA is the correct integration in this environment.
- docs-researcher adds OpenAI developer-docs MCP; existing OpenAI docs skill already covers that source.
- visual-asset-generator prescribes global `npm install -g prompt-to-asset`, an external MCP and unverified free tiers; reject in favor of existing imagegen workflow.
- codebase-orchestrator requires HALT/human approval for every edit, duplicating exploration and conflicting with already-authorized autonomous work.
- No Enroot-specific role or operational procedure exists. Docker and MLOps checklists cannot substitute for current SSH/Enroot project runbooks.
- Root README links an external pied-piper agent, not a tracked primary definition. visual-asset-generator is tracked despite omission from category/root role list; inventory used actual files.

## Agency conclusions and support findings

Markdown personas are converted to TOML with name, description and the Markdown body. The documentation claims unchanged bodies, but the shared `get_body` helper strips every standalone `---` line, including body separators. The Codex converter does not assign model/reasoning/sandbox/tool policy. Installer supports filtering and dry-run but uses cp/ln -sf for same-name targets; it does not merge local customizations or synchronize Mac/SSH hosts. Use reviewed local adaptations only, with local model policy and host-specific discovery verified separately.

No tracked generated Codex agent files exist in this revision: integrations contain adapter documentation plus an MCP-memory example/setup script. No tracked binary asset payloads exist in the inventory. Chinese localization includes a contribution guide, agent-name JSON mapping and PowerShell generator, not a second translated primary-agent collection. An augmented backend persona under integrations/mcp-memory is an integration example, not counted twice as a primary roster definition.


## Final selection and adaptations

Select exactly five Volt roles: **reviewer, scientific-literature-researcher, eval-engineer, data-engineer, performance-engineer**. No Agency persona merits adding to the standing roster. Agency's strongest on-demand references are LLM post-training diagnostics, research synthesis, statistics, Rust refactoring, and targeted domain checklists; use individual concepts when a task calls for them rather than importing broad personas.

Agency final dispositions: 207 out-of-scope (203 scope-screened plus four fully read), 34 reject-as-is, 25 reference-on-demand, 13 overlap. Volt final dispositions: 5 adapt-shortlist, 73 reference-on-demand, 5 reject-as-is, 43 skip-out-of-scope, 49 skip-overlap. CSV rows provide specific per-definition rationale and risks.

Recurring Agency defects include invented experience/persistent-memory claims, oversized mandatory reporting, arbitrary success targets, missing hardcoded support paths, unsolicited production/credential/infrastructure actions, and illustrative code inconsistent with its claims. Concrete examples: the RAG pipeline mixes Document objects and dictionaries and conflates late chunking with ColBERT; data remediation runs model-produced code with eval behind a substring blacklist; experiment tracker targets 95% significant experiments; Evidence Collector mandates 3–5 bugs and treats zero findings as failure; Knowledge Graph Engineer labels unequal claim strings as contradictions; API Tester divides concurrent wall time by request count and calls it mean latency. These are selection evidence, not executed failure reproductions.

Authorized adaptations live in `<collection-checkout>/agents/`. Each preserves its native name and uses `gpt-6-astra`/`low` per user policy, **not an asserted upstream benchmark advantage**. Four remain read-only; data-engineer remains workspace-write. Instructions are 207–218 words each. Removed parent exceptions to factuality, generic persona boilerplate, read-only implementation ambiguity and unsupported confidence. Boundaries separate code defects, published evidence, measurement design, pipeline implementation, and profiling. Added IR candidate/rerank distinctions, paired VLM/spot-difference controls, grouped splits/leakage prevention, no held-out test tuning, bounded/resumable pipelines, and shared SSH/Enroot job preservation. No automatic kills, infrastructure changes or external publication.

Validation: Python `tomllib` parsed all five adapted TOMLs; names, models, effort, sandbox and instruction word counts checked. No upstream snippets, model experiments, installers or long jobs executed. Parent owns repository integration, official/native configuration verification, commits and push. This reviewer changed only the five authorized agent TOMLs and the three review outputs.

Neither repository supplies comparative Astra-specific prompting or performance evidence. Agency conversion changes packaging, not semantics, tool availability, model tuning, or host integration. Install script may auto-run conversion when artifacts are missing and overwrites matching destination filenames without backup; conversion clears generated tool output except README. No Mac-to-SSH synchronization is implemented.

## Supporting tracked-file inventory

### VoltAgent

Read root contributor instructions and installation/format/model sections; category READMEs fully covered with exact repeated-line reuse. LICENSE fully read. Category/readme catalogs contain no separate agent implementation, installer or generated binaries.

### Agency (83 support files)

The following 83 files were inventoried and classified as support, not primary definitions. Local Codex integration README, converter Codex/escaping/discovery/cleanup/dispatch paths, installer Codex/copy/destination/auto-convert/argument paths, and shared frontmatter/body/slug helpers were read. Other integrations, CI, examples and localization assets are inventory/static coverage, not blanket semantic certification; none is a dependency of the five selected native Volt agents.

- `.gitattributes`
- `.github/FUNDING.yml`
- `.github/ISSUE_TEMPLATE/bug-report.yml`
- `.github/ISSUE_TEMPLATE/new-agent-request.yml`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/check-divisions.yml`
- `.github/workflows/check-hermes-config-rewrite.yml`
- `.github/workflows/check-runbooks.yml`
- `.github/workflows/check-tools.yml`
- `.github/workflows/lint-agents.yml`
- `.github/workflows/test-install.yml`
- `.gitignore`
- `CONTRIBUTING.md`
- `CONTRIBUTING_zh-CN.md`
- `LICENSE`
- `README.md`
- `SECURITY.md`
- `divisions.json`
- `examples/README.md`
- `examples/nexus-spatial-discovery.md`
- `examples/workflow-book-chapter.md`
- `examples/workflow-landing-page.md`
- `examples/workflow-startup-mvp.md`
- `examples/workflow-with-memory.md`
- `integrations/README.md`
- `integrations/aider/README.md`
- `integrations/antigravity/README.md`
- `integrations/claude-code/README.md`
- `integrations/codex/README.md`
- `integrations/cursor/README.md`
- `integrations/gemini-cli/README.md`
- `integrations/github-copilot/README.md`
- `integrations/hermes/README.md`
- `integrations/kimi/README.md`
- `integrations/mcp-memory/README.md`
- `integrations/mcp-memory/backend-architect-with-memory.md`
- `integrations/mcp-memory/setup.sh`
- `integrations/openclaw/README.md`
- `integrations/opencode/README.md`
- `integrations/qwen/README.md`
- `integrations/vibe/README.md`
- `integrations/windsurf/README.md`
- `integrations/zcode/README.md`
- `scripts/agents-to-install.example`
- `scripts/build-hermes-plugin.py`
- `scripts/check-agent-originality.sh`
- `scripts/check-divisions.sh`
- `scripts/check-hermes-config-rewrite.py`
- `scripts/check-hermes-config-rewrite.sh`
- `scripts/check-hermes-plugin.py`
- `scripts/check-runbooks.sh`
- `scripts/check-tools.sh`
- `scripts/convert-outputs.sha256`
- `scripts/convert.sh`
- `scripts/i18n/README.md`
- `scripts/i18n/agent-names-zh.json`
- `scripts/i18n/localize-agents-zh.ps1`
- `scripts/install.sh`
- `scripts/lib.sh`
- `scripts/lint-agents.sh`
- `scripts/test-agent-selection.sh`
- `scripts/test-convert-frontmatter.sh`
- `scripts/test-convert-outputs.sh`
- `scripts/test-hermes-plugin.py`
- `scripts/test-install.sh`
- `strategy/EXECUTIVE-BRIEF.md`
- `strategy/QUICKSTART.md`
- `strategy/coordination/agent-activation-prompts.md`
- `strategy/coordination/handoff-templates.md`
- `strategy/nexus-strategy.md`
- `strategy/playbooks/phase-0-discovery.md`
- `strategy/playbooks/phase-1-strategy.md`
- `strategy/playbooks/phase-2-foundation.md`
- `strategy/playbooks/phase-3-build.md`
- `strategy/playbooks/phase-4-hardening.md`
- `strategy/playbooks/phase-5-launch.md`
- `strategy/playbooks/phase-6-operate.md`
- `strategy/runbooks.json`
- `strategy/runbooks/scenario-enterprise-feature.md`
- `strategy/runbooks/scenario-incident-response.md`
- `strategy/runbooks/scenario-marketing-campaign.md`
- `strategy/runbooks/scenario-startup-mvp.md`
- `tools.json`
