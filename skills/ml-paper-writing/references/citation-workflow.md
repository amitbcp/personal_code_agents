# Verified citations

## Identity and claim support are separate checks

1. Start with the existing bibliography and papers already used by the project. Reuse valid citation keys. Search only for missing or uncertain sources using available tools; no particular provider, plugin, or paid service is required.
2. Resolve the intended paper from an authoritative source such as the publisher, official proceedings, or the paper's arXiv record. Match title, authors, year, and identifier; distinguish a preprint from its published version. Use another source when metadata conflict or identity remains uncertain.
3. Read the relevant passage, equation, table, or experimental setup. Record where it supports the proposed claim and retain its qualifications. Metadata, abstracts, or keyword matches alone cannot verify detailed empirical or mathematical claims.
4. Retrieve bibliography metadata from the authoritative record where available. Check it against the paper. If formatting metadata manually, transcribe only verified fields; omit unknown fields rather than guessing them. Preserve the venue's required bibliography system and existing key conventions.
5. Insert the citation near the supported statement. Check every new key resolves, remove accidental duplicates, and verify title capitalization and author names survive the bibliography build.

## Keep a lightweight evidence record

For a substantial literature update, retain the citation key, canonical URL/identifier, version, access date, claim, and supporting page/section/table in the project's existing notes. This is a research record, not text to dump into the manuscript.

If the full text is unavailable, state the access limitation. A verified abstract may support an abstract-level statement; it cannot support unseen methodological details. Leave a visible unresolved citation marker in a working draft or remove the unsupported claim. Never invent a plausible source to complete a sentence.

## Optional automation

Use the project's existing bibliography tooling when it helps. API results need the same identity/content checks as browser results. Bound requests with timeouts and retry limits, respect the provider's current rate limits, cache successful metadata, and preserve existing bibliography entries. Do not automatically cite the first search result, treat an error response as a verified record, overwrite a bibliography with a batch result, or turn failed verification into a successful cached citation.
