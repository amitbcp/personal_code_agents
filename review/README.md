# Selection review — 2026-09-16

## Scope and coverage

Six repositories were cloned at the exact revisions in [sources.json](sources.json). The four requested catalogs and two relevant official additions contain **788 primary definitions**. Every definition received a catalog decision. This expands the earlier sample into a complete selection inventory; it is not a claim that every line received a semantic or security audit.

| Catalog | Tracked files | Definitions | Fully read entrypoints | Other decisions |
|---|---:|---:|---:|---|
| VoltAgent | 191 | 175 | 175 | Exact repeated boilerplate reviewed once |
| K-Dense | 2,484 | 166 | 44 | 122 scope exclusions from descriptions/dependencies |
| Orchestra | 529 | 98 | 69 | 29 scope-based deferrals |
| Agency Agents | 362 | 279 | 76 | 203 scope exclusions from descriptions |
| Hugging Face | 203 | 26 | 9 | 17 catalog-screened deferrals |
| OpenAI | 783 | 44 | 3 | 41 catalog-screened deferrals |

The entire tracked corpus was mechanically scanned: **4,552 files**, including full-text cue scans of **4,323 text files** and classification of **229 binary assets**. Python source files were parsed without execution. Binary assets were not all rendered. Full-file mechanical scanning is not equivalent to reading every algorithm, validating every claim, or executing every example. All selected entrypoints were read directly; supporting material received the different inspection levels recorded in the reports. No Astra-specific quality advantage was established.

Per-entry decisions: [VoltAgent](voltagent.csv), [K-Dense](kdense.csv), [Orchestra](orchestra.csv), [Agency](agency.csv), [Hugging Face](huggingface.csv), [OpenAI](openai.csv). Candidate `include` decisions in upstream ledgers are shortlists; the **five agents and six skills in the repository** are the final selection. Deferred items are not installed and are not implicitly endorsed unchanged.

The [tracked-file inventory](tracked-files.csv) records mechanical coverage separately. To reproduce it from six separate source checkouts:

```bash
python3 review/scan_sources.py --sources /path/to/source-checkouts --output /path/to/new-review-output
```

## Why this collection

- **VoltAgent:** the closest native Codex agent format: real TOML role definitions. Retain only five distinct responsibilities. Native format does not establish scientific correctness or Astra tuning.
- **K-Dense:** retain hypothesis generation and resource inspection. They add useful local procedures and bounded helpers. Most biomedical/domain tooling is unrelated to the current work; broad artifact skills duplicate existing capabilities.
- **Orchestra:** retain paper writing after correcting citation, workflow and venue assumptions. Framework and distributed-training recipes should be selected when a project actually adopts that stack.
- **Agency Agents:** no whole persona retained. Many roles overlap existing capabilities; several recipes contain unsupported quotas, forced workflows, correctness defects or infrastructure actions. Useful evaluation ideas inform the narrow adapted roles.
- **Hugging Face:** retain retrieval/reranking guidance and memory estimation. Remove default publishing and treat experiment choices as project-dependent.
- **OpenAI:** retain notebook scaffolding with a project-output fix. Existing artifact and system skills need no second copy.

This complements existing CBM agents, project guidance and ordinary workers. It does not introduce a new orchestration platform, tracker, database, agent runtime or automatic installation layer.

## Material fixes

The adaptation removes factuality exceptions, fabricated experience, mandatory finding quotas, blanket approval gates, default public uploads and fixed experiment verdicts. Evaluation guidance distinguishes real retrieval from oracle candidate pools, prevents split leakage, preserves pair/group identity and demands evidence for performance claims. Resource advice is allocation-aware and never authorizes killing healthy jobs. Citation identity and actual claim support are separate checks.

Detailed source findings: [agent catalogs](agents.md), [K-Dense](kdense.md), [Orchestra](orchestra.md). Those reports mention working investigation artifacts beyond this published dossier; only linked files here are bundled. Review findings apply to the pinned source revisions, not every future upstream version.

## Validation and limits

- All six skills passed the Codex Skill Creator frontmatter validator.
- Five agent TOMLs, retained Python syntax and 11 provenance mappings passed local validation.
- Two notebook regression tests passed: working-project output placement and explicit overwrite protection.
- Twelve bounded K-Dense helper smoke checks passed, including valid/invalid inputs, local resource detection, advisory memory warnings and hypothesis templates. These do not establish scientific validity or Linux/GPU correctness.
- An independent agent applied the adapted reranking skill to a planning-only case with eight queries from two documents, checkpoint selection on a reused test split, gold-inserted candidates and a 0.61 to 0.63 nDCG change. It correctly classified the result as exploratory oracle-candidate evidence, identified leakage and dependence, proposed a fresh grouped evaluation, and ran no training or uploads. Feedback led to an explicit planning-only instruction. This is one behavioral smoke check, not a quality benchmark.
- Selected-package local references and whitespace checks passed. No GPU training, paid service, publication, live profile installation or server configuration change was performed.

The unchanged upstream baseline and adapted state are separate commits. Use the adapted state, review it for the actual task, and validate discovery separately before installing on Mac or a remote Codex profile.
