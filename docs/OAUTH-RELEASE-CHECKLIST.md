# Docsy v1.0.10 OAuth publication gate

**Status: candidate, not released.** The public v1.0.9 release is still active.

1. Merge and deploy backend OAuth PR #281 in a migration-safe mode.
2. Configure /mcp OAuth and verify OAuth discovery, DCR, PKCE, refresh, revocation, and all five actual tool calls, including 401 without bearer.
3. Confirm `/mcp/registry` is subject to the same authentication boundary (it proxies /mcp at edge).
4. Record a new real OAuth + Docsy tool demo and attach the file at `plugin-v1.0.10`; verify HTTP 200, MIME and duration.
5. Build and verify the signed-off six-file plugin ZIP, ensure approved Brand Kit image SHA-256 checks pass.
6. From the **original** OpenAI App in the publisher account, replace the in-review old submission only after the new OAuth submission is ready; never create a second public App or change the original MCP binding.
7. Submit OAuth review with five positive / three negative cases, domain verification, privacy, support and terms.
8. Enable mandatory OAuth on /mcp only after coordinated client migration. Confirm end-to-end ChatGPT, Codex, mobile.
9. Publish and verify public listing only after OpenAI approval. Do not mistake a draft or review for publication.

A DCR-enabled manifest is public metadata; no tokens, API keys or user email addresses may be included in package.
