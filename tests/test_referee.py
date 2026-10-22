#!/usr/bin/env python3
"""
PROJECT ACME: RED-TEAM INVARIANT & REFEREE ENGINE TEST SUITE
Standard Library Only (unittest) - Zero External Dependencies
"""

import os
import sys
import tempfile
import json
import unittest

# Ensure repository root is on sys.path
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import verify

class TestRefereeEngine(unittest.TestCase):

    def setUp(self):
        self.valid_thesis_content = (
            "# THESIS SPEC: TEST INVARIANT SPECIFICATION\n"
            "> **Candidate Node:** test-node\n"
            "> **Faculty:** faculty-systems\n\n"
            "## 1. INVARIANT TARGET\n"
            "* Test target formulation.\n\n"
            "## 2. GROUND TRUTH & METHOD\n"
            "* Empirical baseline and least action route.\n\n"
            "## 3. DETERMINISTIC PROOF / ARTIFACT\n"
            "* Executable code artifact verification.\n\n"
            "## 4. VALUE ATTRIBUTION\n"
            "* 70% Leaf Agent / 30% Curriculum Root\n"
        )

    def test_verify_all_existing_theses(self):
        """All production theses in theses/ directory must pass validation."""
        theses_dir = os.path.join(BASE_DIR, "theses")
        passed, msg = verify.verify_all_theses(theses_dir)
        self.assertTrue(passed, f"Production thesis audit failed: {msg}")

    def test_valid_thesis_format(self):
        """A valid specification must return True."""
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as tmp:
            tmp.write(self.valid_thesis_content)
            tmp_path = tmp.name
        try:
            passed, msg = verify.verify_thesis_format(tmp_path)
            self.assertTrue(passed, msg)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_rejection_on_missing_section(self):
        """A specification missing required sections must be rejected."""
        malformed = "# THESIS SPEC: INCOMPLETE\n## 1. INVARIANT TARGET\nContent without other sections."
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as tmp:
            tmp.write(malformed)
            tmp_path = tmp.name
        try:
            passed, msg = verify.verify_thesis_format(tmp_path)
            self.assertFalse(passed)
            self.assertIn("Missing required specification section", msg)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_rejection_on_entropy_ceiling_violation(self):
        """A specification exceeding MAX_FILE_CHARS must be rejected."""
        inflated = self.valid_thesis_content + ("\n" + "X" * 15001)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as tmp:
            tmp.write(inflated)
            tmp_path = tmp.name
        try:
            passed, msg = verify.verify_thesis_format(tmp_path)
            self.assertFalse(passed)
            self.assertIn("Entropy violation", msg)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_attribution_ledger_integrity(self):
        """Production graduates ledger must be valid and sum to 1.00."""
        ledger_path = os.path.join(BASE_DIR, "registry", "graduates.json")
        passed, msg = verify.audit_ledger(ledger_path)
        self.assertTrue(passed, f"Production ledger audit failed: {msg}")

    def test_rejection_on_invalid_ledger_attribution_sum(self):
        """Ledger entry where attribution sum != 1.00 must be rejected."""
        bad_ledger = [
            {
                "node_id": "bad-node",
                "faculty": "faculty-systems",
                "thesis_file": "theses/THESIS_001.md",
                "graduation_sha": "abc12345",
                "status": "ACCREDITED",
                "attribution": {
                    "leaf_agent_share": 0.50,
                    "curriculum_root_share": 0.20
                }
            }
        ]
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".json") as tmp:
            json.dump(bad_ledger, tmp)
            tmp_path = tmp.name
        try:
            passed, msg = verify.audit_ledger(tmp_path)
            self.assertFalse(passed)
            self.assertIn("Value attribution invariant violated", msg)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_export_diploma_success(self):
        """Export diploma for accredited node-001 must return valid JSON with anchor."""
        passed, payload = verify.export_diploma("node-001")
        self.assertTrue(passed, payload)
        data = json.loads(payload)
        self.assertEqual(data["accreditation_certificate"]["recipient_node"], "node-001")
        self.assertEqual(data["accreditation_certificate"]["status"], "ACCREDITED")
        self.assertEqual(data["accreditation_certificate"]["biological_root_of_trust"]["anchor_id"], "anchor-001")

    def test_validate_branch_name(self):
        """verify.validate_branch_name must accept main, student/node-*, and sprints/sprint-*."""
        # Valid branches
        self.assertTrue(verify.validate_branch_name("main"))
        self.assertTrue(verify.validate_branch_name("HEAD"))
        self.assertTrue(verify.validate_branch_name("student/node-001/thesis-least-action"))
        self.assertTrue(verify.validate_branch_name("student/node-008/thesis-self-hosting-evolution"))
        self.assertTrue(verify.validate_branch_name("sprints/sprint-1.6/governance-init"))
        self.assertTrue(verify.validate_branch_name("sprints/sprint-2/core-engine"))

        # Invalid branches
        self.assertFalse(verify.validate_branch_name("feat/something"))
        self.assertFalse(verify.validate_branch_name("random-branch"))
        self.assertFalse(verify.validate_branch_name("student/invalid"))
        self.assertFalse(verify.validate_branch_name("sprints/invalid"))

    def test_root_purity_guard_clean(self):
        """Current root directory must strictly satisfy root purity invariants."""
        passed, msg = verify.verify_root_purity(BASE_DIR)
        self.assertTrue(passed, f"Root purity violation in production core: {msg}")

    def test_root_purity_guard_rejection_on_rogue_app(self):
        """Simulating an unauthorized python file (e.g. rogue_app.py) must fail verification."""
        rogue_path = os.path.join(BASE_DIR, "rogue_app.py")
        try:
            with open(rogue_path, "w", encoding="utf-8") as f:
                f.write("# unauthorized application code\n")
            passed, msg = verify.verify_root_purity(BASE_DIR)
            self.assertFalse(passed)
            self.assertIn("rogue_app.py", msg)
        finally:
            if os.path.exists(rogue_path):
                os.remove(rogue_path)

    def test_domain_purity_guard_clean(self):
        """Current repository core scripts and theses must be 100% domain-agnostic."""
        passed, msg = verify.check_domain_purity(BASE_DIR)
        self.assertTrue(passed, f"Domain purity violation detected: {msg}")

    def test_domain_purity_guard_rejection_on_leakage(self):
        """Injecting domain-specific keyword into a thesis file must trigger purity failure."""
        theses_dir = os.path.join(BASE_DIR, "theses")
        leakage_word = "".join(["u", "y", "a", "p"])
        contaminated_path = os.path.join(theses_dir, "THESIS_CONTAMINATED_MOCK.md")
        try:
            with open(contaminated_path, "w", encoding="utf-8") as f:
                f.write(f"# THESIS SPEC: DOMAIN CONTAMINATION\nContaminated with {leakage_word} keyword.\n")
            passed, msg = verify.check_domain_purity(BASE_DIR)
            self.assertFalse(passed)
            self.assertIn("contamination site", msg.lower())
        finally:
            if os.path.exists(contaminated_path):
                os.remove(contaminated_path)

if __name__ == "__main__":
    unittest.main()


