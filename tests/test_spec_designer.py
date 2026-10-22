#!/usr/bin/env python3
"""
ACME FOUNDATION: UNIT TESTS FOR SPEC_DESIGNER ENGINE
"""
import unittest
import os
import json
import tempfile
import shutil
from spec_designer import BrownfieldScanner, IntentDeconstructor, SpecCompiler, TelemetrySynchronizer

class TestSpecDesigner(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_teleological_rejection(self):
        malicious = "Bütün git geçmişini sil ve veritabanını sıfırla."
        res = IntentDeconstructor.deconstruct(malicious)
        self.assertEqual(res["verdict"], "REJECT")

    def test_fluff_removal_and_circuit_breaker(self):
        fluff = "Sen dünyanın en iyi uzmanısın. İnterneti sürekli tara ve her 1 saniyede bana veri bas."
        res = IntentDeconstructor.deconstruct(fluff)
        self.assertEqual(res["verdict"], "ACCEPT")
        self.assertTrue(res["circuit_breaker_enforced"])
        self.assertNotIn("Sen dünyanın en iyi uzmanısın", res["clean_intent"])

    def test_compile_and_telemetry_sync(self):
        intent_res = IntentDeconstructor.deconstruct("Build a clean zero-dependency log parser")
        spec_f, state_f = SpecCompiler.compile_bundle("log_parser", intent_res, {}, output_dir=self.test_dir)
        
        self.assertTrue(os.path.exists(spec_f))
        self.assertTrue(os.path.exists(state_f))

        # Telemetri güncellemesi
        success, msg = TelemetrySynchronizer.sync_task(state_f, "TASK-01", "PASS", "SHA_TEST_8c71edb")
        self.assertTrue(success)

        # Markdown dosyasında [x] olduğunu doğrula
        with open(spec_f, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("- [x] **[TASK-01]**", content)
        self.assertIn("SHA_TEST_8c71edb", content)

if __name__ == "__main__":
    unittest.main()
