# Agent workflow for Mhari Reet

## Owner-directed delivery workflow — 13 October 2026

Complete usable features in coherent, issue-linked batches. Optimize for accepted user flows and delivered releases. This owner-approved workflow supersedes older project instructions that require per-ticket broad reruns, receipt-only PRs, or preview publication for documentation-only changes. Higher-priority instructions and operation-specific permission boundaries still apply.

### Plan one deliverable, then finish it

- State the target delivery channel, included issues, acceptance criteria and one integration owner. Group compatible changes that share a user flow or dependencies; keep unrelated work separate. Do not silently remove owner-required features to simplify a release.
- Read `CONTRIBUTING.md`, the relevant current release/testing sections and existing issue/PR work. Load only context needed for the task; historical snapshots are evidence, not current instructions. Avoid another full-history audit or repeated broad catch-up without a concrete need.
- Keep one concise current checklist: issue, owner, completed evidence, exact missing result and next action. Preserve umbrella issues while closing completed acceptance rows. Finish source, usable setup, acceptance and integration before adding more inactive foundations.
- Use recorded approvals within their scope. Reopen a decision only for changed scope, new risk or an actually missing permission. Separate web pilot, native QA, store distribution and production gates; an unrelated future lane must not block an already-approved delivery.

### Consolidate validation for the delivery batch

- Prepare one validation plan covering the included issues and affected environments. Reuse existing coverage and fixtures. During development, run the smallest check that answers a concrete failure or changed behavior; reserve broad applicable suites for the integrated candidate.
- Run the applicable automated checks once per combined candidate in each required environment. Coordinate one device session for overlapping acceptance rows. Parallel agents share results rather than independently rerunning the same suites.
- Rerun for changed relevant inputs, a failure, a changed environment or a concrete unresolved concern. Documentation, receipts and unrelated server changes do not invalidate unchanged app/native evidence. Record the tested source and any relevant input differences once; do not demand fresh hashes or builds merely because Git HEAD moved.
- Add only a focused regression when changed behavior or a security/data-preservation boundary lacks coverage. Synthetic fixtures protect real data and reproduce failures; do not add duplicate cases or repeatedly build synthetic artifacts to report activity. Synthetic passes cannot replace the required physical, provider, private-review or deployed-service result.
- Prepare the isolated QA app, synthetic account/files, supported readback path and acceptance steps before allocating a device. Eligible synthetic native checks, including #149, can proceed independently of Distribution signing; retain release-specific signed-artifact requirements where applicable.
- Preserve existing assertions and applicable release checks. Consolidation does not authorize bypassing publisher guards, hiding failures/skips, fabricating statuses or calling an unrun acceptance row complete. If a script repeats valid work, fix its reuse path through review rather than manually skipping guards.

### Make handoffs executable

- Assign one worker to each bounded task and one peer reviewer to the completed batch. Delegate independent work; avoid overlapping edits, repeated audits or additional clean reviews of unchanged inputs.
- A handoff contains the actual worker/lane, candidate, usable fixture or private access pointer, permitted actions and expected result. Use verified account handles and the real shared work queue; `@amitbcp2` is not a verified GitHub account. The Amit lanes use `amitbcp` and identify their lane explicitly.
- Device and shared-preview reservations have an owner, candidate and end time. Arrange a safe handoff for an active session; resolve an unknown reservation with its owner instead of holding publication indefinitely.
- Post only changed outcomes, actionable findings or exact blocker requests. Do not repeat unchanged pings, copy the whole board across destinations, or ask the owner to relay routine coordination. When blocked, complete independent in-scope work and name the smallest missing input and its owner.
- Reuse checkouts, caches and approved artifacts. Prefer Vulcan for heavy builds/emulators while the Mac is short on space. Use parallel compute only for useful independent work; avoid duplicate installs, large asset copies and speculative tooling.

## Publish one integrated app candidate to the existing preview

The owner authorizes the existing Firebase Hosting preview for app-affecting delivery batches:

- Project: `marus-84f95`
- Existing channel: `family-test`
- Exact URL: `https://marus-84f95--family-test-vphe071p.web.app`
- Renew this channel for 30 days when deploying; do not create a new channel or substitute production.

Commit the integrated app candidate, then use `npm run push:preview` as its final consolidated publisher gate. It runs required checks, builds the approved real inputs, pushes, deploys and verifies the same preview. If already pushed or publication needs retrying, use `npm run deploy:preview`; follow its guards and investigate the actual failure before retrying.

Intermediate review branches may be pushed without taking over the shared preview. The integration owner publishes the combined app candidate before delivery, or reports the exact publication blocker. A Git push or merge is not evidence that the phone app changed. When merged and tested app/build/config/reference inputs are unchanged, carry the candidate's valid evidence forward and accurately record the served revision; avoid another deployment solely to change the Git marker.

Documentation/guidance-only, receipt-only and test-only changes with no deployable input change require appropriate diff/review checks, not app builds, full suites, native signing or Hosting publication. Server-only changes use their affected checks and applicable service boundaries. These exemptions do not apply to shipped assets, config, packaging or build logic that changes the app.

Put one immutable publication receipt on the substantive PR/release record: served commit, unchanged URL, verified expiry and material limitations. Keep `docs/RELEASE_READINESS.md` to current readiness, material activation/cost decisions and links to receipts. Do not create a receipt-only PR that triggers another deployment and receipt.

Do not silently recreate a missing or expired channel, change the origin, weaken checks/security, or enable billing to get a deployment through. Request missing access using the normal sign-in flow; never ask for account passwords or put credentials into Git/issues. GitHub background deployment is not configured: its CI currently has neither approved real reference inputs nor a deployment identity.

## Release and privacy boundaries

- Publish only the reviewed `www` build with its explicit approved reference-book projection. Never publish the workspace root, `private-content`, WhatsApp chats/media, mixed local catalogs, personal uploads, backups, or QA artifacts.
- Never deploy the synthetic PDFs/catalogs generated for CI.
- Use Hosting preview deployment only. This standing authorization does not cover production Hosting, Auth-provider changes, Firestore/Storage rules, shared-family backend activation, paid plans, or store releases.
- Preview login and backups use the real Firebase project; do not mutate real accounts/data as a smoke test.
- Preserve IndexedDB, local preferences, user originals, and account boundaries. Keep the same preview origin and never instruct routine site-data clearing or reinstallation.
- Keep the per-release worker marker and existing user-controlled **Refresh** prompt working. Do not force reload unfinished forms or recordings.

Use the existing approved preview for the already-approved first web pilot; missing inputs for a new publication do not block that session if the current preview and session controls remain approved. The owner retains private intake/participant records; record aggregate outcomes only. See `docs/PHONE_TESTING.md` and `docs/TESTING.md` for the applicable controls and real-versus-synthetic distinction.

## Done means delivered acceptance

Complete the included user flows, pass their applicable consolidated checks, obtain independent peer review, integrate the reviewed batch and verify its target delivery. Record actual acceptance and close completed issues; leave any remaining epic criteria explicit. No feature is complete solely from a plan, disabled scaffold, test count, simulated result or status update. Once the agreed outcome is met, stop adding checks and bookkeeping.
