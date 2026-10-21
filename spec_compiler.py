#!/usr/bin/env python3
"""
PROJECT ACME: GOAL-TO-SPEC REVERSE ENGINEERING & AUTO-RESOLVER
Version: 1.1.0
Description: Scans the theses repository, resolves invariant dependencies, 
and compiles an atomic TASK_SPEC.md with automated negative constraints.
"""

import os
import sys
import re

def scan_theses(theses_dir="theses"):
    if not os.path.exists(theses_dir):
        return []
    theses = []
    for f in sorted(os.listdir(theses_dir)):
        if f.endswith(".md") and f != "SPEC_TEMPLATE.md":
            theses.append(f)
    return theses

def compile_task_spec(goal_description, output_path="TASK_SPEC.md"):
    theses = scan_theses()
    
    # Check if goal triggers negative filtering (extraction / timeline / parse / uyap)
    trigger_keywords = ["extract", "timeline", "parse", "uyap", "analysis"]
    needs_negative_filter = any(kw in goal_description.lower() for kw in trigger_keywords)

    spec_content = f"""# TASK SPEC: COMPILED FROM GOAL
> **Objective:** {goal_description}  
> **Compiler:** ACME spec_compiler.py v1.1.0  
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
        print("Usage: python spec_compiler.py \"<goal description>\"")
        sys.exit(1)
    goal = sys.argv[1]
    compile_task_spec(goal)

if __name__ == "__main__":
    main()
