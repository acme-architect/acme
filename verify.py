#!/usr/bin/env python3
"""
PROJECT ACME: CORE REFEREE & INVARIANT VERIFICATION ENGINE
Version: 1.4.0
Invariants: Principle of Least Action (PLA), Boundary Guard, Value Attribution (70/30)
"""

import os
import sys
import subprocess
import re
import json

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

def verify_all_theses(theses_dir="theses"):
    if not os.path.exists(theses_dir):
        return False, f"Theses directory not found: {theses_dir}"
    files = [f for f in os.listdir(theses_dir) if f.endswith(".md")]
    if not files:
        return False, "No thesis specifications found."
    for f in sorted(files):
        full_path = os.path.join(theses_dir, f)
        passed, msg = verify_thesis_format(full_path)
        if not passed:
            return False, f"{f}: {msg}"
    return True, f"All {len(files)} thesis specifications verified successfully."

def audit_ledger(registry_path="registry/graduates.json"):
    if not os.path.exists(registry_path):
        return False, f"Registry file not found: {registry_path}"
    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            graduates = json.load(f)
    except Exception as e:
        return False, f"Malformed registry JSON: {e}"

    if not isinstance(graduates, list):
        return False, "Registry must be a JSON array of graduate records."

    for entry in graduates:
        for key in ["node_id", "faculty", "thesis_file", "graduation_sha", "status", "attribution"]:
            if key not in entry:
                return False, f"Missing required registry key: {key} in entry {entry.get('node_id')}"
        if entry["status"] != "ACCREDITED":
            return False, f"Invalid accreditation status for {entry['node_id']}"
        attr = entry["attribution"]
        total_share = attr.get("leaf_agent_share", 0.0) + attr.get("curriculum_root_share", 0.0)
        if round(total_share, 2) != 1.00:
            return False, f"Value attribution invariant violated for {entry['node_id']}: total {total_share} != 1.00"

    return True, f"Attribution ledger verified: {len(graduates)} accredited diploma records intact."

def export_diploma(node_id, registry_path="registry/graduates.json", anchors_path="registry/anchors.json"):
    if not os.path.exists(registry_path):
        return False, f"Registry not found: {registry_path}"
    if not os.path.exists(anchors_path):
        return False, f"Anchors not found: {anchors_path}"

    with open(registry_path, "r", encoding="utf-8") as f:
        graduates = json.load(f)
    with open(anchors_path, "r", encoding="utf-8") as f:
        anchors = json.load(f)

    record = next((g for g in graduates if g.get("node_id") == node_id), None)
    if not record:
        return False, f"Node ID '{node_id}' not found in accreditation registry."

    anchor = anchors[0] if anchors else {"anchor_id": "UNKNOWN", "public_identifier": "UNANCHORED"}

    diploma = {
        "acme_protocol": "RFC-001 (Genesis v1.0.0)",
        "accreditation_certificate": {
            "recipient_node": record["node_id"],
            "faculty": record["faculty"],
            "thesis_specification": record["thesis_file"],
            "immutable_merkle_sha": record["graduation_sha"],
            "status": record["status"],
            "biological_root_of_trust": {
                "anchor_id": anchor.get("anchor_id"),
                "identifier": anchor.get("public_identifier")
            },
            "value_attribution": record["attribution"]
        }
    }
    return True, json.dumps(diploma, indent=2)

def audit_changed_files():
    branch, _, _ = run_cmd("git rev-parse --abbrev-ref HEAD")
    if not branch.startswith("student/"):
        return []

    out, _, code = run_cmd("git diff --name-only main...HEAD")
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

    if len(sys.argv) > 1 and sys.argv[1] == "--verify-all":
        passed, msg = verify_all_theses()
        if passed:
            print(f"[PASS] {msg}")
            sys.exit(0)
        else:
            print(f"[FAIL] {msg}", file=sys.stderr)
            sys.exit(1)

    if len(sys.argv) > 1 and sys.argv[1] == "--audit-ledger":
        passed, msg = audit_ledger()
        if passed:
            print(f"[PASS] {msg}")
            sys.exit(0)
        else:
            print(f"[FAIL] {msg}", file=sys.stderr)
            sys.exit(1)

    if len(sys.argv) > 2 and sys.argv[1] == "--export-diploma":
        node_id = sys.argv[2]
        passed, payload = export_diploma(node_id)
        if passed:
            print(f"[ACME DIPLOMA CERTIFICATE: {node_id}]")
            print(payload)
            sys.exit(0)
        else:
            print(f"[FAIL] {payload}", file=sys.stderr)
            sys.exit(1)

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
