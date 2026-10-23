# Instruction layers and deployment alignment

## What belongs in this repository

- `agents/` and `skills/` are the selected reusable runtime library: five custom agent profiles and seventeen skills. Original imports, provenance and adaptation reviews remain separate.
- [Project AGENTS example](../templates/project-AGENTS.example.md) is an original, portable starting point. It is not a copy of personal global instructions or an active project file. Merge only relevant parts into an existing root guide and replace example paths with current project sources.
- [Wiki setup](../skills/research-knowledge-map/references/project-setup.md) defines the default wiki/handoff layout and scoped upkeep rule. It remains authoritative for this skill's initialization procedure.

## What remains outside Git

- Personal global `AGENTS.md` and the personal guidance directory stay local to each profile. Do not copy their contents into this repository, even if the repository is private. Alignment means compatible behavior and routing, not identical files at every instruction layer.
- Repository-specific service names, environments, ports, storage paths and private receipts belong in that project's approved operational documentation. Root project instructions should point to those sources rather than duplicate them here.
- Authentication, conversations, live SQLite databases, CBM indexes, scratch results and installation backups are not library source.
- Official/system/plugin skills and separately installed `codebase-memory` skills/agents are not vendored by this package. A host may legitimately expose more than seventeen skills and five agents.
- Project-owned SKS workflow skills are maintained in their project's canonical source, not silently pulled into this generic collection.

## How the layers cooperate

- Check the effective execution profile and instruction hierarchy. A project guide names product contracts, canonical docs, current task entry points and narrow project routes. Global guidance supplies personal defaults; specialist skills load on demand.
- The project template covers task completion, ownership/delegation, skill routing, source/CBM verification, OKF upkeep and shared-versus-local storage. Remove irrelevant routes instead of growing every project guide indefinitely.
- Configured custom agents select their models and write permissions. The example permits the owner's Luna/max or Astra/low policy without changing the five shipped Astra/low profiles or forcing model names unavailable on a host.
- A root project wiki rule makes upkeep part of authorized substantive work. Skill installation alone neither starts a writer nor guarantees that an agent used it on every turn.
- Check Git-ignore and CBM indexing policy independently. In the verified CBM 0.12.1 setup, repository-local Git-only excludes allow selected private docs to remain Git-ignored while indexed. Treat that as version-specific behavior to verify on upgrades/new clones, not a portable promise of every indexer. Preserve sensitive-data exclusions.
- Git-based watcher state can miss Git-ignored-only documentation changes. Follow explicit project refresh commands and inspect coverage; do not put automatic indexing or cache migration into the instruction template.

## Maintenance and verification

- Before changing the library, inspect branch/dirt and compare selected installed files with source on each effective Mac/remote profile. Do not confuse extra system/plugin/project skills with missing library components.
- Where a deployed file differs, inspect the content and its provenance before choosing a source. Preserve host-specific runtime configuration separately; do not blindly copy an installed profile back into Git.
- Validate native agent TOML, skill frontmatter, retained helper tests and relative links for changed documents. Deploy runtime changes only where authorized, preserving existing profile configuration and backups.
- Verify file installation and fresh Codex discovery separately. A byte-identical file comparison establishes deployment parity; it does not prove automatic invocation or better task outcomes.
- Record the source revision, selected scope, per-profile comparison result, material limitations and validation date. Historical reviews remain dated evidence; they are not current deployment certificates.
- Commit/push authorized source changes to the intended branch. Updating a branch does not merge it into `main` or install anything on a server.
