# THESIS SPEC: [INVARIANT / SPECIFICATION TITLE] (RFC-XXX)
> **Candidate Node:** [e.g., node-XXX]  
> **Faculty:** [faculty-systems | faculty-philosophy | faculty-law]  
> **Target Branch:** `student/[node-id]/thesis-[topic]`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v[X.Y.Z]

---

## 1. SCOPE & INTENT
[Describe the problem formulation, systemic friction, or capability being introduced. Clearly outline the boundary of this specification.]

---

## 2. HEDEF KİTLE PROFİLİ & ERGONOMİ MATRİSİ (AUDIENCE & ERGONOMICS - INV-AUDIENCE-TARGET)
* **Hedef Persona / Kullanıcı Seviyesi:** [Casual | Pro | Enterprise | Embedded | Autonomous Agent]
* **Birincil Kullanım Bağlamı (Context of Use):** [Deployment environment, interaction cadence, session depth, zero-install requirements]
* **Ergonomi Sınırları:** [Cihaz tipi (Desktop/Mobile/CLI/Embedded), Girdi arayüzü (Klavye/Touch/API/Terminal), Gecikme beklentisi (P95 latency bounds)]

---

## 3. YEREL UYUM & FİKRİ MÜLKİYET (IP) SINIRLARI (COMPLIANCE & IP RADAR - INV-COMPLIANCE-RADAR)
* **Fikri Mülkiyet (IP) & Marka Arındırma:** [Prohibition of proprietary trademarks, clean-room asset reproduction, zero copyrighted asset/audio leakage]
* **Platform & Mevzuat Değişmezleri:** [Yerel veri egemenliği, tarayıcı autoplay/sandbox politikaları, lisans uyumluluğu (MIT/Apache2/GPL-free)]
* **H-SWOT Pazar Gerçekliği & Hukuki Temizlik Kapısı:** [Fırsatlar (O) pazar rezonansına, Tehditler (T) fikri mülkiyet ve platform sürtünmesine bağlanmalıdır]

---

## 4. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Boundary Layer | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **[Layer 1 Name]** | **$\text{DoF} = 0$** | *Lex Invariant* | [Deterministic condition where breach triggers immediate halt / REJECT] |
| **[Layer 2 Name]** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | [Contextual parameter space, heuristic optimization band, or flexible range] |

---

## 5. DUAL NORMATIVE SPECIFICATION (LEX VS. NORM)

### SECTION A: THE LEX (INVIOLABLE HARD INVARIANTS, DoF = 0)
*Violations of the Lex trigger immediate evaluation rejection (`REJECT`). No ad-hoc workarounds or local overrides permitted.*
* **LEX 1 ([Invariant Name]):** [Strict negative boundary or binary requirement]
* **LEX 2 ([Invariant Name]):** [Non-negotiable architectural invariant]

### SECTION B: THE NORMS (ADAPTIVE STANDARDS & HEURISTICS, DoF >= 1)
*Advisory guidelines and best practices. Deviation is permitted with explicit architectural rationale.*
* **NORM 1 ([Standard Name]):** [Recommended operational heuristic, sizing band, or format guideline]
* **NORM 2 ([Standard Name]):** [Performance optimization practice or evolutionary convention]

---

## 6. DEFINITION OF DONE (DoD)
- [ ] Specification drafted conforming to `SPEC_TEMPLATE.md` in UTF-8 No-BOM.
- [ ] Target audience persona and ergonomic matrix verified (`INV-AUDIENCE-TARGET`).
- [ ] Compliance radar and trademark sanitization confirmed (`INV-COMPLIANCE-RADAR`).
- [ ] Peer-review consensus and referee audit verified.
- [ ] Merged to `main` with `--no-ff`, tagged with target release version.
- [ ] Cryptographic Merkle diploma recorded in `registry/graduates.json`.
