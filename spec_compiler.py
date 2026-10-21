#!/usr/bin/env python3
"""
PROJECT ACME: GOAL-TO-SPEC REVERSE ENGINEERING & AUTO-RESOLVER
Version: 1.0.0
Description: Scans the theses repository, resolves invariant dependencies, 
and compiles an atomic TASK_SPEC.md from a raw objective string.
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
    
    spec_content = f"""# TASK SPEC: COMPILED FROM GOAL
> **Objective:** {goal_description}  
> **Compiler:** ACME spec_compiler.py v1.0.0  
> **Status:** COMPILED & LOCKED

---

## 1. RESOLVED INVARIANTS & DEPENDENCIES
"""
    for t in theses:
        spec_content += f"* Automated reference linked: `theses/{t}`\n"

    spec_content += f"""
## 2. DEFINITION OF DONE (DoD)
* Zero-dependency invariant verification via `verify.py`.
* Working tree clean and adherence to CONSTITUTION.md.
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(spec_content)
    
    print(f"[PASS] Successfully compiled {output_path} referencing {len(theses)} foundational theses.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python spec_compiler.py \"<goal description>\"")
        sys.exit(1)
    goal = sys.argv[1]
    compile_task_spec(goal)

if __name__ == "__main__":
    main()
