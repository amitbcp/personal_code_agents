# Agent workflow for Mhari Reet

Read `CONTRIBUTING.md` and the relevant testing/release documentation before changes. Preserve the user's existing work and private data. Use small issue-linked branches/PRs, regression tests, and peer review; preview publication does not authorize merging a PR.

## Every pushed change must reach the existing test preview

The owner explicitly authorizes keeping this Firebase Hosting preview current after code pushes:

- Project: `marus-84f95`
- Existing channel: `family-test`
- Exact URL: `https://marus-84f95--family-test-vphe071p.web.app`
- Renew this channel for 30 days when deploying; do not create a new channel or substitute production.

After committing, use `npm run push:preview`. It runs checks/tests, builds the real approved inputs, pushes the current branch, deploys the same preview, and verifies the published revision. If HEAD is already pushed or a deployment needs retrying, use `npm run deploy:preview`; this runs the same checks without another push.

Plain `git push` has no deployment hook. After any agent code push, publish and verify the preview before the final handoff, or clearly report that Git was pushed but Firebase publication is blocked and explain what access/input/check failed. Do not claim the phone app is updated solely because the repository changed. Coordinate parallel work because the shared preview can show only one branch/revision at a time. Report its verified commit and expiry alongside the unchanged link.

Do not silently recreate a missing or expired channel, change the origin, weaken checks/security, or enable billing to get a deployment through. Request missing access using the normal sign-in flow; never ask for account passwords or put credentials into Git/issues. GitHub background deployment is not configured: its CI currently has neither approved real reference inputs nor a deployment identity.

## Release and privacy boundaries

- Publish only the reviewed `www` build with its explicit approved reference-book projection. Never publish the workspace root, `private-content`, WhatsApp chats/media, mixed local catalogs, personal uploads, backups, or QA artifacts.
- Never deploy the synthetic PDFs/catalogs generated for CI.
- Use Hosting preview deployment only. This standing authorization does not cover production Hosting, Auth-provider changes, Firestore/Storage rules, shared-family backend activation, paid plans, or store releases.
- Preview login and backups use the real Firebase project; do not mutate real accounts/data as a smoke test.
- Preserve IndexedDB, local preferences, user originals, and account boundaries. Keep the same preview origin and never instruct routine site-data clearing or reinstallation.
- Keep the per-release worker marker and existing user-controlled **Refresh** prompt working. Do not force reload unfinished forms or recordings.

Record material activation/cost boundaries and verified deployment evidence in `docs/RELEASE_READINESS.md` and the PR/handoff. See `docs/PHONE_TESTING.md` for phone refresh instructions and `docs/TESTING.md` for the real-versus-synthetic build distinction.
