---
name: research-knowledge-map
description: Create, query, or deliberately update a source-linked map of research papers, concepts, claims, contradictions, and open questions in project Markdown notes. Use for a durable literature memory map, not code indexing or automatic conversation memory.
---

# Research Knowledge Map

Maintain inspectable research knowledge in the project's existing notes. Treat the map as a navigational synthesis whose claims can be traced back to sources.

## Choose the smallest useful representation

Read the existing index and relevant notes first. Reuse identifiers, bibliography keys and directory conventions. For a small collection, one index plus linked paper/concept notes is sufficient. For a larger collection, an edge table may help. Do not introduce a graph database, embeddings service or automatic watcher merely to draw a map.

Separate source records, generated synthesis and personal annotations. Preserve raw material and historical notes; corrections should identify the superseded claim/version. Store authorized source copies only, with provenance. Link restricted or large material instead of duplicating it. Do not import credentials, conversation dumps or private global agent instructions.

## Make relationships meaningful

Identify papers by verified stable IDs and versions; resolve concept aliases without collapsing genuinely different definitions. Each meaningful relationship should have:

| From | Relation | To | Source/location | Conditions/version | Evidence status |
|---|---|---|---|---|---|

Useful relations include *uses*, *extends*, *tests*, *supports under conditions*, *contradicts under conditions*, and *requires prerequisite*. A citation edge alone does not imply support. An embedding neighbor is a candidate relationship, not scientific evidence. Keep your conjectures visibly distinct from source-backed edges. “No supporting source found” is not a negative experimental result.

If drawing a diagram, derive it from the recorded relationships and include a legend. Visual proximity, color and arrow direction should not invent stronger claims than the underlying records. Avoid a forced diagram for a tiny list.

## Query and maintain deliberately

For a question, retrieve relevant notes, verify consequential claims against their source versions, and answer with citations. Do not rewrite the map merely because it was queried. Note stale or unsupported records and continue from available evidence.

For a requested ingest/update, list affected records, read the new source, update only supported claims and relationships, preserve unresolved contradictions, and append a concise change record. Check local links, source locators and the index after edits. A failed fetch should leave existing records intact and be recorded as unavailable, not retracted.

Keep files in the agreed project or personal notes folder. Project Markdown can live beside NFS-hosted code; coordinate ownership of files during concurrent edits and inspect changes before overwriting. This skill does not change CBM settings, rebuild an index, relocate live SQLite databases, share Codex histories, or schedule background work. Knowledge notes and a codebase structural index serve different purposes.

## Design provenance

Original project procedure inspired by Karpathy's public LLM Wiki idea and reviewed evidence/identity concepts in K-Dense's market-research-reports, ncats-arax and ontology-term-resolution skills. No biomedical runtime or community wiki helper is bundled. See [research workflow and sources](https://github.com/amitbcp/personal_code_agents/blob/main/review/research-workflow.md).
