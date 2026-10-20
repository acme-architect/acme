#!/usr/bin/env python3
"""
PROJECT ACME: SYSTEM STATE EXPORT GENERATOR
Version: 1.0.0
Compiles comprehensive system state, Merkle tree history, registry records, and verification status.
"""

import os
import sys
import subprocess
import json
from datetime import datetime, timezone

def run_cmd(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def load_json(path):
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None

def main():
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    output_path = os.path.join(base_dir, "STATE_EXPORT.md")

    head_sha, _, _ = run_cmd("git rev-parse HEAD")
    tag, _, _ = run_cmd("git describe --tags --abbrev=0")
    status_out, _, _ = run_cmd("git status --short")
    git_log, _, _ = run_cmd("git log --graph --oneline -n 12")

    anchors = load_json(os.path.join(base_dir, "registry", "anchors.json")) or []
    graduates = load_json(os.path.join(base_dir, "registry", "graduates.json")) or []

    # Run verification suite
    v_env_out, _, v_env_code = run_cmd("python verify.py --check-env")
    v_all_out, _, v_all_code = run_cmd("python verify.py --verify-all")
    v_led_out, _, v_led_code = run_cmd("python verify.py --audit-ledger")
    v_main_out, _, v_main_code = run_cmd("python verify.py")

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = [
        "# PROJECT ACME: CANONICAL SYSTEM STATE EXPORT",
        f"> **Generated:** {ts} | **Release Tag:** `{tag}` | **Head SHA:** `{head_sha}`",
        "",
        "---",
        "",
        "## 1. REPOSITORY TELEMETRY & MERKLE TREE",
        f"- **Active Commit HEAD:** `{head_sha}`",
        f"- **Current Release Tag:** `{tag}`",
        f"- **Working Tree Status:** `{'CLEAN' if not status_out else 'DIRTY'}`",
        "",
        "### Recent Merkle History:",
        "```text",
        git_log,
        "```",
        "",
        "## 2. BIOLOGICAL ROOT OF TRUST REGISTRY",
    ]

    for a in anchors:
        lines.append(f"- **Anchor ID:** `{a.get('anchor_id')}` | **Role:** {a.get('role')} | **Identifier:** `{a.get('public_identifier')}` | **Status:** `{a.get('status')}`")

    lines.extend([
        "",
        "## 3. ACCREDITED GRADUATION REGISTRY",
        f"**Total Accredited Nodes:** {len(graduates)}",
        ""
    ])

    for g in graduates:
        lines.append(f"### Node: `{g.get('node_id')}` ({g.get('faculty')})")
        lines.append(f"- **Thesis File:** `{g.get('thesis_file')}`")
        lines.append(f"- **Graduation Merkle SHA:** `{g.get('graduation_sha')}`")
        lines.append(f"- **Status:** `{g.get('status')}`")
        lines.append(f"- **Value Attribution:** {int(g.get('attribution', {}).get('leaf_agent_share', 0)*100)}% Leaf Agent / {int(g.get('attribution', {}).get('curriculum_root_share', 0)*100)}% Curriculum Root")
        lines.append("")

    lines.extend([
        "## 4. INVARIANT VERIFICATION SUITE TELEMETRY",
        f"- **Environment Check:** `{'PASS' if v_env_code == 0 else 'FAIL'}` ({v_env_out})",
        f"- **Theses Specification Audit:** `{'PASS' if v_all_code == 0 else 'FAIL'}` ({v_all_out})",
        f"- **Attribution Ledger Audit:** `{'PASS' if v_led_code == 0 else 'FAIL'}` ({v_led_out})",
        f"- **Boundary Guard Audit:** `{'PASS' if v_main_code == 0 else 'FAIL'}` ({v_main_out})",
        "",
        "## 5. AIR-GAPPED RECOVERY CHECKPOINT",
        "- **Bundle File:** `acme-v1.0.0.bundle`",
        "- **Offline Clone Command:** `git clone acme-v1.0.0.bundle acme-restored`",
        "",
        "---",
        "*Project ACME: Autonomous Cognitive Multi-Agent Ecosystem (RFC-001)*"
    ])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"[+] State export generated successfully: {output_path}")

if __name__ == "__main__":
    main()
