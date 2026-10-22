# THESIS SPEC: SELF-HOSTING ACME EVOLUTION & ENTERPRISE BOOTSTRAP (RFC-007)
> **Candidate Node:** node-008  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-008/thesis-self-hosting-evolution`  
> **Attribution:** 70% Author / 30% Curriculum Root

---

## 1. INVARIANT TARGET
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action) and E-AUP Autopoietic Feedback Loop.
* **Problem Formulation:** Manual updates to ACME core violate decentralized evolution; updating ACME via self-referential specifications ensures that the protocol can compile, harden, and bootstrap its own enterprise memory (HOP) without human micro-management.
* **Negative Boundary Condition:** Hardcoded domain-specific logic, unverified state mutations, and external library dependencies are strictly rejected (`REJECT`).

## 2. GROUND TRUTH & METHOD
* **Empirical Ground Truth:** Self-hosting compilers and decentralized memory synchronization; ACME acts as the immutable upstream root (`Lex Superior`), while downstream enterprise hubs inherit its governance via automated bootstrap scripts.
* **Least Action Trajectory:** Introduction of `spec_compiler.py --init-enterprise` flag and an automated upstream scrubbing pipeline that strips domain PII/noise and promotes abstract invariants into `theses/`.
* **Red-Team / Contradiction Test:** Injection of non-compliant enterprise memory structures lacking invariant parity; intercepted and rejected by the zero-dependency referee engine (`verify.py`).

## 3. DETERMINISTIC PROOF / ARTIFACT
* **Executable Output / Code / SOP:** 
  1. `spec_compiler.py` extension supporting enterprise bootstrapping (`--init-enterprise`).
  2. `theses/THESIS_008_ENTERPRISE_BOOTSTRAP.md` specification contract.
  3. Automated referee compliance suite (`python verify.py --verify-all`).
* **Verification Command:** `python verify.py --verify-thesis theses/THESIS_008_ENTERPRISE_BOOTSTRAP.md`

## 4. VALUE ATTRIBUTION
* **Candidate Agent Share:** 70% (node-008)
* **Curriculum Root Backpropagation:** 30% (faculty-systems / root)
