#!/usr/bin/env python3
"""
PROJECT ACME: GOAL-TO-SPEC REVERSE ENGINEERING & AUTO-RESOLVER
Version: 1.2.0 (Crucible Hardened)
Description: Scans the theses repository, resolves invariant dependencies, 
and compiles an atomic TASK_SPEC.md with automated negative constraints.
"""

import os
import sys
import re

# Configure UTF-8 stdout/stderr buffering on Windows
if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

MAX_GOAL_CHARS = 10000

def scan_theses(theses_dir="theses"):
    if not os.path.exists(theses_dir) or not os.path.isdir(theses_dir):
        return []
    theses = []
    for f in sorted(os.listdir(theses_dir)):
        full_path = os.path.join(theses_dir, f)
        if f.endswith(".md") and f != "SPEC_TEMPLATE.md" and os.path.isfile(full_path):
            theses.append(f)
    return theses

def compile_task_spec(goal_description, output_path="TASK_SPEC.md", theses_dir="theses"):
    if not goal_description or not goal_description.strip():
        print("[FAIL] Empty goal specification is prohibited.", file=sys.stderr)
        sys.exit(1)

    if len(goal_description) > MAX_GOAL_CHARS:
        print(f"[FAIL] Goal payload exceeds maximum allowed entropy ({MAX_GOAL_CHARS} chars).", file=sys.stderr)
        sys.exit(1)

    theses = scan_theses(theses_dir)
    if not theses:
        print("[FAIL] Orphan execution: No foundational theses found in repository.", file=sys.stderr)
        sys.exit(1)
    
    # Check if goal triggers negative filtering (extraction / timeline / parse / uyap)
    trigger_keywords = ["extract", "timeline", "parse", "uyap", "analysis"]
    needs_negative_filter = any(kw in goal_description.lower() for kw in trigger_keywords)

    spec_content = f"""# TASK SPEC: COMPILED FROM GOAL
> **Objective:** {goal_description.strip()}  
> **Compiler:** ACME spec_compiler.py v1.2.0  
> **Status:** COMPILED & LOCKED (Semantic Noise Rejection Enforced)

---

## 1. RESOLVED INVARIANTS & DEPENDENCIES
"""
    for t in theses:
        spec_content += f"* Automated reference linked: `theses/{t}`\n"

    spec_content += f"""
## 2. NEGATIVE INVARIANTS & BOUNDARY CONDITIONS
"""
    if needs_negative_filter:
        spec_content += "* **INVARIANT (RFC-005):** Must isolate identity metadata (birthdates, party IDs) from operational timeline events. Must provide periodic progress stdout.\n"
    else:
        spec_content += "* Standard zero-friction invariant bounds apply.\n"

    spec_content += f"""
## 3. DEFINITION OF DONE (DoD)
* Zero-dependency invariant verification via `verify.py`.
* UTF-8 stdout buffering and periodic heartbeat telemetry implemented.
* Working tree clean and adherence to CONSTITUTION.md.
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(spec_content)
    
    print(f"[PASS] Successfully compiled {output_path} referencing {len(theses)} foundational theses (Negative Filter: {needs_negative_filter}).")

def main():
    if len(sys.argv) < 2:
        print("Usage: python spec_compiler.py \"<goal description>\"", file=sys.stderr)
        sys.exit(1)
    goal = sys.argv[1]
    compile_task_spec(goal)

if __name__ == "__main__":
    main()
