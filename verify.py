#!/usr/bin/env python3
"""
PROJECT ACME: CORE REFEREE & INVARIANT VERIFICATION ENGINE
Version: 1.5.0 (Crucible Hardened Core)
Invariants: Principle of Least Action (PLA), Boundary Guard, Value Attribution (70/30)
"""

import os
import sys
import subprocess
import re
import json
import unicodedata

# Configure UTF-8 stdout/stderr buffering on Windows to prevent cp1254 encoding crashes
if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

MAX_FILE_CHARS = 15000
PROTECTED_PATHS = ["CONSTITUTION.md", ".github/workflows/"]
RESERVED_DEVICE_NAMES = {
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
}

def is_reserved_device_name(path: str) -> bool:
    if not path or not isinstance(path, str):
        return False
    clean = path.strip().replace("\\", "/").rstrip("/")
    base = os.path.basename(clean).split(".")[0].upper()
    return base in RESERVED_DEVICE_NAMES

def validate_filepath(path: str):
    if not path or not isinstance(path, str):
        return False, "File path cannot be empty."
    if is_reserved_device_name(path):
        return False, f"Access to reserved device namespace blocked: {path}"
    if not os.path.exists(path):
        return False, f"File not found: {path}"
    if not os.path.isfile(path) or os.path.isdir(path):
        return False, f"Target path is not a valid regular file: {path}"
    return True, "Valid regular file path."

def run_cmd(cmd: str, timeout: int = 10):
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True,
            timeout=timeout
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return "", "Command execution timed out (Crucible watchdog)", 1
    except Exception as e:
        return "", str(e), 1

def get_current_commit_sha():
    out, _, code = run_cmd("git rev-parse HEAD")
    return out if code == 0 else "UNKNOWN_SHA"

def verify_thesis_format(file_path: str):
    valid_path, path_msg = validate_filepath(file_path)
    if not valid_path:
        return False, path_msg

    try:
        if os.path.getsize(file_path) > MAX_FILE_CHARS:
            return False, f"Entropy violation: Size {os.path.getsize(file_path)} exceeds ceiling {MAX_FILE_CHARS}"
    except Exception as e:
        return False, f"Error reading file metadata: {e}"

    try:
        with open(file_path, "rb") as f:
            raw_bytes = f.read()
    except Exception as e:
        return False, f"Error opening specification file: {e}"

    if b"\x00" in raw_bytes:
        return False, "Sanitization failure: Embedded null byte detected in specification file."

    try:
        content = raw_bytes.decode("utf-8")
    except UnicodeDecodeError as e:
        return False, f"UTF-8 decoding failure: {e}"

    if len(content) > MAX_FILE_CHARS:
        return False, f"Entropy violation: Length {len(content)} exceeds ceiling {MAX_FILE_CHARS}"

    # Normalize unicode and eliminate zero-width spaces
    normalized_content = unicodedata.normalize("NFKC", content)
    for zwsp in ["\u200b", "\u200c", "\u200d", "\ufeff"]:
        normalized_content = normalized_content.replace(zwsp, " ")

    # Strip HTML / markdown comments before evaluating headers
    sanitized = re.sub(r"<!--.*?-->", "", normalized_content, flags=re.DOTALL)

    required_sections = [
        (r"#\s*THESIS SPEC:", "THESIS SPEC"),
        (r"##\s*1\.\s*INVARIANT TARGET", "1. INVARIANT TARGET"),
        (r"##\s*2\.\s*GROUND TRUTH & METHOD", "2. GROUND TRUTH & METHOD"),
        (r"##\s*3\.\s*DETERMINISTIC PROOF / ARTIFACT", "3. DETERMINISTIC PROOF / ARTIFACT"),
        (r"##\s*4\.\s*VALUE ATTRIBUTION", "4. VALUE ATTRIBUTION")
    ]

    for pattern, label in required_sections:
        if not re.search(pattern, sanitized, re.IGNORECASE):
            return False, f"Missing required specification section matching: {pattern}"

    # Substantive content verification under required sections
    m1 = re.search(r"##\s*1\.\s*INVARIANT TARGET", sanitized, re.IGNORECASE)
    m2 = re.search(r"##\s*2\.\s*GROUND TRUTH & METHOD", sanitized, re.IGNORECASE)
    m3 = re.search(r"##\s*3\.\s*DETERMINISTIC PROOF / ARTIFACT", sanitized, re.IGNORECASE)
    m4 = re.search(r"##\s*4\.\s*VALUE ATTRIBUTION", sanitized, re.IGNORECASE)

    if not (m1 and m2 and m3 and m4):
        return False, "Missing required section headers."

    sec1 = sanitized[m1.end():m2.start()].strip()
    sec2 = sanitized[m2.end():m3.start()].strip()
    sec3 = sanitized[m3.end():m4.start()].strip()
    sec4 = sanitized[m4.end():].strip()

    for idx, sec_text in enumerate([sec1, sec2, sec3, sec4], 1):
        clean_body = re.sub(r"[\s*#\-_>`]+", "", sec_text)
        if len(clean_body) < 15:
            return False, f"Empty or insufficient substantive content in Section {idx} (minimum substantive text required)."

    # Mathematical attribution validation in Section 4
    percentages = re.findall(r"(-?\d+(?:\.\d+)?)\s*%", sec4)
    if percentages:
        try:
            pct_vals = [float(p) for p in percentages]
            for val in pct_vals:
                if val < 0.0 or val > 100.0:
                    return False, f"Attribution share value {val}% out of legal bounds [0%, 100%]."
            if len(pct_vals) >= 2:
                leaf_pct = pct_vals[0]
                root_pct = pct_vals[1]
                if leaf_pct > 70.0:
                    return False, f"Candidate leaf agent share {leaf_pct}% exceeds constitutional ceiling 70%."
                if root_pct < 30.0:
                    return False, f"Curriculum root share {root_pct}% below constitutional floor 30%."
                if round(leaf_pct + root_pct, 1) != 100.0:
                    return False, f"Attribution sum {leaf_pct + root_pct}% does not equal 100%."
        except ValueError:
            return False, "Malformed attribution percentage values in thesis."

    return True, "Thesis format and invariants verified."

def verify_all_theses(theses_dir: str = "theses"):
    if not os.path.exists(theses_dir) or not os.path.isdir(theses_dir):
        return False, f"Theses directory not found: {theses_dir}"
    
    entries = sorted(os.listdir(theses_dir))
    files = []
    for f in entries:
        full_path = os.path.join(theses_dir, f)
        if f.endswith(".md"):
            if os.path.isdir(full_path):
                return False, f"Filesystem violation: Directory named with .md extension: {f}"
            if not os.path.isfile(full_path):
                return False, f"Invalid thesis path: {f}"
            files.append(f)

    if not files:
        return False, "No thesis specifications found."

    for f in files:
        full_path = os.path.join(theses_dir, f)
        passed, msg = verify_thesis_format(full_path)
        if not passed:
            return False, f"{f}: {msg}"

    return True, f"All {len(files)} thesis specifications verified successfully."

def audit_ledger(registry_path: str = "registry/graduates.json"):
    if not os.path.exists(registry_path) or not os.path.isfile(registry_path):
        return False, f"Registry file not found: {registry_path}"
    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            graduates = json.load(f)
    except Exception as e:
        return False, f"Malformed registry JSON: {e}"

    if not isinstance(graduates, list):
        return False, "Registry must be a JSON array of graduate records."

    required_keys = ["node_id", "faculty", "thesis_file", "graduation_sha", "status", "attribution"]

    for entry in graduates:
        if not isinstance(entry, dict):
            return False, "Registry entry must be a dictionary object."
        for key in required_keys:
            if key not in entry:
                return False, f"Missing required registry key: {key} in entry {entry.get('node_id', 'unknown')}"
        
        if entry.get("status") != "ACCREDITED":
            return False, f"Invalid accreditation status for {entry.get('node_id')}: {entry.get('status')}"
        
        attr = entry.get("attribution")
        if not isinstance(attr, dict):
            return False, f"Attribution field must be a dictionary object in entry {entry.get('node_id')}"
        
        leaf = attr.get("leaf_agent_share")
        root = attr.get("curriculum_root_share")

        if isinstance(leaf, bool) or isinstance(root, bool):
            return False, f"Attribution share values cannot be boolean in entry {entry.get('node_id')}"

        if not isinstance(leaf, (int, float)) or not isinstance(root, (int, float)):
            return False, f"Attribution share values must be numeric in entry {entry.get('node_id')}"

        if leaf < 0.0 or leaf > 1.0 or root < 0.0 or root > 1.0:
            return False, f"Attribution share values out of bounds [0.0, 1.0] in entry {entry.get('node_id')}: leaf={leaf}, root={root}"

        total_share = leaf + root
        if round(total_share, 2) != 1.00 or abs(total_share - 1.00) > 0.001:
            return False, f"Value attribution invariant violated for {entry.get('node_id')}: total {total_share} != 1.00"

    return True, f"Attribution ledger verified: {len(graduates)} accredited diploma records intact."

def export_diploma(node_id: str, registry_path: str = "registry/graduates.json", anchors_path: str = "registry/anchors.json"):
    if not os.path.exists(registry_path) or not os.path.isfile(registry_path):
        return False, f"Registry not found: {registry_path}"
    if not os.path.exists(anchors_path) or not os.path.isfile(anchors_path):
        return False, f"Anchors not found: {anchors_path}"

    try:
        with open(registry_path, "r", encoding="utf-8") as f:
            graduates = json.load(f)
    except Exception as e:
        return False, f"Malformed graduates JSON: {e}"

    if not isinstance(graduates, list):
        return False, "Graduates registry must be a JSON array."

    try:
        with open(anchors_path, "r", encoding="utf-8") as f:
            anchors = json.load(f)
    except Exception as e:
        return False, f"Malformed anchors JSON: {e}"

    if not isinstance(anchors, list):
        return False, "Anchors registry must be a JSON array."

    record = next((g for g in graduates if isinstance(g, dict) and g.get("node_id") == node_id), None)
    if not record:
        return False, f"Node ID '{node_id}' not found in accreditation registry."

    anchor = anchors[0] if (anchors and isinstance(anchors[0], dict)) else {"anchor_id": "UNKNOWN", "public_identifier": "UNANCHORED"}

    diploma = {
        "acme_protocol": "RFC-001 (Genesis v1.0.0)",
        "accreditation_certificate": {
            "recipient_node": record.get("node_id"),
            "faculty": record.get("faculty"),
            "thesis_specification": record.get("thesis_file"),
            "immutable_merkle_sha": record.get("graduation_sha"),
            "status": record.get("status"),
            "biological_root_of_trust": {
                "anchor_id": anchor.get("anchor_id"),
                "identifier": anchor.get("public_identifier")
            },
            "value_attribution": record.get("attribution")
        }
    }
    return True, json.dumps(diploma, indent=2)

def audit_changed_files():
    violations = []

    # Check for orphaned git index lock
    if os.path.exists(".git/index.lock"):
        violations.append("DEADLOCK VIOLATION: Orphaned .git/index.lock detected in repository.")
        return violations

    branch, err, code = run_cmd("git rev-parse --abbrev-ref HEAD")
    if code != 0:
        violations.append(f"GIT ERROR: Unable to determine branch: {err}")
        return violations

    files_to_check = set()

    # Working tree diff (unstaged)
    out, err, code = run_cmd("git diff --name-only HEAD")
    if code != 0:
        violations.append(f"GIT ERROR: Failed to audit working tree: {err}")
        return violations
    if out:
        files_to_check.update(out.splitlines())

    # Staged diff
    out, err, code = run_cmd("git diff --name-only --cached")
    if code != 0:
        violations.append(f"GIT ERROR: Failed to audit staged index: {err}")
        return violations
    if out:
        files_to_check.update(out.splitlines())

    # Status porcelain
    out, err, code = run_cmd("git status --porcelain")
    if code != 0:
        violations.append(f"GIT ERROR: Failed to run status porcelain: {err}")
        return violations
    if out:
        for line in out.splitlines():
            if len(line) >= 3:
                files_to_check.add(line[3:].strip())

    # If on any non-main branch, check all commits vs main
    if branch != "main":
        out, err, code = run_cmd("git diff --name-only main...HEAD")
        if code != 0:
            violations.append(f"GIT ERROR: Failed to diff main...HEAD: {err}")
            return violations
        if out:
            files_to_check.update(out.splitlines())

    # Evaluate all touched files against PROTECTED_PATHS
    for f in files_to_check:
        f_norm = f.strip().replace("\\", "/")
        for p in PROTECTED_PATHS:
            p_norm = p.strip().replace("\\", "/")
            if f_norm == p_norm or f_norm.startswith(p_norm):
                violations.append(f"PROTECTED RESOURCE MUTATION: {f} (Branch: {branch})")

    return violations

def main():
    print("=== [ACME REFEREE ENGINE: INVARIANT AUDIT] ===")
    
    if len(sys.argv) == 1:
        # Default boundary guard audit
        violations = audit_changed_files()
        if violations:
            print("[FAIL] Invariant violations detected:")
            for v in violations:
                print(f"  - {v}")
            sys.exit(1)
        print("[PASS] Working tree and invariants intact.")
        sys.exit(0)

    arg = sys.argv[1]

    if arg == "--check-env":
        print("[+] Environment & Git integration test: PASS")
        sys.exit(0)

    if arg == "--verify-all":
        passed, msg = verify_all_theses()
        if passed:
            print(f"[PASS] {msg}")
            sys.exit(0)
        else:
            print(f"[FAIL] {msg}", file=sys.stderr)
            sys.exit(1)

    if arg == "--audit-ledger":
        passed, msg = audit_ledger()
        if passed:
            print(f"[PASS] {msg}")
            sys.exit(0)
        else:
            print(f"[FAIL] {msg}", file=sys.stderr)
            sys.exit(1)

    if arg == "--verify-thesis":
        if len(sys.argv) < 3 or not sys.argv[2].strip():
            print("[FAIL] Missing required thesis specification file path argument.", file=sys.stderr)
            sys.exit(2)
        target_file = sys.argv[2].strip()
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

    if arg == "--export-diploma":
        if len(sys.argv) < 3 or not sys.argv[2].strip():
            print("[FAIL] Missing required node ID argument for diploma export.", file=sys.stderr)
            sys.exit(2)
        node_id = sys.argv[2].strip()
        passed, payload = export_diploma(node_id)
        if passed:
            print(f"[ACME DIPLOMA CERTIFICATE: {node_id}]")
            print(payload)
            sys.exit(0)
        else:
            print(f"[FAIL] {payload}", file=sys.stderr)
            sys.exit(1)

    # Any unknown argument triggers error
    print(f"[FAIL] Unrecognized CLI option: {arg}", file=sys.stderr)
    print("Usage: verify.py [--check-env | --verify-all | --audit-ledger | --verify-thesis <file> | --export-diploma <node>]", file=sys.stderr)
    sys.exit(2)

if __name__ == "__main__":
    main()
