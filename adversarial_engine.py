#!/usr/bin/env python3
"""
PROJECT ACME: DIALECTICAL ADVERSARIAL SPEC ENGINE
Version: 1.0.0 (Zero-Dependency)
Implements: Cross-Coupled NAND Dialectics & Degrees of Freedom (DoF) Budgeting
"""

import sys
import re

# Configure UTF-8 stdout/stderr buffering on Windows
if sys.platform == "win32":
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

class AdversarialSpecEngine:
    def __init__(self):
        # DoF = 0 olması gereken yerlerde tespit edilecek gevşek sıfatlar
        self.fluff_patterns = [
            r"\bhızlı\b", r"\bgüvenli\b", r"\bkolay\b", r"\bmodern\b",
            r"\bkaliteli\b", r"\byeterli\b", r"\besnek\b", r"\bmakul\b"
        ]

    def audit_dof_table(self, content: str) -> bool:
        """Serbestlik Dereceleri Tablosunun varlığını doğrular."""
        return "TABLE OF DEGREES OF FREEDOM" in content or "SERBESTLİK DERECELERİ BÜTÇESİ" in content

    def critic_evaluate(self, spec_text: str) -> dict:
        """Spec-B (Çürütücü / Eleştirmen) Rolü: Gedik ve serbestlik sızıntısı arar."""
        issues = []
        
        # 1. DoF Tablosu Kontrolü
        if not self.audit_dof_table(spec_text):
            issues.append("EKSİK DOF TABLOSU: Sistem serbestlik derecelerini bütçelememiş.")

        # 2. Ölçülemeyen Sıfat (Fluff / DoF Sızıntısı) Taraması
        for pattern in self.fluff_patterns:
            matches = re.findall(pattern, spec_text, re.IGNORECASE)
            if matches:
                issues.append(f"ÖLÇÜLEMEYEN NİTELEME: '{matches[0]}' ifadesi sayısal bir DoF sınırına bağlanmamış.")

        # 3. Via Negativa Tabanı (En az 3 negatif kısıt)
        negatives = len(re.findall(r"(?:YASAK|INVARIANT|NEVER|REJECT)", spec_text))
        if negatives < 3:
            issues.append(f"YETERSİZ KISIT: Yalnızca {negatives} negatif kısıt bulundu. En az 3 kısıt şarttır.")

        # 4. Kabul Kriteri (DoD) Matematiksel Kanıt Denetimi
        dod_items = re.findall(r"- \[[ x]\] (.+)", spec_text)
        if not dod_items:
            issues.append("EKSİK DoD: Doğrulanabilir kabul kriteri maddesi bulunamadı.")
        else:
            for item in dod_items:
                if not re.search(r"assert|exit_code|[<>=]{1,2}|\b\d+\b", item):
                    issues.append(f"ÖLÇÜLEMEYEN DoD: '{item}' bir test fonksiyonuna veya eşiğe dayanmıyor.")

        return {
            "verdict": "ACCEPT" if not issues else "REJECT",
            "issues": issues
        }

    def co_verify(self, core_spec: str, project_spec: str) -> bool:
        """Çift Yönlü Doğrulama: Proje şartnamesi çekirdek hakemi bozamaz."""
        core_eval = self.critic_evaluate(core_spec)
        proj_eval = self.critic_evaluate(project_spec)
        
        if core_eval["verdict"] != "ACCEPT":
            print(f"[FAIL] Çekirdek Anayasa Zafiyeti: {core_eval['issues']}")
            return False
            
        if proj_eval["verdict"] != "ACCEPT":
            print(f"[FAIL] Proje Şartname Zafiyeti: {proj_eval['issues']}")
            return False

        print("[PASS] Çift Yönlü Doğrulama Mühürlendi: Hem çekirdek hem proje kurşun geçirmez.")
        return True

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python adversarial_engine.py <spec_file.md>")
        sys.exit(1)
        
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        spec_content = f.read()
        
    engine = AdversarialSpecEngine()
    result = engine.critic_evaluate(spec_content)
    
    print(f"--- SPEC EVALUATION REPORT: {sys.argv[1]} ---")
    print(f"KARAR: {result['verdict']}")
    if result["issues"]:
        for issue in result["issues"]:
            print(f"  * {issue}")
        sys.exit(1)
    else:
        print("  * Tebrikler: Şartname sıfır serbestlik sızıntısıyla mühürlendi.")
        sys.exit(0)

if __name__ == "__main__":
    main()
