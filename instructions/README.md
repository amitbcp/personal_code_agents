# Actual deployed instruction files

These are owner-authorized, exact-byte snapshots of the active global, workspace and project `AGENTS.md` files captured on 2026-10-23. The purpose is Git history, review and informed team reuse. They are distinct from the portable [project example](../templates/project-AGENTS.example.md).

The active files were read from the Mac and both effective node-local Vulkan profiles. Shared-project files were independently read through both nodes and matched byte-for-byte; one shared copy is kept here. Both node-local global files remain separate so future differences have clear history. [manifest.json](manifest.json) records exact source paths, capture time, original modification times, sizes and comparison results. Capture time does not mean every instruction or operational fact was reverified that day.

## Inventory

| Snapshot | Source host(s) | Active source path |
| --- | --- | --- |
| [global/mac/AGENTS.md](global/mac/AGENTS.md) | Mac | `/Users/aamita/.codex/AGENTS.md` |
| [workspaces/mac/AGENTS.md](workspaces/mac/AGENTS.md) | Mac | `/Users/aamita/AGENTS.md` |
| [projects/mac/agentic_sks/AGENTS.md](projects/mac/agentic_sks/AGENTS.md) | Mac | `/Users/aamita/Oracle/oracle/bitbucket/agentic_sks/AGENTS.md` |
| [projects/mac/marus/AGENTS.md](projects/mac/marus/AGENTS.md) | Mac | `/Users/aamita/Oracle/amitbcp/marus/AGENTS.md` |
| [projects/mac/marus-active-main/AGENTS.md](projects/mac/marus-active-main/AGENTS.md) | Mac | `/Users/aamita/Oracle/amitbcp/marus/tools-local/worktrees/active-main-20261005/AGENTS.md` |
| [global/vulkan-7783/AGENTS.md](global/vulkan-7783/AGENTS.md) | vulcan-a100v2-7783 | `/mnt/localdisk/enroot/sks/codex/home/AGENTS.md` |
| [projects/shared/agentic_sks/AGENTS.md](projects/shared/agentic_sks/AGENTS.md) | vulcan-a100v2-7783, vulcan-a100v2-6269 | `/mnt/rag/aamita/project/agentic_sks/AGENTS.md` |
| [projects/shared/sks_media/AGENTS.md](projects/shared/sks_media/AGENTS.md) | vulcan-a100v2-7783, vulcan-a100v2-6269 | `/mnt/rag/aamita/project/sks_media/AGENTS.md` |
| [projects/shared/rerank/AGENTS.md](projects/shared/rerank/AGENTS.md) | vulcan-a100v2-7783, vulcan-a100v2-6269 | `/mnt/rag/aamita/project/rerank/AGENTS.md` |
| [projects/shared/amit/AGENTS.md](projects/shared/amit/AGENTS.md) | vulcan-a100v2-7783, vulcan-a100v2-6269 | `/mnt/rag/aamita/research/amit/AGENTS.md` |
| [projects/shared/marus/AGENTS.md](projects/shared/marus/AGENTS.md) | vulcan-a100v2-7783, vulcan-a100v2-6269 | `/mnt/rag/aamita/project/marus/AGENTS.md` |
| [projects/shared/story_to_frames_eval/AGENTS.md](projects/shared/story_to_frames_eval/AGENTS.md) | vulcan-a100v2-7783, vulcan-a100v2-6269 | `/mnt/rag/aamita/research/amit/tasks/research/story_to_frames_eval/AGENTS.md` |
| [global/vulkan-6269/AGENTS.md](global/vulkan-6269/AGENTS.md) | vulcan-a100v2-6269 | `/mnt/localdisk/enroot/sks/codex/home/AGENTS.md` |

## How to reuse and maintain

- Read these files as deployed configuration records. Host paths, service names, environments, permissions, project assumptions and operational references belong to their source context; review and adapt them before use on another machine or project.
- These copies intentionally preserve the originals, including historical statements and local links. Relative links and absolute paths resolve in the original environment, not necessarily inside this repository. The three selected guidance documents are now separately included under [guidance/](../guidance/README.md). Other references, private receipts, runtime config and credentials are not included merely because an AGENTS file names them.
- A snapshot may itself say not to copy personal instructions. The owner's explicit request authorizes this version-history capture; it does not grant every later agent general permission to export other personal files or conversations.
- Editing a snapshot does not change its deployed source. For an authorized live change, inspect current dirt/ownership, preserve a backup, update the intended source, verify it and then refresh the corresponding snapshot. Never overwrite a newer deployed file blindly from a stale snapshot.
- Keep stable snapshot paths and let Git record history; update the manifest and describe which sources changed. Preserve genuine per-host/project differences rather than forcing byte-identical instructions.
- Do not automatically install this directory as a runtime instruction hierarchy. Choose the appropriate source guide and merge/adapt it deliberately; use the example when a portable starting point is more appropriate.
- Authentication, tokens, `.env` contents, conversations and private keys remain excluded. Check both file contents and repository visibility before publishing future captures. Public publication is a separate decision from local history and team reuse.

## Current publication state

On 2026-10-23, the owner explicitly authorized publishing these exact host/project snapshots as-is in this public repository after reviewing the visibility and disclosure concerns. Repository visibility remains public. This authorization covers this capture; future captures still require review of their contents and intended audience.
