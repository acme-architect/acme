# CANONICAL 7-STEP AOP OPERATIONAL LIFECYCLE STATE MACHINE (SYS-127)
> **Standard Specification:** Canonical Agent-Oriented Paradigm (AOP) Operational Framework  
> **Constitutional Anchor:** CONSTITUTION.md Section I (Principle of Least Action), Section II (INV-CIRCADIAN-CADENCE, INV-SEQUENCE-PRECEDENCE, INV-NORMATIVE-RESOLVE), Section III (Biological Primacy)  
> **Target Release:** ACME v2.27.0+  
> **Faculty:** faculty-systems (SYS-127)

---

## 1. TELEOLOGICAL INTENT & STATE MACHINE TAXONOMY

In autonomous multi-agent environments, uncontrolled dispatch and informal handoffs introduce entropy, unanchored execution drift, and dangling compute allocations. The **Canonical 7-Step AOP Operational Lifecycle** operationalizes Hans Kelsen's normative stratification and military C4I discipline into a deterministic, non-bypassable finite state machine (FSM). 

Every autonomous agent runtime, developer harness, or downstream workflow must advance strictly through these 7 canonical phases:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   CANONICAL 7-STEP AOP STATE MACHINE                   │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
       ┌────────────────────────────────────────────────────────┐
       │ 1. READY (Quiescent Standby / Clean Tree / Zero Tokens)│
       └───────────────────────────┬────────────────────────────┘
                                   │ Directive Ingestion (T0)
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │ 2. DIRECTIVE (Task Intent / Lex Bounds / DoF Ceiling)   │
       └───────────────────────────┬────────────────────────────┘
                                   │ Reveille Roll-Call
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │ 3. MARCH (Upstream Sync / Git Pull / Referee Pass)     │
       └───────────────────────────┬────────────────────────────┘
                                   │ Invariant Lock
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │ 4. EXECUTE & TELEMETRY (Atomic Build / Test Loop / Scar)│
       └───────────────────────────┬────────────────────────────┘
                                   │ Milestone Reached (Optional)
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │ 5. RELEASE (Clean Tag / Merkle Mühür / Production Push)│
       └───────────────────────────┬────────────────────────────┘
                                   │ End of Shift Signal
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │ 6. RETREAT (Garbage Collection / Debris Scrub / Commit) │
       └───────────────────────────┬────────────────────────────┘
                                   │ Digest Emission
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │ 7. EOD SUMMARY (Consolidated Telemetry / Merkle Proof) │
       └───────────────────────────┬────────────────────────────┘
                                   │ Quiescent Lock
                                   ▼
       ┌────────────────────────────────────────────────────────┐
       │ 1. READY (Quiescent Standby / Zero Allocation)          │
       └────────────────────────────────────────────────────────┘
```

---

## 2. THE 7 CANONICAL LIFECYCLE PHASES

### Phase 1: READY (Quiescent Standby)
* **Invariant:** `INV-QUIESCENT-STANDBY-03` ($\text{DoF} = 0$)
* **State:** Working tree 100% clean, zero background daemons, zero inference tokens consumed.
* **Exit Condition:** Receipt of an authenticated biological or machine-to-machine (M2M) directive.

### Phase 2: DIRECTIVE (Teleological Ingestion & Boundary Binding)
* **Invariant:** `INV-NORMATIVE-RESOLVE-01` & `INV-DYNAMIC-CONATUS` ($\text{DoF} = 0$)
* **State:** Parse human intent ($T_0$), identify governing normative hierarchy (Layers 0-4), extract DoF ceiling ($\le 1.5\times$), and lock task specification.
* **Exit Condition:** Deterministic task spec formulated; negative anti-pattern gates cataloged.

### Phase 3: MARCH (Morning Reveille & Upstream Alignment)
* **Invariant:** `INV-REVEILLE-01` & `INV-CIRCADIAN-CADENCE` ($\text{DoF} = 0$)
* **State:** Roll-call verification: execute upstream status pull (`git pull origin main`), verify local repository health, and run constitutional referee (`python verify.py`).
* **Exit Condition:** Upstream parity confirmed 100% green. Unsynchronized dispatch raises `REJECT_UNSYNCHRONIZED_DISPATCH`.

### Phase 4: EXECUTE & TELEMETRY (Atomic Construction & Verification)
* **Invariant:** `INV-KEY-03` & `INV-SEQUENCE-PRECEDENCE` ($\text{DoF} \ge 1$ bounded by $\text{DoF}=0$ keystone)
* **State:** Atomic implementation sprints, episodic scar logging, continuous pre-flight gate verification, and structured regression runs.
* **Exit Condition:** Unit tests, linting, and invariant audits pass 100% green without scaffold residue.

### Phase 5: RELEASE (Production Promotion & Milestone Sealing - Optional)
* **Invariant:** `INV-STANDALONE-INSTANCE` & `INV-CANONICAL-CASCADE` ($\text{DoF} = 0$)
* **State:** Mid-day or milestone promotion: clean-room export, Git Merkle commit hash sealing, SemVer tag increment, and remote push.
* **Exit Condition:** Distributed artifacts decontaminated of internal PMO governance harnesses.

### Phase 6: RETREAT (EOD Consolidation & Garbage Collection)
* **Invariant:** `INV-RETREAT-02` ($\text{DoF} = 0$)
* **State:** Mandatory evening garbage collection: prune ephemeral test scratchpads, flush transient probe files, seal living state hashes into Git, and dispatch unresolved friction as candidate RFCs.
* **Exit Condition:** Working tree 100% clean; zero untracked mock artifacts.

### Phase 7: EOD SUMMARY (Consolidated Telemetry & Transition to Standby)
* **Invariant:** `INV-OBSERVER-CORE` ($\text{DoF} = 0$)
* **State:** Emit single-page consolidated status telemetry: Merkle commit SHAs, test pass counts, active tags, and transition acknowledgment.
* **Exit Condition:** Transition directly into **Phase 1: READY**; runtime drops compute allocations to zero.

---

## 3. SECTION 1.4: PRE-MORTEM ANTI-PATTERN GATES (DoF = 0)
*Violations halt verification immediately (`REJECT_UNANCHORED_INCEPTION`). Top 3 domain-specific structural failure modes cataloged and strictly prohibited:*

* **FAILURE MODE 1 (Unanchored Premature Leap):** Transitioning from DIRECTIVE straight to EXECUTE without executing MARCH upstream alignment -> `[PROHIBITED]` Circuit breaker trips immediately (`REJECT_PREMATURE_LEAP` / `INV-SEQUENCE-PRECEDENCE`).
* **FAILURE MODE 2 (Dirty Retreat & Ephemeral Residue):** Concluding an operating cycle while leaving unpruned test scratchpads, mock files, or uncommitted deltas on disk -> `[PROHIBITED]` Mandatory scrub gate enforced during RETREAT (`INV-RETREAT-02`).
* **FAILURE MODE 3 (Zombie Compute Bleed):** Autonomous runtimes or polling loops maintaining background thread activity post-summary -> `[PROHIBITED]` Immediate drop of compute allocations to absolute zero in READY (`INV-QUIESCENT-STANDBY-03`).

---

## 4. TABLE OF DEGREES OF FREEDOM (DoF BUDGET)

| Lifecycle Stage | Permitted DoF | Constraint Type | Cognitive Referee Rule |
| :--- | :--- | :--- | :--- |
| **Phase 1: READY Gate** | **$\text{DoF} = 0$** | *Safety Invariant* | Quiescent zero-token listener. Clean working tree mandatory. |
| **Phase 2: DIRECTIVE Gate** | **$\text{DoF} = 0$** | *Lex Invariant* | Kelsen hierarchy grounding mandatory before code emission. |
| **Phase 3: MARCH Gate** | **$\text{DoF} = 0$** | *Lex Invariant* | Upstream sync & referee pass mandatory. Zero unverified dispatch. |
| **Phase 4: EXECUTE Plane** | **$\text{DoF} \ge 1$** | *Adaptive Norm* | Algorithmic implementation tuning within locked keystone constraints. |
| **Phase 5: RELEASE Gate** | **$\text{DoF} = 0$** | *Integrity Lex* | Decontaminated clean-room export; Merkle SHA sealed. |
| **Phase 6: RETREAT Gate** | **$\text{DoF} = 0$** | *Boundary Lex* | Ephemeral scratchpads pruned; living state committed. |
| **Phase 7: EOD SUMMARY** | **$\text{DoF} = 0$** | *Reporting Lex* | Deterministic single-page digest; immediate transition to READY. |

---

## 5. DEFINITION OF DONE (DoD)

- [x] Specification drafted conforming to UTF-8 No-BOM.
- [x] Sequential 7-step progression locked with zero-degree-of-freedom boundary gates.
- [x] Anti-pattern catalog locked with negative failure mode gates (`DoF = 0`).
- [x] Curriculum integration verified in `curriculum/faculty-systems/FOUNDATIONS.md` (SYS-127).
- [x] Full-sweep verification green (`python verify.py --verify-all`).
- [x] Git Merkle tree sealed and synchronized with remote repository.
