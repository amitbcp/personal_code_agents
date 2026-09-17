---
name: train-sentence-transformers
description: Design or update Sentence Transformers training for dense retrieval, CrossEncoder reranking, learned sparse retrieval or multi-vector models, including loss/data alignment and leakage-aware evaluation. Use for training or evaluation planning and implementation.
license: Apache-2.0
---

<!-- Modified 2026-09-17 for Personal Code Agents; see CHANGES.md and provenance.json. -->

# Train retrieval models

Adapted from Hugging Face Skills; see repository provenance.json and CHANGES.md.

## Start from the project

Use its existing trainer, environment, dataset contracts and experiment ledger. Determine whether the requested model is a bi-encoder, CrossEncoder, sparse encoder or multi-vector encoder; do not replace the model family simply to fit an example. Check the installed Sentence Transformers/Transformers versions and their matching official documentation before choosing loss classes or argument names.

Run on the authorized execution host/allocation. Keep Python environments and caches appropriate to that host; shared source paths do not imply shared usable GPUs. Preserve user-selected models, hardware and concurrency unless evidence warrants a proposed change. Do not install drivers, build custom frameworks or switch to paid cloud compute as an automatic fallback.

## Data and objective

- Establish the unit of independence and split before mining or training. Related queries, source documents and near duplicates can cross splits even when row IDs differ.
- Mine negatives from permitted training data; record the retriever, candidate depth, filtering and positive-label coverage. Do not mine from the held-out final test set.
- Preserve query/document prompts, tokenizer/truncation, pooling, normalization and similarity conventions across training, evaluation and inference. Verify the intended settings survive checkpoint save/reload; model-card defaults are not interchangeable across model families.
- For in-batch negatives, inspect batch sampling and duplicates: another query’s positive may also be relevant to this query. Check the loss’s handling of multiple positives and false negatives.
- Check real batch columns, order, tensor shapes, masks and labels against the installed loss API. Pointwise labels, pairwise margins and listwise relevance are different contracts.
- Choose class weighting, score activation, sequence length and negative counts from the experiment; no universal setting is optimal.
- For cached contrastive losses, sparse regularizers or multi-vector scoring, verify library compatibility and inspect a small forward/backward batch before scaling.

Read [evaluation.md](references/evaluation.md) when designing or changing evaluation; [cross-encoder.md](references/cross-encoder.md) for reranker-specific checks.

## Run and compare

For a planning-only request, provide the protocol and leave execution steps below as proposed work.

1. Record the existing baseline on development data before making the change.
2. Smoke-test a small training batch, evaluation batch, checkpoint save and reload using the project environment. Check finite loss, expected gradients, scoring behavior and evaluator metric names.
3. Run the authorized experiment with explicit config, seed, split identity, package versions, hardware, batch size and concurrency. Use the project's tracker and output paths; do not require a new tracker or fixed log format.
4. Select checkpoints and tune on development data. Keep the final test reserved for the agreed frozen comparison. Report failures and negative results alongside successful runs.
5. Save checkpoints locally or to the project's authorized durable storage. Hub uploads, public repositories, external metrics syncing and paid jobs require authorization for that destination/action; local training does not imply publishing.

A small score increase alone is not a win. Compare paired query-level uncertainty, candidate recall, latency, memory and training cost. When data are too small to distinguish runs, report that uncertainty rather than emitting an unconditional WIN verdict.

## References

- [Sentence Transformers training overview](https://www.sbert.net/docs/sentence_transformer/training_overview.html)
- [CrossEncoder training overview](https://www.sbert.net/docs/cross_encoder/training_overview.html)
- [Sentence Transformers documentation](https://www.sbert.net/)

Use current documentation for the installed release. Examples from the upstream import are retained in Git history; they are not executable defaults in this collection.
