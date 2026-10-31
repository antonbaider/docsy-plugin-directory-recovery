<p align="center">
  <img src="assets/docsy-icon-192.png" width="96" height="96" alt="Docsy logo">
</p>

<h1 align="center">Docsy</h1>
<p align="center"><strong>Developer documentation your AI assistant can cite.</strong></p>
<p align="center">Official source links · Library versions · Focused MCP retrieval · Five read-only tools</p>

<p align="center">
  <a href="https://chatgpt.com/plugins/plugin_asdk_app_6ad6814ca7708191956117b3a3b58eb5"><strong>Open Docsy in ChatGPT</strong></a>
  · <a href="#connect-your-ai-client">Connect an MCP client</a>
  · <a href="docs/ACCOUNT-FREE-REVIEW.md">Try the public endpoint</a>
  · <a href="https://docsy.remcp.site/docs">Documentation</a>
</p>

<p align="center">
  <a href="https://github.com/getremcp/docsy-plugin/actions/workflows/plugin-quality.yml"><img alt="Public plugin checks" src="https://img.shields.io/github/actions/workflow/status/getremcp/docsy-plugin/plugin-quality.yml?branch=main&label=checks"></a>
  <a href="https://github.com/getremcp/docsy-plugin/releases/latest"><img alt="Latest stable release" src="https://img.shields.io/github/v/release/getremcp/docsy-plugin?label=stable"></a>
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-222"></a>
</p>

[简体中文](docs/README.zh-CN.md) · [Website](https://docsy.remcp.site) · [Support](https://docsy.remcp.site/support)

---

## Why Docsy?

Coding assistants can mix documentation from different versions or give answers without a checkable source. Docsy helps them resolve the right library, find version-specific documentation and return links to the original publisher files or pages.

- **Version-aware:** ask for a specific release and see which versions are indexed; upstream tags alone do not imply indexed documentation.
- **Source-linked:** excerpts include origin URLs and, when available, a pinned Git revision.
- **Focused:** retrieve the relevant passage or request links without loading an entire manual.
- **Read-only:** no local shell execution, file writes or access to your private repositories.

### MCP tools

| Tool | Use it for |
| --- | --- |
| `resolve-library-id` | Match a framework, package or SDK name to its documentation ID |
| `list-library-versions` | Discover available versions and indexed status |
| `query-docs` | Get focused excerpts or source links for a chosen library/version |
| `search` | Search the public documentation index |
| `fetch` | Read a returned result by ID or a verified publisher page |

For example, ask: **“Using official React documentation, explain `useEffect` cleanup and cite the original source.”**

## Use Docsy in ChatGPT

**[Open the Docsy ChatGPT plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ad6814ca7708191956117b3a3b58eb5).**

This is the publisher-provided ChatGPT plugin link. Availability and sign-in depend on your ChatGPT account and client. A direct URL is not evidence of an independently verified public marketplace approval.

## Connect your AI client

Two **separate** hosted MCP endpoints serve different use cases:

| Endpoint | Access | Purpose |
| --- | --- | --- |
| `https://docsy.remcp.site/mcp/registry` | OAuth 2.1 | Canonical account-linked MCP connection |
| `https://docsy.remcp.site/mcp/public` | No Docsy account or API key | Rate-limited evaluation against **public** documentation |

Both expose the five read-only tools. The public endpoint does **not** make private libraries, account data or arbitrary web URLs accessible. On 31 October 2026, anonymous `initialize`, `tools/list`, `resolve-library-id` and `query-docs` passed a live MCP protocol smoke test; the canonical endpoint still returned HTTP 401 without OAuth. This is **not** a claim of a completed Codex CLI agent test.

**Claude Code — canonical OAuth endpoint**

```sh
claude mcp add --transport http docsy https://docsy.remcp.site/mcp/registry
```

**Codex CLI — canonical OAuth endpoint**

```sh
codex mcp add docsy --url https://docsy.remcp.site/mcp/registry
codex mcp login docsy
```

**Cursor, VS Code and other remote MCP clients** — configure a Streamable HTTP connection to the canonical URL:

```json
{
  "mcpServers": {
    "docsy": {
      "type": "http",
      "url": "https://docsy.remcp.site/mcp/registry"
    }
  }
}
```

For account-free evaluation and protocol-level commands, see [Public MCP evaluation](docs/ACCOUNT-FREE-REVIEW.md). Some clients initiate OAuth discovery on their own even for an anonymous endpoint; client-specific behavior must be verified separately.

More guides: [Getting started](docs/GETTING-STARTED.md) · [Client integrations](docs/CLIENT-INTEGRATIONS.md) · [Claude Code community plugin manifest](.claude-plugin/marketplace.json).

## Where Docsy is available

These are **distinct distribution channels**, not interchangeable approval statuses. Records below were checked on **31 October 2026** unless noted.

| Channel | Verified record |
| --- | --- |
| [ChatGPT plugin](https://chatgpt.com/plugins/plugin_asdk_app_6ad6814ca7708191956117b3a3b58eb5) | Publisher-provided direct link; anonymous verification is blocked by ChatGPT (HTTP 403) |
| [Official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.getremcp%2Fdocsy/versions/latest) | `io.github.getremcp/docsy` v1.0.9, canonical OAuth endpoint |
| [GitHub plugin releases](https://github.com/getremcp/docsy-plugin/releases) | Stable `plugin-v1.0.9`; `plugin-v1.0.10` is a **prerelease review candidate** |
| [Glama](https://glama.ai/mcp/connectors/io.github.getremcp/docsy) | Public connector page accessible |
| npm [SDK](https://www.npmjs.com/package/@remcp/docsy-sdk) / [CLI](https://www.npmjs.com/package/@remcp/docsy-cli) | Published `@remcp/docsy-sdk` v0.1.2 / `@remcp/docsy-cli` v0.1.4 |
| [AI Anytime](https://github.com/AIAnytime/Awesome-MCP-Servers/pull/313) / [TensorBlock](https://github.com/TensorBlock/awesome-mcp-servers/pull/4485) / [Sagargupta](https://github.com/Sagargupta16/awesome-mcp-servers/pull/212) | Three independent GitHub directory pull requests confirmed **merged** |
| [Claude Code community marketplace](.claude-plugin/marketplace.json) | Installable GitHub manifest; **not** official Anthropic marketplace approval |

See [Distribution status and review queue](docs/DISTRIBUTION-STATUS.md) for other directories, pending applications and the Smithery transition. The [awesome-codex submission #33](https://github.com/ichangyou/awesome-codex/pull/33) was **closed without merging**; a new submission must wait for a recorded firsthand Codex invocation.

## Releases, scope and security

This repository is the **public integration and distribution package**, not the hosted Docsy backend. It intentionally includes plugin manifests, client settings, read-only skill metadata, reviewed documentation and brand assets; it does **not** include crawlers, database contents, deployment secrets or a local server implementation.

- Use the [stable GitHub release](https://github.com/getremcp/docsy-plugin/releases/latest) for downloadable plugin assets; don't assume prereleases are approved marketplace versions.
- The canonical endpoint uses OAuth 2.1; the public evaluator has its own rate limits and public-corpus boundaries.
- Never include credentials, personal information or proprietary code in documentation queries or public security reports.
- For a vulnerability or potential exposure, follow [SECURITY.md](SECURITY.md), not a public issue containing sensitive details.

[SDK & CLI repository](https://github.com/getremcp/docsy) · [Privacy](https://docsy.remcp.site/privacy) · [Terms](https://docsy.remcp.site/terms) · [Support](https://docsy.remcp.site/support) · [MIT License](LICENSE)

<p align="center"><sub>Docsy is an independent documentation service. External directory listings do not imply endorsement by their platform owners.</sub></p>
