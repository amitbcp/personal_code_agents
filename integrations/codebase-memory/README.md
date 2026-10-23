# Optional Codebase Memory integration

CBM is a separately installed native MCP server. This directory records the Mac's existing integration procedures and three read-only graph-agent profiles so the extra local setup is visible and reusable; it does not bundle the native executable, a daemon, graph databases or caches.

## Captured files

- [skill/SKILL.md](skill/SKILL.md): exact installed procedure snapshot.
- [agents/codebase-memory.toml](agents/codebase-memory.toml): ordinary Tier 2 verification.
- [agents/codebase-memory-scout.toml](agents/codebase-memory-scout.toml): provisional Tier 1 lookup.
- [agents/codebase-memory-auditor.toml](agents/codebase-memory-auditor.toml): bounded Tier 3 audit.

These optional agents intentionally use read-only operation. They are separate from this library's five write-enabled specialists and do not override the owner's execution-agent policy. Their captured MCP command names an existing Mac user's absolute binary path; adapt it to the teammate's actual installation before copying a profile. Preserve the correct tool profile/allowlist and confirm current config compatibility.

## Install and verify separately

- Follow the [official CBM installation documentation](https://github.com/DeusData/codebase-memory-mcp) for the target OS/CPU and inspect its current config changes before running an installer. The operator's verified deployment was 0.12.1 on 2026-10-23; this is a dated observation, not a promise of the latest version.
- Verify `codebase-memory-mcp --version`, actual MCP discovery and the intended cache/runtime directory on the new laptop. Never copy another user's authentication or live SQLite files to reproduce the integration.
- Upstream installation may already register a skill or graph agents. Inspect what it installed before copying these optional snapshots; do not create duplicate same-named definitions in different scanned locations.
- The captured skill's “15 MCP Tools” table predates the verified 0.12.1 live 17-tool catalog. It is retained unchanged as a procedure snapshot, not a current API reference; inspect live schemas and current upstream documentation for tools such as `get_file_outline` and `compare_graphs`.
- Index only the authorized project roots. Verify status, path coverage and source fallback; automatic indexing/watch settings are independent choices. Git-ignored-only documentation can require explicit refresh.

## Attribution

CBM upstream is [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), MIT licensed; its license is retained as [LICENSE.upstream](LICENSE.upstream). The graph-agent profiles record the operator's local configuration. No official/system or proprietary plugin bundle is copied here. These optional integration snapshots are outside the seventeen-skill/five-agent deployment-parity count.
