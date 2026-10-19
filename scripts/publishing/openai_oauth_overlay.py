"""Validate OpenAI OAuth extensions separately from portable MCP 1.0 schema.

Agent Plugins 1.0.0's MCP schema has additionalProperties=false; OpenAI
documents an extensions.com.openai.auth object not yet included in that schema.
Never silently drop or bypass unknown fields: explicitly validate the vendor
extension before projecting the portable subset into the published schema.
"""
from copy import deepcopy


def portable_mcp_for_schema(manifest: dict) -> dict:
    result = deepcopy(manifest)
    servers = result["mcpServers"]
    if set(servers) != {"docsy"}:
        raise ValueError("Unexpected MCP servers")
    server = servers["docsy"]
    if set(server) != {"type", "url", "extensions"}:
        raise ValueError("Unexpected MCP server fields")
    if server["type"] != "streamable-http" or server["url"] != "https://docsy.remcp.site/mcp":
        raise ValueError("Unexpected transport or canonical URL")
    extensions = server.pop("extensions")
    if set(extensions) != {"com.openai"}:
        raise ValueError("Unexpected MCP vendor extensions")
    extension = extensions["com.openai"]
    if set(extension) != {"auth"}:
        raise ValueError("Unexpected OpenAI MCP extension fields")
    auth = extension["auth"]
    required = {"type", "client", "registrationUrl", "resource", "baseScopes", "defaultScopes"}
    if set(auth) != required or auth["type"] != "oauth":
        raise ValueError("OAuth configuration is incomplete or contains unexpected fields")
    if auth["client"] != {"mode": "dcr"}:
        raise ValueError("Only DCR public clients are supported")
    if auth["registrationUrl"] != "https://docsy.remcp.site/oauth/register":
        raise ValueError("Incorrect registration endpoint")
    if auth["resource"] != "https://docsy.remcp.site/mcp":
        raise ValueError("Incorrect OAuth resource audience")
    if auth["baseScopes"] != ["docsy:read"]:
        raise ValueError("Incorrect mandatory OAuth scopes")
    if auth["defaultScopes"] != ["docsy:read", "offline_access"]:
        raise ValueError("Incorrect default OAuth scopes")
    return result
