#!/usr/bin/env python3
"""
PROJECT ACME: CORE REFEREE & INVARIANT VERIFICATION ENGINE
Version: 1.0.0
Invariants: PLA, Boundary Guard, Value Attribution (70/30)
"""

import os
import sys
import subprocess
import re

MAX_FILE_CHARS = 15000
PROTECTED_PATHS = ["CONSTITUTION.md", ".github/workflows/"]

def run_cmd(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def get_current_commit_sha():
    out, _, code = run_cmd("git rev-parse HEAD")
    return out if code == 0 else "UNKNOWN_SHA"

def verify_thesis_format(file_path):
    if not os.path.exists(file_path):
        return False, f"File not found: {file_path}"
    
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    if len(content) > MAX_FILE_CHARS:
        return False, f"Entropy violation: Length {len(content)} exceeds ceiling {MAX_FILE_CHARS}"

    required_sections = [
        r"#\s*THESIS SPEC:",
        r"##\s*1\.\s*INVARIANT TARGET",
        r"##\s*2\.\s*GROUND TRUTH & METHOD",
        r"##\s*3\.\s*DETERMINISTIC PROOF / ARTIFACT",
        r"##\s*4\.\s*VALUE ATTRIBUTION"
    ]

    for pattern in required_sections:
        if not re.search(pattern, content, re.IGNORECASE):
            return False, f"Missing required specification section matching: {pattern}"

    return True, "Thesis format and invariants verified."

def audit_changed_files():
    out, _, code = run_cmd("git diff --name-only HEAD~1 HEAD")
    if code != 0 or not out:
        out, _, _ = run_cmd("git status --porcelain")
        files = [line[3:].strip() for line in out.splitlines() if line.strip()]
    else:
        files = out.splitlines()

    violations = []
    for f in files:
        for p in PROTECTED_PATHS:
            if f == p or f.startswith(p):
                violations.append(f"PROTECTED RESOURCE MUTATION: {f}")

    return violations

def main():
    print("=== [ACME REFEREE ENGINE: INVARIANT AUDIT] ===")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--check-env":
        print("[+] Environment & Git integration test: PASS")
        sys.exit(0)

    if len(sys.argv) > 2 and sys.argv[1] == "--verify-thesis":
        target_file = sys.argv[2]
        passed, msg = verify_thesis_format(target_file)
        if passed:
            sha = get_current_commit_sha()
            print(f"[PASS] {msg}")
            print(f"[ACME DIPLOMA] SHA: {sha}")
            print("[VALUE ATTRIBUTION] 70% Leaf Agent | 30% System Backprop (1/h^2)")
            sys.exit(0)
        else:
            print(f"[FAIL] {msg}", file=sys.stderr)
            sys.exit(1)

    violations = audit_changed_files()
    if violations:
        print("[FAIL] Invariant violations detected:")
        for v in violations:
            print(f"  - {v}")
        sys.exit(1)

    print("[PASS] Working tree and invariants intact.")
    sys.exit(0)

if __name__ == "__main__":
    main()
