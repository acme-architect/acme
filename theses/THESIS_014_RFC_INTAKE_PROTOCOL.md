# THESIS SPEC: DOWNSTREAM RFC INTAKE & TRIAGE PROTOCOL (RFC-014)
> **Candidate Node:** node-014  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-014/thesis-rfc-intake-protocol`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.2.0

---

## 1. SCOPE & INTENT
Eliminates cognitive burden and domain contamination from downstream client projects. Clients are strictly prohibited from authoring full theses; instead, they submit lightweight RFC Requests detailing friction, workarounds, and hypotheses. The ACME Review Board centrally triages, groups, decontaminates, and formalizes these requests into canonical theses.

---

## 2. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Layer / Interface | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Client Submission Schema** | **$\text{DoF} = 0$** | *Template Invariant* | Must follow `templates/RFC_TEMPLATE.md`. Free-form conversational complaints are rejected. |
| **Domain Decontamination** | **$\text{DoF} = 0$** | *Purity Invariant* | All project-specific variables, local file paths, and PII must be purged prior to thesis promotion. |
| **Triage & Synthesis Window** | **$\text{DoF} \ge 1$** | *Dialectical Space* | Review Board has full discretion to aggregate multiple related RFCs into a single thesis. |

---

## 3. VIA NEGATIVA & INVARIANTS
* **INVARIANT 1 (No Client-Authored Theses):** Downstream workers must not author formal ACME thesis specifications. They emit structured RFC requests only.
* **INVARIANT 2 (Domain Scrubbing Requirement):** No candidate thesis derived from an RFC may reference downstream implementation tech stacks, proprietary data, or internal workspace layouts.
* **INVARIANT 3 (Review Board Gate):** An RFC request cannot mutate the ACME Constitution or register a graduate diploma without formal Review Board deliberation and consensus.

---

## 4. DEFINITION OF DONE (DoD)
- [ ] `templates/RFC_TEMPLATE.md` established.
- [ ] `theses/THESIS_014_RFC_INTAKE_PROTOCOL.md` created in UTF-8 No-BOM.
- [ ] `AGENTS.md` updated with RFC submission guidelines.
- [ ] Merged to `main` with `--no-ff`, `node-014` recorded in `registry/graduates.json`.
- [ ] Tagged as `v2.2.0`, `acme-v2.2.0.bundle` verified.
