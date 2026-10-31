# RFC REQUEST: WORKSPACE COHERENCE & SCOPE DRIFT INVARIANT (INV-WORKSPACE-COHERENCE)
> **Reporting Client / Node:** acme-downstream-client  
> **Status:** CANDIDATE_REQUEST  
> **Target Faculty:** faculty-law  
> **Anchored Theses:** THESIS-003, THESIS-016, THESIS-020  

---

## 1. OBSERVED FRICTION (WHAT BROKE?)
- **Context:** Autonomous downstream workspaces operating under `mode: autonomous_workspace` author multiple specifications and prototypes over extended delivery cycles.
- **Root Tension:** Absence of a cross-spec orthogonality referee allows disparate, ontologically unrelated specifications (e.g., enterprise competency engines, adjective decompilers, and isolated discrete state machines) to accumulate in the root `specs/` directory without isolation. This leads to scope creep (scope drift) and unmonitored invariant contradictions between specifications (e.g., Zero-Asset Audio vs. External MP3 dependencies).

---

## 2. AD-HOC WORKAROUND (HOW WAS WORK PRESERVED?)
- **Immediate Mitigation:** Manual directory renaming and informal developer agreements to segregate non-core prototypes.
- **Residual Risk:** Repository pollution, schema divergence, and silent failure of upstream intake compilation due to domain contamination.

---

## 3. PROPOSED HYPOTHESIS & DUAL SPECIFICATION
- **A. Proposed Lex (Hard Invariants, DoF=0):**
  - **INV-COHERENCE-01 (Domain Distance Enforcement):** The constitutional referee MUST compare spec domains against the `.acme` manifest `mode`. Non-core or orthogonal specifications that lack the explicit `EXPLICIT_SANDBOX_POC` tag halt Merkle sealing with `[WARN: SCOPE_DRIFT]`.
  - **INV-COHERENCE-02 (Cross-Spec Invariant Orthogonality):** An automated referee function `assert_no_spec_conflicts()` MUST scan all active specifications. Contradictory policy assertions between specs immediately halt pipeline execution (`REJECT_INVARIANT_CONFLICT`).
- **B. Proposed Norms (Adaptive Guidance, DoF>=1):**
  - Automated recommendations advising relocation of isolated sandboxes to dedicated downstream workspaces (e.g., `projects/discrete-fdsm`).
