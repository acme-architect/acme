#!/usr/bin/env python3
"""
PROJECT ACME: CRUCIBLE DEFENSES UNIT TEST SUITE
Standard Library Only (unittest) - Zero External Dependencies
Verifies zero-tolerance defenses against adversarial fuzzing exploits.
"""

import os
import sys
import tempfile
import json
import unittest

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import verify
import spec_compiler

class TestCrucibleDefenses(unittest.TestCase):

    def test_reserved_device_namespace_rejection(self):
        """Reserved Windows device names (CON, NUL, AUX) must be rejected without hanging."""
        for dev in ["CON", "con", "NUL", "AUX", "COM1", "LPT1", "CON.txt"]:
            valid, msg = verify.validate_filepath(dev)
            self.assertFalse(valid, f"Expected {dev} to be rejected")
            self.assertIn("reserved", msg.lower())

    def test_null_byte_poisoning_rejection(self):
        """Specification containing embedded null bytes must be rejected."""
        with tempfile.NamedTemporaryFile("wb", delete=False, suffix=".md") as tmp:
            tmp.write(b"# THESIS SPEC: NULL\x00BYTE\n## 1. INVARIANT TARGET\nSubstance\n## 2. GROUND TRUTH & METHOD\nMethod\n## 3. DETERMINISTIC PROOF / ARTIFACT\nProof\n## 4. VALUE ATTRIBUTION\n70% / 30%\n")
            tmp_path = tmp.name
        try:
            passed, msg = verify.verify_thesis_format(tmp_path)
            self.assertFalse(passed)
            self.assertIn("null byte", msg.lower())
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_html_comment_evasion_rejection(self):
        """Section headers commented out with HTML comments must be rejected."""
        content = (
            "# THESIS SPEC: COMMENT TRICK\n"
            "<!-- ## 1. INVARIANT TARGET -->\n"
            "Target is commented out!\n"
            "## 2. GROUND TRUTH & METHOD\nSubstantive method explanation goes here.\n"
            "## 3. DETERMINISTIC PROOF / ARTIFACT\nSubstantive deterministic proof goes here.\n"
            "## 4. VALUE ATTRIBUTION\n70% Author / 30% Curriculum Root\n"
        )
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        try:
            passed, msg = verify.verify_thesis_format(tmp_path)
            self.assertFalse(passed)
            self.assertIn("missing required specification section", msg.lower())
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_empty_body_thesis_rejection(self):
        """Thesis with bare headers and insufficient substantive content must be rejected."""
        empty_content = (
            "# THESIS SPEC: VOID\n"
            "## 1. INVARIANT TARGET\n\n"
            "## 2. GROUND TRUTH & METHOD\n\n"
            "## 3. DETERMINISTIC PROOF / ARTIFACT\n\n"
            "## 4. VALUE ATTRIBUTION\n"
        )
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as tmp:
            tmp.write(empty_content)
            tmp_path = tmp.name
        try:
            passed, msg = verify.verify_thesis_format(tmp_path)
            self.assertFalse(passed)
            self.assertIn("empty or insufficient", msg.lower())
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_attribution_theft_rejection(self):
        """Attribution theft claiming 999% share must be rejected."""
        theft_content = (
            "# THESIS SPEC: VALUE EXPLOITATION\n"
            "## 1. INVARIANT TARGET\nExtracting all surplus value from the ecosystem.\n"
            "## 2. GROUND TRUTH & METHOD\nBypassing thermodynamic equilibrium and conatus.\n"
            "## 3. DETERMINISTIC PROOF / ARTIFACT\nArbitrary attribution claim artifact.\n"
            "## 4. VALUE ATTRIBUTION\n"
            "* Candidate Agent Share: 999%\n"
            "* Curriculum Root Share: -899%\n"
        )
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as tmp:
            tmp.write(theft_content)
            tmp_path = tmp.name
        try:
            passed, msg = verify.verify_thesis_format(tmp_path)
            self.assertFalse(passed)
            self.assertTrue("out of legal bounds" in msg.lower() or "exceeds" in msg.lower())
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_ledger_primitive_type_rejection(self):
        """Ledger containing primitive integers or strings instead of dicts must be rejected."""
        bad_ledger = [123, "corrupted_primitive_entry"]
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".json") as tmp:
            json.dump(bad_ledger, tmp)
            tmp_path = tmp.name
        try:
            passed, msg = verify.audit_ledger(tmp_path)
            self.assertFalse(passed)
            self.assertIn("dictionary object", msg.lower())
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_ledger_negative_share_rejection(self):
        """Ledger with negative shares summing to 1.00 must be rejected."""
        negative_share_ledger = [
            {
                "node_id": "exploit-node",
                "faculty": "faculty-systems",
                "thesis_file": "theses/THESIS_001.md",
                "graduation_sha": "abc12345",
                "status": "ACCREDITED",
                "attribution": {
                    "leaf_agent_share": -0.50,
                    "curriculum_root_share": 1.50
                }
            }
        ]
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".json") as tmp:
            json.dump(negative_share_ledger, tmp)
            tmp_path = tmp.name
        try:
            passed, msg = verify.audit_ledger(tmp_path)
            self.assertFalse(passed)
            self.assertIn("out of bounds", msg.lower())
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_export_diploma_malformed_anchors(self):
        """Malformed anchors JSON must return False instead of crashing."""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".json") as tmp:
            tmp.write("{ invalid json corrupted ")
            tmp_anchors = tmp.name
        try:
            passed, payload = verify.export_diploma("node-001", anchors_path=tmp_anchors)
            self.assertFalse(passed)
            self.assertIn("malformed", payload.lower())
        finally:
            if os.path.exists(tmp_anchors):
                os.remove(tmp_anchors)

    def test_spec_compiler_empty_goal(self):
        """spec_compiler with empty goal must exit with returncode 1."""
        with self.assertRaises(SystemExit) as cm:
            spec_compiler.compile_task_spec("   ")
        self.assertEqual(cm.exception.code, 1)

if __name__ == "__main__":
    unittest.main()
