# RFC REQUEST: DOWNSTREAM INDEPENDENT SEMVER DECOUPLING & v0.0.0 GENESIS INVARIANT (RFC-037)
> **Reporting Client / Node:** acme-premier-studio  
> **Status:** CANDIDATE_REQUEST  
> **Target Faculty:** faculty-systems / faculty-law  
> **Target Release:** ACME v2.22.1  
> **Anchored Theses:** THESIS-013, THESIS-033, THESIS-036  

---

## 1. OBSERVED FRICTION (WHAT BROKE?)
- **Context:** Downstream autonomous client workspaces (such as `acme-premier-studio`, `acme-v214-preview`) adopting ACME as *Lex Superior* frequently conflate the upstream normative standard release tag (e.g., `v2.22.0`) with the downstream client's own application version number.
- **Root Tension (Conflation of Doctrine vs. Implementation Cadence):** 
  Automated developer agents and scaffolding routines erroneously stamp newly initialized downstream workspaces with the upstream ACME release tag (`v2.22.0`). This creates severe semantic version inflation, compromises SemVer integrity, and obscures the empirical fact that a downstream project is a brand-new application starting at its own inception genesis (`v0.0.0` / `v0.1.0`).

---

## 2. AD-HOC WORKAROUND (HOW WAS WORK PRESERVED?)
- **Immediate Mitigation:** Operators and architects manually intervene post-scaffolding to reject the inflated upstream tag and reset the downstream application version to `v0.0.0` / `v0.1.0`.
- **Residual Risk:** Without a constitutional invariant codified into ACME Lex Superior, autonomous agents repeatedly commit this category error during downstream workspace bootstrapping, creating confusion between the normative anchor and the product version.

---

## 3. PROPOSED HYPOTHESIS & DUAL SPECIFICATION

### A. PROPOSED LEX (INVIOLABLE HARD INVARIANTS, DoF = 0)
* **INV-DOWNSTREAM-GENESIS-SEMVER ($\text{DoF} = 0$):** 
  Every downstream client workspace adopting ACME MUST maintain an independent Semantic Versioning lifecycle strictly decoupled from upstream ACME core release tags. Downstream project repositories MUST initialize at `v0.1.0` (or `v0.0.0` genesis) and advance based solely on downstream atomic work package delivery.
* **INV-UPSTREAM-ANCHOR-DISENTANGLEMENT ($\text{DoF} = 0$):**
  Upstream ACME version coordinates (e.g., `v2.22.0` or `latest`) belong strictly inside the root `.acme` manifest and governance sidecars as the external normative authority reference (`lex_anchor`), and shall NEVER be stamped as the downstream project's own application version number.

### B. PROPOSED NORMS (ADAPTIVE STANDARDS & HEURISTICS, DoF >= 1)
* **NORM 1 (Dual Version Banner Standard):**
  Downstream CLI tools, web dashboards, and documentation headers should explicitly display both coordinates in bifurcated format:
  $$\text{Header: } \text{[Project Name]} \text{ vX.Y.Z (Genesis/SemVer)} \mid \text{Normative Anchor: ACME Lex Superior vA.B.C}$$
* **NORM 2 (Manifest Clarity):**
  Downstream `.acme` manifest schema may optionally specify `"project_version": "0.0.0"` alongside `"version": "latest"` to prevent agent hallucination during bootstrapping.

---

## 4. DEFINITION OF DONE (DoD)
- [x] RFC candidate formulated adhering to `templates/RFC_TEMPLATE.md`.
- [x] Clear demarcation between downstream SemVer (`v0.0.0`) and upstream Lex anchor (`v2.22.0`).
- [x] Decontaminated and dispatched to upstream ACME intake queue (`acme/rfcs`).

