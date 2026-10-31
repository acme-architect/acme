# THESIS SPEC: AIR-GAPPED STANDALONE PUBLIC DISTRIBUTION & CLEAN-ROOM EXPORT (RFC-041)
> **Candidate Node:** node-046  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-046/thesis-standalone-public-distribution`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.25.0  
> **Constitutional Anchor:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action), Section II (INV-STANDALONE-INSTANCE, Dewdrop Boundary Invariant), Section III (Biological Primacy)

---

## 1. TELEOLOGICAL INTENT & CONSTITUTIONAL REFERENCE
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action), Section II, Article 4 (Dewdrop Boundary Invariant), Section II, Article 7 (Downstream Non-Pollution & Single Manifest), Section II, Article 12 (INV-STANDALONE-INSTANCE), and Section III, Article 13 (Biological Primacy).
* **Problem Formulation (Governance Artifact Leakage & Contaminated Distribution):** When public open-source software packages or executable binaries are deployed to downstream consumers, internal project management office (PMO) governance artifacts—such as constitutional specs, thesis files, cognitive referee harnesses (`verify.py`), and private telemetry sidecars—frequently leak into end-user repositories. This introduces confusing cognitive baggage, unwanted normative dependencies, and security/confidentiality vulnerabilities. Standalone Public Distribution establishes a strict clean-room unidirectional projection mechanism, ensuring the final consumer deliverable (e.g., `cadence`) contains exclusively executable code, isolated unit tests, consumer documentation, and an open-source license, totally decoupled from internal governance.
* **Negative Boundary Condition (Via Negativa):** Distributing an open-source instance or binary artifact containing `.acme`, `CONSTITUTION.md`, `verify.py`, internal theses, or PMO telemetry is strictly prohibited (`REJECT_PMO_CONTAMINATION`).

### SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt verification immediately (`REJECT_UNANCHORED_INCEPTION`). Top 3 domain-specific structural failure modes cataloged and strictly prohibited:*
* **FAILURE MODE 1 (Governance Artifact Pollution):** PMO manifests, referee verifiers, or thesis files published to public end-user repos -> `[PROHIBITED]` Strict clean-room export whitelist prohibiting internal governance tracking (`INV-STANDALONE-INSTANCE-01`).
* **FAILURE MODE 2 (Bidirectional Coupling Drift):** Upstream PMO importing runtime code modifications directly from public repos without scrubbed intake -> `[PROHIBITED]` Unidirectional projection filter with strict osmosis barrier (`INV-CLEAN-ROOM-PROJECTION-02`).
* **FAILURE MODE 3 (Heavyweight Toolchain Imposition):** Forcing end-users to install internal cognitive agents or Python SDK tooling to run deliverables -> `[PROHIBITED]` Zero-dependency standalone execution and lightweight one-click launcher bootstrap (`INV-LIGHTWEIGHT-BOOTSTRAP-03`).

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Clean-Room Boundary** | **$\text{DoF} = 0$** | *Lex Invariant* | Zero governance files (`.acme`, `CONSTITUTION.md`, `verify.py`) in public repo. |
| **Unidirectional Projection** | **$\text{DoF} = 0$** | *Integrity Lex* | Export pipeline is strictly unidirectional (PMO $\to$ Public Instance). |
| **Zero External Ingestion** | **$\text{DoF} = 0$** | *Safety Invariant* | Standalone runtime executes with zero dependency on ACME Core or PMO. |
| **Launcher Packaging Heuristics**| **$\text{DoF} \ge 1$** | *Adaptive Norm* | Bootstrap launcher selects curl/gh release vs. binary unpack dynamically. |
| **Consumer Documentation Depth**| **$\text{DoF} \ge 1$** | *Adaptive Norm* | Public README tailors developer quickstarts to target developer personas. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INV-STANDALONE-INSTANCE-01 (Absolute Governance Decontamination):** Any distributed public open-source repository (e.g., `cadence`) or binary installation package must contain zero internal PMO or constitutional governance artifacts. Files such as `.acme`, `CONSTITUTION.md`, `verify.py`, `theses/`, or `rfcs/` are strictly barred (`REJECT_PMO_CONTAMINATION`).
* **INV-CLEAN-ROOM-PROJECTION-02 (Deterministic Clean-Room Whitelist Filter):** Migration of code from the internal PMO workspace to the public instance repository occurs exclusively through an audited clean-room projection filter. Only pure executable source code (`src/`), independent unit tests (`tests/`), end-user documentation (`README.md`), and open-source licensing (`LICENSE`) may be exported.
* **INV-LIGHTWEIGHT-BOOTSTRAP-03 (One-Click Lightweight Bootstrap):** Public distribution packages must provide a lightweight standalone launcher or bootstrap script allowing consumers to retrieve and execute certified releases directly from GitHub Releases with zero external environment setup.

---

## 4. ADAPTIVE NORMS & HEURISTICS (NORM: DoF >= 1)
* **NORM 1 (Self-Contained Test Suites):** Exported test suites in `tests/` must evaluate exclusively against public APIs and standard library mocks, without requiring PMO fixture databases.
* **NORM 2 (Public Release Cadence):** Public release tags on standalone repositories synchronize with PMO production milestone seals, maintaining an independent consumer SemVer.

---

## 5. DEFINITION OF DONE (DoD)
- [x] `theses/THESIS_046_STANDALONE_PUBLIC_DISTRIBUTION.md` authored in UTF-8 No-BOM.
- [x] `CONSTITUTION.md` Section II augmented with Article 12 / `INV-STANDALONE-INSTANCE`.
- [x] `curriculum/faculty-systems/FOUNDATIONS.md` updated with SYS-125 axiom.
- [x] `registry/graduates.json` augmented with `node-046` graduation diploma.
- [x] `python verify.py --verify-all` passes 100% green with zero code artifacts.
- [x] Clean `--no-ff` merge to `main`, ready for dual release milestone.
