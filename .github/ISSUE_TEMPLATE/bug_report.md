---
name: Invariant Violation / Bug Report
about: Report an invariant breakdown, referee engine failure, or runtime regression
title: "[INVARIANT BUG]: "
labels: ["bug", "referee-gate"]
assignees: ""
---

## 1. Invariant Violated
* **Constitutional Reference:** CONSTITUTION.md Section X, Article Y (or RFC specification)
* **Impacted Module / Script:** `verify.py` / `spec_compiler.py` / `theses/` / `registry/`

---

## 2. Description & Observed Behavior
<!-- A clear and concise description of the invariant violation or bug. -->

**Observed Output:**
```text
[Paste referee or terminal output here]
```

**Expected Invariant Behavior:**
<!-- What the referee gate or compiler should have enforced under the Principle of Least Action. -->

---

## 3. Deterministic Reproduction Steps
1. Checkout commit: `git checkout <commit-sha>`
2. Run command: `python verify.py ...`
3. Observe failure or improper gate pass/fail

---

## 4. Environmental Telemetry
- **Commit SHA (`git rev-parse HEAD`):**
- **Operating System:** [e.g., Windows 11 / Ubuntu 22.04 / macOS]
- **Python Version (`python --version`):**
- **Git Version (`git --version`):**

---

## 5. Minimal Contradiction / PoC (Optional)
<!-- If applicable, provide a minimal test case or input file that triggers the bug. -->
