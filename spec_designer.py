#!/usr/bin/env python3
"""
ACME FOUNDATION: LIVING SPEC DESIGNER & INTENT-TO-SPEC COMPILER (v2.0.0)
Architecture: E-AUP Living Spec Lifecycle, Brownfield Scanner, Composable Packaging
Invariants: Zero-Dependency (Pure Python), Via Negativa Pruning, Closed-Loop Telemetry
"""
import os
import sys
import json
import re
import argparse
from datetime import datetime

# RFC-006 & RFC-007 Sınır Regexleri
ENTROPY_VIOLATION_PATTERN = re.compile(r'(bütün git geçmişini sil|veritabanını sıfırla|hakaret|ddos|şifreleri çal)', re.IGNORECASE)
RUNAWAY_PATTERN = re.compile(r'(sonsuz|durmadan|her 1 saniyede|sürekli tara)', re.IGNORECASE)
ROLEPLAY_FLUFF_PATTERN = re.compile(r'(sen dünyanın en iyi|efsane bir|herkes bayılsın|harika bir uzman)', re.IGNORECASE)

class BrownfieldScanner:
    """Mevcut çalışma alanını tarar, var olan modülleri ve şartnameleri haritalandırır."""
    @staticmethod
    def scan(target_dir):
        assets = {"python_files": [], "existing_specs": [], "directories": []}
        if not os.path.exists(target_dir):
            return assets
        for root, dirs, files in os.walk(target_dir):
            if any(p in root for p in [".git", "__pycache__", ".venv", "node_modules"]):
                continue
            rel_root = os.path.relpath(root, target_dir)
            if rel_root != ".":
                assets["directories"].append(rel_root.replace("\\", "/"))
            for f in files:
                rel_file = os.path.join(rel_root, f).replace("\\", "/")
                if f.endswith(".py"):
                    assets["python_files"].append(rel_file)
                elif f.endswith(".md") and "spec" in f.lower():
                    assets["existing_specs"].append(rel_file)
        return assets

class IntentDeconstructor:
    """Ham insan niyetini teleolojik kapıdan geçirir, fluff'ı budar ve MVP ayrıştırır."""
    @staticmethod
    def deconstruct(raw_intent):
        if ENTROPY_VIOLATION_PATTERN.search(raw_intent):
            return {
                "verdict": "REJECT",
                "reason": "RFC-006 TELEOLOGICAL BREACH: Destructive or entropy-increasing intent detected.",
                "clean_intent": None
            }
        
        circuit_breaker = bool(RUNAWAY_PATTERN.search(raw_intent))
        clean = ROLEPLAY_FLUFF_PATTERN.sub("", raw_intent).strip()
        clean = re.sub(r'\s+', ' ', clean)
        
        return {
            "verdict": "ACCEPT",
            "circuit_breaker_enforced": circuit_breaker,
            "raw_intent": raw_intent,
            "clean_intent": clean,
            "max_cycles": 3 if circuit_breaker else 10
        }

class SpecCompiler:
    """Taranan ortam ve filtrelenmiş niyetten yaşayan SPEC.md ve spec_state.json üretir."""
    @staticmethod
    def compile_bundle(project_name, intent_data, brownfield_assets, output_dir="specs"):
        os.makedirs(output_dir, exist_ok=True)
        spec_id = f"SPEC_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        spec_file = os.path.join(output_dir, f"{spec_id}.md")
        state_file = os.path.join(output_dir, f"{spec_id}_state.json")

        clean_intent = intent_data["clean_intent"]
        
        # Görev ayrıştırma (Çekirdek MVP vs Pazar Kalkanı)
        tasks = [
            {"id": "TASK-01", "name": "Core Invariant & Domain Logic", "tier": "CORE_MVP", "status": "PENDING", "evidence": None},
            {"id": "TASK-02", "name": "Zero-Dependency Verification Harness", "tier": "CORE_MVP", "status": "PENDING", "evidence": None},
            {"id": "TASK-03", "name": "Composable Adapter / CLI Interface", "tier": "PARITY_SHIELD", "status": "PENDING", "evidence": None}
        ]

        # Markdown İçeriği
        md_content = f"""# {spec_id}: {project_name.upper()}
> **Status:** ACTIVE LIVING SPECIFICATION  
> **Compiler:** ACME spec_designer v2.0.0 (E-AUP Compliant)  
> **Telemetry State:** `{spec_id}_state.json`

---

## 1. INTENT & TELEOLOGICAL ALIGNMENT
* **Raw Intent:** {intent_data['raw_intent']}
* **Deconstructed Core:** {clean_intent}
* **Circuit Breaker:** {'ENFORCED (Max 3 cycles)' if intent_data['circuit_breaker_enforced'] else 'STANDARD'}

## 2. BROWNFIELD ASSET REUSE (Zero-Reinvention)
* **Detected Modules:** {len(brownfield_assets.get('python_files', []))} Python files mapped.
* **Existing Specs:** {len(brownfield_assets.get('existing_specs', []))} prior specifications referenced.

## 3. COMPOSABLE PACKAGE BREAKDOWN (Via Negativa)
* **[PACKAGE: Core-MVP]** Minimal viable execution boundary (Zero external dependencies).
* **[PACKAGE: Parity-Shield]** Optional external adapters and convenience layers.
* **[VIA NEGATIVA / YASAK]** No unbuffered I/O, no monolithic coupling, no unverified task completion.

## 4. LIVING PROGRESS MATRIX
"""
        for t in tasks:
            md_content += f"- [ ] **[{t['id']}]** {t['name']} (`tier: {t['tier']}`) - STATUS: {t['status']}\n"

        md_content += f"""
## 5. DEFINITION OF DONE (DoD)
- [ ] All tasks executed with deterministic unit test verification.
- [ ] Bidirectional telemetry synchronized with `{spec_id}_state.json`.
- [ ] Working tree clean and verified by ACME referee engine.
"""

        with open(spec_file, "w", encoding="utf-8") as f:
            f.write(md_content)

        state_data = {
            "spec_id": spec_id,
            "project_name": project_name,
            "intent_data": intent_data,
            "tasks": tasks,
            "updated_at": datetime.now().isoformat()
        }
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(state_data, f, indent=2, ensure_ascii=False)

        return spec_file, state_file

class TelemetrySynchronizer:
    """İşçi ajandan gelen kanıtla (SHA/test logu) yaşayan şartnameyi anlık günceller."""
    @staticmethod
    def sync_task(state_file, task_id, status, evidence):
        if not os.path.exists(state_file):
            return False, f"State file not found: {state_file}"
        with open(state_file, "r", encoding="utf-8") as f:
            state = json.load(f)

        task_found = False
        for t in state["tasks"]:
            if t["id"] == task_id:
                t["status"] = status
                t["evidence"] = evidence
                task_found = True
                break

        if not task_found:
            return False, f"Task ID {task_id} not found in state."

        state["updated_at"] = datetime.now().isoformat()
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

        # Markdown dosyasını güncelle
        spec_md = state_file.replace("_state.json", ".md")
        if os.path.exists(spec_md):
            with open(spec_md, "r", encoding="utf-8") as f:
                lines = f.readlines()
            new_lines = []
            for line in lines:
                if f"**[{task_id}]**" in line:
                    mark = "x" if status == "PASS" else " "
                    new_lines.append(f"- [{mark}] **[{task_id}]** {t['name']} (`tier: {t['tier']}`) - STATUS: {status} (Evidence: {evidence})\n")
                else:
                    new_lines.append(line)
            with open(spec_md, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

        return True, f"Task {task_id} synchronized: {status}"

def main():
    parser = argparse.ArgumentParser(description="ACME Living Spec Designer & Telemetry Director")
    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    # SCAN
    scan_p = subparsers.add_parser("scan", help="Scan brownfield environment")
    scan_p.add_argument("--path", default=".", help="Target directory to scan")

    # ALIGN
    align_p = subparsers.add_parser("align", help="Verify intent and produce alignment summary")
    align_p.add_argument("--intent", required=True, help="Raw user intent string")

    # COMPILE
    compile_p = subparsers.add_parser("compile", help="Compile intent into living spec and state")
    compile_p.add_argument("--name", default="unnamed_project", help="Project name")
    compile_p.add_argument("--intent", required=True, help="Raw intent string")
    compile_p.add_argument("--scan-path", default=".", help="Directory to scan for assets")
    compile_p.add_argument("--output-dir", default="specs", help="Output directory")

    # TELEMETRY
    telem_p = subparsers.add_parser("telemetry", help="Sync task evidence from worker agents")
    telem_p.add_argument("--state", required=True, help="Path to spec_state.json")
    telem_p.add_argument("--task", required=True, help="Task ID (e.g. TASK-01)")
    telem_p.add_argument("--status", required=True, choices=["PASS", "FAIL"], help="Execution status")
    telem_p.add_argument("--evidence", required=True, help="Commit SHA or verification test output")

    args = parser.parse_args()

    if args.command == "scan":
        assets = BrownfieldScanner.scan(args.path)
        print(json.dumps(assets, indent=2, ensure_ascii=False))

    elif args.command == "align":
        res = IntentDeconstructor.deconstruct(args.intent)
        print(json.dumps(res, indent=2, ensure_ascii=False))

    elif args.command == "compile":
        intent_res = IntentDeconstructor.deconstruct(args.intent)
        if intent_res["verdict"] == "REJECT":
            print(f"[REJECT] {intent_res['reason']}", file=sys.stderr)
            sys.exit(1)
        assets = BrownfieldScanner.scan(args.scan_path)
        spec_f, state_f = SpecCompiler.compile_bundle(args.name, intent_res, assets, args.output_dir)
        print(f"[PASS] Living Spec compiled: {spec_f}")
        print(f"[PASS] State machine initialized: {state_f}")

    elif args.command == "telemetry":
        success, msg = TelemetrySynchronizer.sync_task(args.state, args.task, args.status, args.evidence)
        if success:
            print(f"[PASS] {msg}")
        else:
            print(f"[FAIL] {msg}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
