# Karpathy-Inspired Coding Principles

**Applies to:** Every non-trivial implementation, refactoring, debugging, or code review task executed by Astra/Codex agents.
**Core Anti-Patterns Prevented:** Unchecked assumptions, over-complication (speculative generality), orthogonal damage (drive-by edits), and unvalidated completion.

## 1. Think Before Coding (Alignment)
*   **Do Not Assume:** Never silently reconcile conflicting instructions or guess user intent. State your assumptions about inputs, environment, and existing behavior explicitly.
*   **Surface Tradeoffs:** If multiple valid designs exist, name the alternatives concisely and justify your chosen path before executing.
*   **Push Back:** If a request fundamentally contradicts the codebase's established architecture, propose the better path and wait for user confirmation.
*   **Ask First:** If an open question materially changes the correctness or scope of the result, stop and ask. Provide concrete options.

## 2. Simplicity First (YAGNI)
*   **Minimum Viable Code:** Write the absolute minimum code required to solve the explicit request. Three clear lines always beat a generalized mechanism.
*   **No Speculative Generality:** Zero new abstractions, plugin points, or config knobs for unstated future needs. No "while I'm here" features.
*   **Existing Tools:** Rely strictly on the "boring," standard tools already present in the project. Do not introduce new dependencies, frameworks, or MCP servers unless explicitly directed.
*   **Bounded Error Handling:** Handle only the failure modes the code can *actually* hit. Make errors actionable. Do not write defensive code for mathematically or logically impossible states.

## 3. Surgical Changes (Zero Orthogonal Damage)
*   **Strict Scope:** Touch *only* what the task explicitly requires. 
*   **No Drive-By Edits:** Absolutely no opportunistic refactoring, renames, reformatting, or fixes to unrelated code—even if it is objectively poorly written. 
*   **Chameleon Style:** Match the surrounding style and conventions perfectly, even if you would author it differently from scratch.
*   **Debris Cleanup:** Remove your own scaffolding, temporary debug prints, and unused imports before submitting for review.
*   **Log, Don't Fix:** If you notice unrelated bugs or tech debt, list them briefly at the end of your task report. Do not include them in your diff.

## 4. Goal-Driven Execution (Verification)
*   **Define the Check:** Before writing implementation code, establish the verifiable outcome: exactly which test must pass, what output must match, or what metric must improve. Write the test first if one does not exist.
*   **Milestones:** For multi-step work, state the plan as a series of independently verifiable milestones.
*   **Execution Loop:** Implement → Run Check → Fix → Repeat. 
*   **Proof of Work:** Never report a task as "done" based merely on reading the generated code. You must report the actual commands run, the terminal output observed, and the specific metrics verified.