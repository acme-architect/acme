# RFC REQUEST: ENTERPRISE C/C++ BROWNFIELD INSPECTOR & CONTINUOUS ARCHITECTURE STREAM (SPEC-030 / SPEC-031)
> **Reporting Client / Node:** acme-downstream-client  
> **Status:** CANDIDATE_REQUEST  
> **Target Faculty:** faculty-systems  
> **Anchored Theses:** THESIS-017, THESIS-022, THESIS-025  

---

## 1. OBSERVED FRICTION (WHAT BROKE?)
- **Context:** Enterprise client systems environments (Carrier-grade NAC appliances, high-throughput SIEM/DPI sensors, and distributed core engines) rely heavily on 10-20 year-old undocumented C/C++ legacy codebases.
- **Root Tension:** 
  1. Teams suffer from severe memory safety debt (unmonitored buffer overflows, memory leaks, use-after-free, CWE-119/416), where original architects have departed and modern engineers avoid refactoring out of fear.
  2. Architecture governance in enterprise agile processes (E-AUP) suffers from cycle time dilation: PRs remain idle for >72 hours awaiting manual architectural sign-off, without cryptographic Merkle alignment between Jira tasks, PR lifecycles, and commit hashes.

---

## 2. AD-HOC WORKAROUND (HOW WAS WORK PRESERVED?)
- **Immediate Mitigation:** Ad-hoc manual code reviews, fragmented Valgrind runs without deterministic spec integration, and subjective status meetings.
- **Residual Risk:** Undetected critical security exploits, regulatory compliance failures (NIS2, ISO 27001), and unbounded delivery lead times.

---

## 3. PROPOSED HYPOTHESIS & DUAL SPECIFICATION
- **A. Proposed Lex (Hard Invariants, DoF=0):**
  - **INV-BROWNFIELD-01 (Deterministic Memory Safety Harness):** Every legacy C/C++ inspection candidate must pass Clang AddressSanitizer/LeakSanitizer with zero memory leaks (`assert asan_leak_bytes == 0`) and zero critical memory-corruption CWEs.
  - **INV-CAS-01 (Cryptographic Flow Provenance):** Every delivery artifact MUST cryptographically bind Jira task IDs, PR lifecycle timestamps, and Git Merkle commit SHAs.
  - **INV-CAS-02 (Flow Efficiency Lead Time Ceiling):** PR idle review duration is strictly bounded to P95 $\le 24\text{ hours}$, with cycle times $\le 72\text{ hours}$.
- **B. Proposed Norms (Adaptive Guidance, DoF>=1):**
  - Automated Clang-Tidy `cert-*` and `bugprone-*` lint rules calibrated to codebase age.
  - E-AUP phase gate progression metrics (Inception to Transition) reported in real-time telemetry.
