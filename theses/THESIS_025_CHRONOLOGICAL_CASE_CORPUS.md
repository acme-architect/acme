# THESIS SPEC: CHRONOLOGICAL CASE CORPUS AND UDF DISENTANGLEMENT ENGINE (RFC-024)
> **Candidate Node:** node-025  
> **Faculty:** faculty-law  
> **Target Branch:** `student/node-025/thesis-chronological-case-corpus`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.13.0  

---

## 1. INVARIANT TARGET & TELEOLOGICAL INTENT
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action), Section II, Article 4 (Dewdrop Boundary Invariant), and Section III, Article 8 (Minimal Evidentiary Path / Procedural Aikido).
* **Problem Formulation (The Chronological Hallucination & Identity-Event Contamination Gap):** Unstructured legal proceedings, judicial XML filings (UDF/UYAP), and witness testimonies routinely intertwine static personal metadata (national ID numbers, birthdates, barcode stamps, court docket numbers) with factual dispute timelines. Furthermore, the absence of strict temporal causal ordering and automated estoppel auditing (*Venire Contra Factum Proprium*) allows mutual contradictions between subjective claims and verified material records to go undetected, inflating litigation entropy.
* **Negative Boundary Condition (Via Negativa):** Blending personal identity metadata into operational event sequences, asserting causal relations without monotonic chronological ordering ($t_0 \le t_1 \le t_2$), failing to quarantine unanchored events (`UNRESOLVED_TEMPORAL_ANCHOR`), or asserting subjective contradiction claims without documentary parity is strictly prohibited (REJECT).

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Monotonic Temporal Ordering** | **$\text{DoF} = 0$** | *Lex Invariant* | Extracted dispute events must satisfy strict chronological progression ($t_i \le t_{i+1}$). Ambiguous timestamps must be quarantined immediately. |
| **Identity Metadata Quarantine** | **$\text{DoF} = 0$** | *Absolute Invariant* | Personal identity data (TCKN, birthdates, barcodes, docket IDs) must be quarantined from factual event sequences (RFC-005). |
| **Estoppel & Contradiction Parity** | **$\text{DoF} = 0$** | *State Invariant* | Contradictions between party assertions and official records evaluate via a binary matrix; subjective editorializing is barred. |
| **Extraction Window & Lexical Aliasing** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Linguistic date pattern regexes, normalization schemas, and jurisdictional terminology adapt dynamically across judicial venues. |

---

## 3. VIA NEGATIVA & INVIOLABLE INVARIANTS (LEX: DoF = 0)
* **INVARIANT 1 (Strict Temporal Causal Monotonicity):** Operational event sequences must adhere to strict temporal monotonicity. Unanchored or conflicting dates must be assigned `UNRESOLVED_TEMPORAL_ANCHOR` and isolated from the active causal trajectory.
* **INVARIANT 2 (Identity & Metadata Quarantine Gate):** Personal identity attributes, civil registry numbers, and procedural docket headers must be quarantined from the factual event stream. Merging identity metadata into occurrence chronology constitutes an invariant breach.
* **INVARIANT 3 (Binary Estoppel & Contradiction Verification):** The contradiction matrix must assert estoppel (*Venire Contra Factum Proprium*) between subjective claims and verified material records (e.g., bank ledgers, corporate registries). Speculative editorializing without documentary parity is forbidden.
* **INVARIANT 4 (Cryptographic Corpus Ledger Proof):** The extracted clean timeline, contradiction matrix, and sanitized UDF document hash (SHA-256) must be anchored to the case audit ledger prior to judicial brief compilation.

---

## 4. ADAPTIVE NORMS & HEURISTICS (NORM: DoF $\ge$ 1)
* **NORM 1 (Jurisdictional Date Normalization):** Support for localized date formats (DD.MM.YYYY, ISO 8601, textual month strings) adapts dynamically via configurable parsing profiles.
* **NORM 2 (XML Styling Strip Depth):** Stripping depth for procedural styles and font formatting nodes adapts to UDF/UYAP schema revisions without discarding substantive text bodies.
* **NORM 3 (Diagnostic Discrepancy Telemetry):** Non-fatal timeline ambiguities may log structured advisory notes without terminating the primary extraction pipeline.

---

## 5. DETERMINISTIC PROOF & DEFINITION OF DONE (DoD)
- [ ] `theses/THESIS_025_CHRONOLOGICAL_CASE_CORPUS.md` verified UTF-8 No-BOM.
- [ ] Zero-code pure NLP compliance maintained across repository.
- [ ] Isolated branch `student/node-025/thesis-chronological-case-corpus` merged into `main` via `--no-ff`.
- [ ] `registry/graduates.json` augmented with `node-025` accreditation record (70/30 attribution ratio under `faculty-law`).
- [ ] `README.md` version bumped to `v2.13.0`.
- [ ] Official Git tag `v2.13.0` created and verified.
- [ ] Downstream `acme-incubator` referee gate (`python verify.py`) passes 6/6 `PASS`.

---

## 6. VALUE ATTRIBUTION
* **Candidate Share:** 70% (`node-025`)
* **Curriculum Root Share:** 30% (`faculty-law`)