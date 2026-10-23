# Set up a separate team laptop

This repository contains the reusable instruction library and its supporting guidance. It is not an image of the operator's laptop: applications, native MCP executables, Python packages, plugin runtime bundles, accounts, credentials and project index databases are separate installations.

## 1. Get the correct branch

```bash
git clone --branch codex/research-helper-refresh-20261002 https://github.com/amitbcp/personal_code_agents.git
cd personal_code_agents
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Use Python 3.11+ for the repository checks. This branch contains additions not yet merged into `main`; cloning `main` does not reproduce this library. Record the actual commit selected for the teammate's installation. Install a supported Codex desktop/CLI version and sign in with the teammate's own account first.

## 2. Install the reusable files

Inspect existing discovery paths and same-named components before copying. Back up existing files and do not create duplicate skill definitions across scanned locations. Use copies for a standalone installation or symlinks only if this checkout remains available. Copy whole skill directories, including their references, scripts, assets and licenses.

| Repository source | Target | Purpose |
| --- | --- | --- |
| Seventeen directories under `skills/` | Personal `~/.agents/skills/`, or the verified discovery location of an existing/custom profile | Research, engineering, figures, UI and OKF workflows |
| Five TOML files under `agents/` | Effective profile's `agents/`, normally `~/.codex/agents/` | Five configured Astra/low, workspace-write specialists |
| Three Markdown files under `guidance/` | Effective profile's `guidance/`, normally `~/.codex/guidance/` | Karpathy-inspired coding, research engineering and scale/concurrency |
| Chosen snapshot under `instructions/global/` | Effective profile's `AGENTS.md`, normally `~/.codex/AGENTS.md`, after adaptation | Personal defaults and on-demand guidance/skill routing |
| `templates/project-AGENTS.example.md` or a relevant actual project snapshot | Existing project-root `AGENTS.md`, merged/adapted | Project sources, task contracts, wiki upkeep and ownership |

The source installations use `~/.codex/skills`; current official guidance lists `~/.agents/skills` for personal skills. Confirm what the teammate's actual profile scans, rather than blindly installing into both. Custom `CODEX_HOME`, remote profiles and older clients can differ. The captured global guides contain the operator's machine paths and project assumptions: update their path references, permission expectations, guidance routes and model availability before activating them. Do not replace the teammate's existing instructions wholesale.

The global AGENTS guide should route non-trivial implementation/review to `karpathy-coding-principles.md`, experiments/evaluations/reports to `research-engineering-practices.md`, and scale-sensitive pipelines to `scale-and-concurrency.md`. Those are guidance files read under the global rule, not additional slash-command skills. Keep the existing seventeen-skill map and project-specific routes where appropriate.

## 3. OKF/research knowledge map

The complete [research-knowledge-map skill](../skills/research-knowledge-map/SKILL.md), [project setup](../skills/research-knowledge-map/references/project-setup.md) and [OKF conventions](../skills/research-knowledge-map/references/okf-conventions.md) are included. Merge the maintenance rule into each intended project guide and reuse the existing wiki location, normally `docs/wiki/`. Installation alone does not create a wiki, ingest conversation history or start a background writer.

Use selected canonical project documents to initialize a new wiki, and source-linked scoped upkeep during authorized work. Keep migration handoffs separate, preserve source files and annotations, and coordinate one writer for overlapping shared wiki pages.

## 4. Native tools, helper dependencies and CBM

- **Archify:** Node.js >=18; run its documented doctor/demo using the skill's directory. No global Archify package or separate Archify plugin is required by our retained skill.
- **Python helpers:** use the consuming project's environment. Repository tests do not install notebook, scientific plotting, model-training or model-memory runtimes. Check the selected skill's actual dependency requirements before use; no blanket lockfile or GPU environment is shipped.
- **CBM:** [optional integration notes and captured profiles](../integrations/codebase-memory/README.md) are included. Install the native server separately for the target OS/CPU, configure the teammate's MCP path and node-local cache, and inspect any definitions created by the upstream installer before using the captured skill/agents. No existing project database is included. Index only authorized roots.
- **Server/project-owned workflow skills:** these are maintained in their project's canonical source, not part of this generic library. Obtain those from the authorized project checkout when the teammate needs that workflow.

## 5. Plugins, built-in skills and connected services

A [public plugin inventory](plugin-inventory.json) records only the bundled/runtime IDs explicitly enabled in the source Mac config at capture time. It is a reference inventory, not a plugin installer, portable cache or entitlement certificate. Match capabilities and target account availability rather than pinning incidental cache directory versions.

| Capability | How to prepare the target laptop |
| --- | --- |
| Core/system skills, app panels and built-in agent tools | Install/update Codex; confirm its current built-in catalog. These are supplied by the product, not this Git repository. |
| Documents, PDFs, spreadsheets, presentations and reusable artifact templates | Enable/install the available official capabilities through the target account's plugin catalog. Their actual runtimes/dependencies are provisioned separately. |
| Browser/computer use, visualization and code review | Use supported capabilities for the target OS/app, and grant required local permissions through the normal UI. Installing instructions does not grant browser/desktop access. |
| Optional iOS/Android, Pages or other specialist plugins | Install only when the workload requires them and the target account exposes them. Cache presence on another machine is not proof of activation. |
| Connected apps, third-party MCP servers and organization plugins | The teammate obtains their own approved installation/access and signs in separately. Do not copy another user's cached bundles, tokens or app credentials. |

Start a fresh chat after plugin installation. Official references: [plugins](https://learn.chatgpt.com/docs/plugins), [skill discovery](https://learn.chatgpt.com/docs/build-skills), [custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents). Catalog and organization access can differ. We do not claim every installed/account-bound plugin is vendored in this public repository.

## 6. Verify on the actual laptop

- Run the repository validator/tests; confirm all seventeen selected skills and five configured agents are discoverable from a fresh Codex session, with no duplicate names or load errors.
- Check that the active global guide resolves the three guidance files on that laptop. Verify all guidance references after adapting paths.
- Ask an ordinary literature/design/debugging question and verify the intended skill can be read. Explicit invocation can confirm availability, but does not prove reliable automatic routing.
- For knowledge-map work, use an authorized disposable/example project and verify source links, correct wiki layout and preservation of existing handoffs. Do not ingest a real project merely as an installation test.
- If CBM is installed, verify version, MCP connection and project-specific coverage with an authorized sample. Do not index the home directory or copy another machine's live cache.
- Verify selected plugin capabilities using the teammate's own access. Report unavailable capabilities as separate setup gaps rather than claiming a full clone of the original environment.

No target-laptop deployment has been performed by publishing this guide. A passing source test suite is distinct from fresh discovery, dependency installation and successful runtime use on another machine.
