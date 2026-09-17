# K-Dense semantic review completion

Reviewed revision `330c8e764435a731eff571e3efdda70b363d0792`.

## Coverage

All **166/166 SKILL.md entrypoints** have now received full semantic reading: the prior 44 plus all 122 formerly scope-screened entries. No entrypoint remains pending or scope-only. `kdense.csv` records every package decision; `kdense-completion-notes.json` preserves substantive findings for the additional 122. Deferred packages are references or conditional future options, not installation recommendations.

The common citation tail was compared across all entrypoints: all 136 occurrences are exactly identical, so earlier omitted repetitions were reused losslessly. All other bodies were read in bounded batches; oversized/truncated requests were reread before recording coverage.

Prior whole-tree static coverage remains 2,484 tracked files: 2,313 UTF-8 text files (27,934,705 bytes) and 171 binary assets (169 PNG, 2 GIF), with 692 Python files AST-parsed. This is mechanical supporting-file coverage, not semantic certification of every supporting algorithm. The 13 scripts retained with hypothesis-generation/get-available-resources were fully inspected in the earlier adaptation; the earlier smoke record documents 12 cases. Binary assets were classified, not decoded or executed. No upstream programs, installs, cloud submissions, or model downloads were run in this completion pass.

## Selection and cross-domain findings

The existing compact selection remains appropriate. No additional imports or destination adaptations are needed from this completion pass.

- Survey workflow: literature-review and research-lookup offer search/screen ledgers, contradictory evidence passes, verified versus search-only coverage, claim-source excerpts, and explicit shortfalls. Provider mandates and fixed reference quotas should not transfer.
- Paper reading: scientific-critical-thinking plus market-research-reports' claim/source/calculation/assumption ledgers; Waypoint illustrates tokenizer coverage, pooling parity, grouped study splits, simple baselines and downstream performance diverging from pretraining loss.
- Knowledge maps: ontology-term-resolution's canonical IDs and unresolved states; ncats-arax's typed edges, exact bindings and source-versus-aggregator provenance. Keep local SKS/CBM architecture; importing biomedical graph services adds no necessary value.
- Experiment design: scikit-survival's prediction/metric contracts and training-only nuisance estimation; RELSA's score-composition drift, reference frames and interval-width/coverage pairing; SimPy's independent replications, unfinished-entity accounting and time-weighted monitoring. These are methodological references, not grounds to install their domain stacks.
- Pipeline engineering: schema validation does not guarantee side-effect-free dry runs; Tamarind explicitly uploads inline files during validation. Parent aggregation completion differs from subjob completion. Typed results, stable IDs, bounded polling, observed count reconciliation and missing-versus-zero distinctions recur across useful domain examples.

## Material limitations and defects observed in entrypoints

TimesFM labels q10–q90 as a 90% interval (it is 80%) and q20–q80 as 80% (it is 60%); its alert interpretation and universal calibration/preflight-safety claims should not be reused. TileDB-VCF's purported BED-style string conversion conflicts with its 1-based region contract. Molecular-dynamics examples disagree about integration timestep; pydeseq2's suggestion that interaction terms fix perfect confounding is invalid. Paperclip's shell sourcing of a .env file executes its contents. What-if-oracle's golden-ratio resource allocation and overlapping scenario probabilities lack a sound inferential basis. Provider-bound schematic scores cannot establish scientific correctness; generated slide copies of actual data figures can alter evidence.

These are static observations and methodological judgments, not live API verification or security certification. Package licenses vary despite the collection's umbrella licensing; proprietary and noncommercial packages should not be blanket-imported. Model-specific superiority, including Astra performance, is not established by these entrypoints.
