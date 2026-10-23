---
name: property-based-testing
description: "Writes, reviews, and debugs property-based tests — Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. Use whenever tests should cover a whole input domain instead of a hand-picked list of examples: encode/decode and serialize/deserialize pairs, parsers, canonicalizers and normalizers, validators, numeric and Decimal types, comparators and sort order, data structures, and smart-contract state invariants. Also use when adding cases to an existing @given, fast-check, or proptest suite, when judging whether existing property tests assert anything real, and when a generator has shrunk a counterexample and you need to tell a wrong property from a genuine bug. Not for coverage-guided binary fuzzing (libFuzzer, AFL), mutation-testing campaigns, static analysis, benchmarking, or end-to-end UI tests."
---

# Property-Based Testing

An example test asserts one point. A property asserts a rule over the whole input
domain and lets the generator hunt for the counterexample. That trade is worth making
when the code has an algebraic shape — an inverse, an invariant, an oracle — and not
otherwise. Code with no such shape gets example tests; saying so is a valid outcome.

Check first whether the shape is missing or merely buried. A calculation wrapped in I/O,
a string built by concatenation, an in-place mutation — each has a property and no seam
to assert it through. See [references/refactoring.md](references/refactoring.md) before
concluding there is nothing to assert.

## Property catalog

| Property | Formula | Where it applies |
|---|---|---|
| Roundtrip | `decode(encode(x)) == x` | Serialization, conversion pairs |
| Inverse | `f(g(x)) == x` | encrypt/decrypt, compress/decompress |
| Oracle | `new(x) == reference(x)` | Optimization, refactoring, reimplementation |
| Idempotence | `f(f(x)) == f(x)` | Normalization, formatting, sorting |
| Invariant | Holds before and after | Any transformation, contract state |
| Easy to verify | `is_sorted(sort(x))` | Complex algorithms with cheap checkers |
| Commutativity | `f(a, b) == f(b, a)` | Binary and set operations |
| Associativity | `f(f(a,b), c) == f(a, f(b,c))` | Combining operations |
| Identity | `f(x, e) == x` | Operations with a neutral element |

A useful heuristic, not a universal strength ordering:
`no crash → type preservation → invariant → idempotence → roundtrip / oracle`.

Assert the strongest property the code supports. "No crash" alone rarely justifies the
dependency — if that is all you can find, either a small rearrangement exposes something
stronger, or the honest report is that this code is a poor PBT candidate. Rule out the
first before settling for the second.

## The two ways a property test asserts nothing

- **Tautology.** An assertion that compares a value with itself, or computes its expectation using the same potentially defective helper, cannot independently check the intended contract. A specification-based oracle such as `add(a, b) == a + b` is valid when addition is the independent contract, even if the current implementation is short. Preserve that oracle and supplement it with algebraic properties; those laws alone may admit incorrect implementations. Repeated calls can test determinism when that is the intended property.
- **Vacuity and rejected inputs.** A reachable test that conditionally skips every meaningful assertion may pass vacuously. Excessive or contradictory Hypothesis `assume()` filters instead can produce a health-check failure or unsatisfiable-input error; do not report that as a passing zero-case test. Generate valid inputs directly where practical and verify that the intended assertions execute.

## Where to look next

Load the one that matches the task in front of you:

| Task | File |
|---|---|
| Writing new tests, designing strategies | [references/generating.md](references/generating.md) |
| The code has no property to assert yet | [references/refactoring.md](references/refactoring.md) |
| Reviewing existing property tests | [references/reviewing.md](references/reviewing.md) |
| A property test just failed | [references/interpreting-failures.md](references/interpreting-failures.md) |
| Library choice, Echidna and Medusa | [references/libraries.md](references/libraries.md) |

## Introducing PBT to a project that lacks it

- Reuse the project's PBT library and test conventions.
- If adding a library is already authorized, make the smallest appropriate development dependency change and verify it. Otherwise propose the concrete property and dependency only when that decision blocks work; continue independent analysis.
- Keep production refactors within the requested scope. A test-only inverse belongs in test code unless production needs it independently.
- Ground invariants in actual contracts. Heuristic rankings and model outputs require appropriate evaluation; do not invent algebraic guarantees.
- Record seeds, shrunk counterexamples, strategy bounds and commands so failures can be replayed.

See [attribution](ATTRIBUTION.md) for the adapted CC-BY-SA-4.0 source and license.
