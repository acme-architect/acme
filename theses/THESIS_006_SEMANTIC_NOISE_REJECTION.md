# THESIS SPEC: SEMANTIC NOISE REJECTION AND NEGATIVE INVARIANTS IN DOCUMENT EXTRACTION (RFC-005)
> **Candidate Node:** node-006  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-006/thesis-semantic-noise-rejection`  
> **Attribution:** 70% Author / 30% Curriculum Root

---

## 1. INVARIANT TARGET
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action) and Section II, Article 6 (Zero-Friction Shield).
* **Problem Formulation:** Unfiltered regex matching across legal and administrative documents confuses identity metadata (birthdates, party IDs, barcode stamps) with operational timeline events, generating high-entropy garbage data. Furthermore, missing stdout buffer wrappers cause platform crashes, and silent batch processing creates a frozen execution illusion.
* **Negative Boundary Condition:** Merging identity attributes with factual occurrence timelines, operating without UTF-8 stdout buffering, and executing batch loops without periodic progress heartbeats are strictly rejected (REJECT).

## 2. GROUND TRUTH & METHOD
* **Empirical Ground Truth:** Signal-to-noise ratio (SNR) optimization in automated information extraction; boundary isolation between static meta-attributes and dynamic event sequences.
* **Least Action Trajectory:** Automated negative filtering in `spec_compiler.py` and downstream CLI targets, enforcing strict structural separation, UTF-8 buffer wrapping, and progress telemetry.
* **Red-Team / Contradiction Test:** Injection of unstructured legal corpora containing overlapping birthdates and financial claims; intercepted and cleansed by negative constraint enforcement gates.

## 3. DETERMINISTIC PROOF / ARTIFACT
* **Executable Output / Code / SOP:** Enhanced `spec_compiler.py`, updated referee engine verification suite, and isolated extraction rules.
* **Verification Command:** `python verify.py --verify-thesis theses/THESIS_006_SEMANTIC_NOISE_REJECTION.md`

## 4. VALUE ATTRIBUTION
* **Candidate Agent Share:** 70% (node-006)
* **Curriculum Root Backpropagation:** 30% (faculty-systems / root)
