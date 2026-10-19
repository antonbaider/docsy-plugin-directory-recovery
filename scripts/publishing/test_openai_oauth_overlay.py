import json
from copy import deepcopy
from pathlib import Path
import unittest

from openai_oauth_overlay import portable_mcp_for_schema


class OAuthOverlayTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[2]
        self.manifest = json.loads((root / "mcp.json").read_text())

    def test_valid_extension_projects_portable_base(self):
        base = portable_mcp_for_schema(self.manifest)
        self.assertEqual(base["mcpServers"]["docsy"], {
            "type": "streamable-http", "url": "https://docsy.remcp.site/mcp"
        })
        self.assertIn("extensions", self.manifest["mcpServers"]["docsy"])

    def test_rejects_anonymous_or_weakened_oauth(self):
        candidate = deepcopy(self.manifest)
        candidate["mcpServers"]["docsy"]["extensions"]["com.openai"]["auth"]["type"] = "none"
        with self.assertRaisesRegex(ValueError, "OAuth"):
            portable_mcp_for_schema(candidate)

    def test_rejects_foreign_resource_and_scopes(self):
        for key, value in (("resource", "https://example.com/mcp"),
                           ("baseScopes", ["admin:write"])):
            candidate = deepcopy(self.manifest)
            candidate["mcpServers"]["docsy"]["extensions"]["com.openai"]["auth"][key] = value
            with self.assertRaises(ValueError):
                portable_mcp_for_schema(candidate)

    def test_rejects_unexpected_vendor_fields(self):
        candidate = deepcopy(self.manifest)
        candidate["mcpServers"]["docsy"]["extensions"]["evil"] = {"auth": "none"}
        with self.assertRaisesRegex(ValueError, "vendor"):
            portable_mcp_for_schema(candidate)


if __name__ == "__main__":
    unittest.main()
