# TASK SPEC: COMPILED FROM GOAL
> **Objective:** Build UYAP document timeline extractor with zero noise  
> **Compiler:** ACME spec_compiler.py v1.1.0  
> **Status:** COMPILED & LOCKED (Semantic Noise Rejection Enforced)

---

## 1. RESOLVED INVARIANTS & DEPENDENCIES
* Automated reference linked: `theses/THESIS_001_LEAST_ACTION.md`
* Automated reference linked: `theses/THESIS_002_INVERSE_SPEC.md`
* Automated reference linked: `theses/THESIS_002_PROCEDURAL_AIKIDO.md`
* Automated reference linked: `theses/THESIS_003_DEWDROP_BOUNDARY.md`
* Automated reference linked: `theses/THESIS_005_GOAL_TO_SPEC.md`
* Automated reference linked: `theses/THESIS_006_SEMANTIC_NOISE_REJECTION.md`

## 2. NEGATIVE INVARIANTS & BOUNDARY CONDITIONS
* **INVARIANT (RFC-005):** Must isolate identity metadata (birthdates, party IDs) from operational timeline events. Must provide periodic progress stdout.

## 3. DEFINITION OF DONE (DoD)
* Zero-dependency invariant verification via `verify.py`.
* UTF-8 stdout buffering and periodic heartbeat telemetry implemented.
* Working tree clean and adherence to CONSTITUTION.md.
