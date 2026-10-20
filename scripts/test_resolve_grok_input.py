#!/usr/bin/env python3
"""Tests for resolve_grok_input.py — no network, no API key."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import resolve_grok_input as r


class ResolveGrokInputTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.characters = r.load_characters()
        cls.slugs = {c["slug"] for c in cls.characters}

    def test_roster_size(self):
        self.assertGreaterEqual(len(self.characters), 18)
        self.assertIn("green-eyed-woman", self.slugs)
        self.assertIn("new-forest-spunk", self.slugs)
        self.assertIn("kate-hampshire", self.slugs)

    def test_kate_by_name(self):
        result = r.resolve("kate")
        self.assertTrue(result["ok"])
        grok = result["grok_return"]
        self.assertEqual(grok["slug"], "kate-hampshire")
        self.assertIn("04sDh", grok["frame_ids"])
        self.assertTrue(grok["bible"].startswith("# Character Bible"))
        self.assertTrue(grok["imagine_tags"])
        self.assertTrue(grok["skills"])

    def test_slug_path(self):
        result = r.resolve("characters/clare-hampshire/")
        self.assertTrue(result["ok"])
        self.assertEqual(result["grok_return"]["slug"], "clare-hampshire")
        self.assertIn("LlvFU", result["grok_return"]["frame_ids"])

    def test_frame_id(self):
        result = r.resolve("LlvFU")
        self.assertTrue(result["ok"])
        self.assertEqual(result["grok_return"]["matched_on"], "frame_id")
        self.assertEqual(result["grok_return"]["slug"], "clare-hampshire")

    def test_uuid_and_at_tag(self):
        uid = "ff0116d1-7647-49a9-a4a1-7c05b5e80c7f"
        for query in (uid, f"@{uid}", f"https://grok.com/imagine/post/{uid}?source=copy_link"):
            with self.subTest(query=query):
                result = r.resolve(query)
                self.assertTrue(result["ok"], result)
                grok = result["grok_return"]
                self.assertEqual(grok["slug"], "green-eyed-woman")
                self.assertIn(uid, grok["uuids"])
                self.assertIn(f"@{uid}", grok["imagine_tags"])

    def test_skill_url(self):
        result = r.resolve("https://grok.com/imagine?skill=imagine-restyle")
        self.assertTrue(result["ok"])
        grok = result["grok_return"]
        self.assertEqual(grok["kind"], "skill")
        self.assertEqual(grok["name"], "imagine-restyle")
        self.assertIn("skills/imagine-restyle/SKILL.md", grok["path"])

    def test_unresolved(self):
        result = r.resolve("not-a-real-character-xyz")
        self.assertFalse(result["ok"])
        self.assertEqual(result["grok_return"]["kind"], "unresolved")
        self.assertTrue(result["suggestions"])

    def test_video_intent_uses_toolkit(self):
        result = r.resolve("kate", intent="video")
        names = [s["name"] for s in result["grok_return"]["skills"]]
        self.assertIn("grok-imagine", names)

    def test_catalog_roundtrip(self):
        payload = r.catalog_payload()
        self.assertEqual(payload["version"], 1)
        self.assertEqual(len(payload["characters"]), len(self.characters))
        self.assertTrue(payload["skills"])
        json.dumps(payload)

    def test_cli_json(self):
        from io import StringIO
        buf = StringIO()
        old = sys.stdout
        sys.stdout = buf
        try:
            code = r.main(["kate"])
        finally:
            sys.stdout = old
        self.assertEqual(code, 0)
        data = json.loads(buf.getvalue())
        self.assertEqual(data["grok_return"]["slug"], "kate-hampshire")


if __name__ == "__main__":
    unittest.main()
