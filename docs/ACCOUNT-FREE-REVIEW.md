# Account-free Docsy MCP evaluation for Codex

> Publication gate: do not advertise this route as working until the backend
> and edge rollout of [docsy-full PR #851](https://github.com/antonbaider/docsy-full/pull/851)
> has passed an external anonymous smoke test.

Docsy's canonical, account-linked MCP endpoint remains
`https://docsy.remcp.site/mcp/registry` and requires OAuth 2.1.

The separate **public documentation evaluator** is:

```
https://docsy.remcp.site/mcp/public
```

This evaluator allows limited access to public indexed documentation with no
Docsy account, API key, or OAuth grant. It has exactly five read-only tools:
`resolve-library-id`, `list-library-versions`, `query-docs`, `search`,
and `fetch`. It does not expose the hosted backend source code. The public
plugin repository contains the client integration and distribution metadata;
the hosted backend is maintained separately.

## Run a real Codex evaluation

After confirming anonymous MCP `initialize` and `tools/list` return 200
from the production guest URL:

```sh
codex mcp add docsy-public --url https://docsy.remcp.site/mcp/public
codex mcp list
```

Example question to ask in Codex:

> Use Docsy to resolve React's official documentation and find guidance for
> cleaning up a useEffect subscription. Include the original version-pinned
> source URL.

A real evaluation report should include the exact commands, client version,
source links returned, and whether `query-docs` actually completed. Do not
claim that a suggested prompt is an executed test. Remove the temporary MCP
entry with `codex mcp remove docsy-public` when finished.

## Guest access and security boundaries

- Guest requests are restricted to the public corpus. They are not associated
  with a Docsy account and cannot access private libraries or account policies.
- 20 MCP HTTP requests per minute per IP maximum, with a 128 KiB body limit
  and independent pre-auth throttling.
- Guest tool discovery advertises only `noauth`; the canonical
  `/mcp` and `/mcp/registry` transports still require OAuth.
- The edge does not forward Authorization headers to this guest route.
- It is a public source-linked documentation service, not an unrestricted
  URL fetcher or a tool for running arbitrary commands.

## Directory review status

[awesome-codex PR #33](https://github.com/ichangyou/awesome-codex/pull/33)
was closed on 31 October 2026 because the then-published MCP endpoint
required signup to evaluate, and the submission did not describe firsthand
use. A new catalog submission should happen only after the live account-free
route and an actual Codex tool invocation have been verified. Acceptance is
at the curator's discretion.
