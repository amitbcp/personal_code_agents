# Domain vocabulary and invariants in the existing wiki

Use when an authorized knowledge update changes domain concepts or records a consequential decision. Navigate the current OKF index and canonical glossary/decision locations first. Reuse those pages and identifiers; do not introduce a second root glossary, ADR tree or knowledge runtime.

For an overloaded term, record the preferred name, concise domain definition, context, aliases and distinctions that matter. Preserve aliases used by existing sources so links remain discoverable. Distinct contexts may legitimately use the same word differently; record the boundary instead of forcing a universal definition. General programming vocabulary needs no project glossary entry.

Separate definition from behavior and implementation evidence. An invariant is a condition claimed to hold across allowed states, such as “a completed run references the immutable evaluation dataset version.” Record its scope, counterexamples/edge cases, and the code, tests, schema or empirical evidence that supports it. A desired invariant is a requirement, not a verified property. Check consequential claims against current source; expose contradictions between documentation, user intent and implementation without silently choosing a winner.

Resolve routine terminology from evidence within scope. Ask only when competing meanings materially block correctness, while continuing independent work. Link implementation details from the concept instead of burying them inside its definition.

Record a decision in the existing decision location when it captures a real, meaningful tradeoff whose rationale future readers will need. Include context, alternatives, accepted choice, consequences and evidence; avoid ceremonial ADRs for routine reversible choices. If no location exists, add only the needed Concept or Decision page inside the established OKF bundle, with valid metadata, source links, index entry and log update. Preserve annotations and dated superseded knowledge.

Adapted from mattpocock/skills domain-modeling; its root glossary/ADR layout and repeated interview gates are intentionally replaced with the existing OKF paths and authorization model. See `LICENSE.mattpocock`.
