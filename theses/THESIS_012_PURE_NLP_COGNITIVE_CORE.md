# THESIS SPEC: PURE NLP COGNITIVE CORE & RADICAL CODE PURGE (RFC-009)
> **Candidate Node:** node-012  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-012/thesis-pure-nlp-core`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v2.0.0 (The Pure Semantic Invariant)

---

## 1. KAPSAM VE ÇEKİRDEK NİYET (SCOPE & INTENT)
ACME bir yazılım projesi, bir Python paketi veya yürütülebilir bir script çöplüğü değildir. ACME; büyük dil modellerinin (LLM) latent uzayını hizalayan, anlamsal sınırları çizen ve zemin gerçeğini tutan bağımsız bir bilişsel doktrin deposudur.
Kök depoya mekanik kod dosyalarının (`.py`), test koşucuların veya regex kalıplarının sokulması, kütüphanenin içine beton mikseri sokmakla eşdeğer bir mimari kirlenmedir (domain leakage).
Bu şartnamenin amacı; ACME çekirdeğini tek bir bayt dahi kod barındırmayan saf bir NLP/şartname külliyatına dönüştürmek; yürütme, test ve derleme mekanizmalarını tamamen dış şantiye/harness alanlarına (`acme-lab`, sandbox projeleri) tahliye etmektir.

---

## 2. SERBESTLİK DERECELERİ BÜTÇESİ (TABLE OF DEGREES OF FREEDOM)

| Katman / Varlık | İzin Verilen DoF | Kısıt Tipi | Bilişsel Hakem Kuralı |
| :--- | :--- | :--- | :--- |
| **Kök Depo Dosya Türleri** | **$\text{DoF} = 0$** | *Format Değişmezi* | Depoda `.md` ve `.json` (kütük) haricinde hiçbir programlama dili uzantısı (`.py`, `.sh`, `.js`, `.bin`) bulunamaz. Tespit anında ret. |
| **Anayasal Kurallar** | **$\text{DoF} = 0$** | *Salt Metin / Anayasa* | Yalnızca `CONSTITUTION.md` ve `theses/` altındaki NLP şartnameleri geçerlidir. |
| **Yürütme ve Test Mekaniği** | **$\text{DoF} = 0$** | *Tam Yalıtım (Ejection)* | Tüm Python testleri, hakem scriptleri ve harness araçları `acme-lab` deposuna aittir; ACME kökünde barınamaz. |
| **Semantik Çıkarım (NLP Logic)** | **$\text{DoF} \ge 1$** | *Akışkan Anlambilim* | Modeller, şartnameleri regex ile değil, doğal dilin anlamsal çıkarımıyla (semantic entailment) doğrular. |

---

## 3. DEĞİŞMEZ KISITLAR (VIA NEGATIVA & INVARIANTS)
*   **INVARIANT 1 (Sıfır Kod Değişmezi - Zero-Code Invariant):**  
    Kök depoda (`acme`) hiçbir `.py` dosyası (`verify.py`, `spec_compiler.py`, `adversarial_engine.py` dahil) ve `tests/` dizini yer alamaz. Varlıkları doğrudan anayasal ihlaldir.
*   **INVARIANT 2 (İki Düzlemli Mimari Yalıtımı):**  
    Bilişsel Düzlem (ACME Core: Saf Doktrin) ile İcra Düzlemi (`acme-lab` & `projects/`: Çalıştırılabilir Kod) fiziksel olarak farklı depolarda yaşar. ACME sadece şartname üretir ve saklar; çalıştırma sorumluluğunu üstlenmez.
*   **INVARIANT 3 (Doğal Dil Yürütülebilirliği):**  
    Tüm SPEC ve Tez belgeleri; çalıştırılması için Python'a muhtaç olmayan, salt doğal dille tanımlanmış girdi/çıktı sözleşmeleri, negatif kısıtlar (Via Negativa) ve nesnel kabul kapıları (DoD) içermek zorundadır.

---

## 4. KABUL KRİTERLERİ (DEFINITION OF DONE - DoD)
- [ ] `theses/THESIS_012_PURE_NLP_COGNITIVE_CORE.md` dosyası UTF-8 No-BOM formatında oluşturulmuş olmalı.
- [ ] `verify.py`, `spec_compiler.py`, `adversarial_engine.py` dosyaları ve `tests/` klasörü `acme` kök deposundan Git geçmişi korunarak silinmeli (`git rm`).
- [ ] Kök depoda `Get-ChildItem -Recurse -Filter *.py` taraması 0 (sıfır) dosya döndürmeli.
- [ ] `registry/graduates.json` kütüğüne 12. akredite mezun olarak `node-012` diploması işlenmeli.
- [ ] Değişiklikler `main` dalına `--no-ff` ile birleştirilmeli.
- [ ] `v2.0.0` sürüm etiketi basılmalı ve `acme-v2.0.0.bundle` arşivi diske mühürlenmeli.
- [ ] Çalışma ağacı `working tree clean` olmalı.
