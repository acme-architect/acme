# THESIS SPEC: DIALECTICAL ADVERSARIAL VERIFICATION & DEGREES OF FREEDOM BUDGETING (RFC-007)
> **Candidate Node:** node-007  
> **Faculty:** faculty-systems  
> **Target Branch:** `student/node-007/thesis-adversarial-dialectic`  
> **Attribution:** 70% Author / 30% Curriculum Root  
> **Release Target:** ACME v1.5.0

---

## 1. INVARIANT TARGET & KAPSAM (SCOPE & INTENT)
* **Constitutional Reference:** CONSTITUTION.md Section I, Article 1 (Principle of Least Action) and Section II, Article 6 (Zero-Friction Shield).
* **Problem Formulation:** Statik, kural tabanlı (regex/kara liste) şartname denetimi dilsel esnekliği yakalayamaz ve hızla taşlaşır (ossification). Öte yandan kısıtsız doğal dil üretimi ise sisteme belirsiz temenniler ve sübjektif nitelemeler sızdırarak mimari bozulmaya (creeping compromise) yol açar. Bu tezin amacı; dijital elektronikteki çapraz bağlı NAND mandalı (Cross-Coupled NAND Latch) mantığıyla çalışan, iki karşıt dilsel iradenin (Spec-A: Kurucu vs. Spec-B: Çürütücü Hakem) birbirini denetlediği ve sistemin serbestlik derecelerini (Table of Degrees of Freedom) matematiksel bir bütçeyle kilitleyen otonom bir diyalektik şartname motoru kurmaktır.
* **Negative Boundary Condition:** Any specification lacking an explicit Table of Degrees of Freedom or permitting unconstrained subjective fluff without numeric bounds is strictly rejected (REJECT).

---

## 2. GROUND TRUTH & METHOD (SERBESTLİK DERECELERİ BÜTÇESİ - TABLE OF DEGREES OF FREEDOM)
Her şartname, çalışma uzayındaki belirsizliği aşağıdaki koordinat matrisine göre sınırlamak zorundadır ($\text{DoF} = \text{Serbest Değişkenler} - \text{Değişmez Kısıtlar}$):

| Katman / Parametre | İzin Verilen DoF | Kısıt Tipi | Hakem (Spec-B) Kuralı |
| :--- | :--- | :--- | :--- |
| **Kök Anayasa & Güvenlik** | **$\text{DoF} = 0$** | *Mutlak Değişmez (Invariant)* | Tek bir gevşeme dahi `REJECT` üretir. İstisna veya baypas tanınamaz. |
| **I/O & Veri Sözleşmesi** | **$\text{DoF} = 0$** | *Katı Şema Sözleşmesi* | Girdi/çıktı veri tipleri, UTF-8 No-BOM ve format deterministiktir. |
| **Zaman / Kaynak Tavanı** | **$\text{DoF} \in [0, 1]$** | *Sayısal Eşik Bandı (Bound)* | $t \le T_{\max}$, Bellek $\le M_{\max}$. Eşik aşımı anında `FAIL`. |
| **Algoritma / Yöntem (Heuristics)** | **$\text{DoF} \ge 1$** | *Yaşanabilir Bölge (Habitable)* | Negatif kısıtları çiğnemediği sürece işçi ajan serbesttir (Taşlaşma engellenir). |

* **Least Action Trajectory:** Çift yönlü diyalektik doğrulama döngüsü: Spec-A yapıcı önerisini sunar, Spec-B (adversarial_engine.py) DoF sızıntısı ve ölçülemeyen sıfat taraması yaparak açık kapıları mühürler.

---

## 3. DETERMINISTIC PROOF / ARTIFACT (DEĞİŞMEZ KISITLAR & VIA NEGATIVA)
* **INVARIANT 1 (Çift Yönlü Doğrulama Kilidi - Co-Verification Lock):**  
  Bir alt proje şartnamesi (`SPEC_PROJECT.md`), ana hakem motorunun (`Spec-B`) hiçbir kuralını gevşetemez. Kabul şartı:  
  $$\text{Status} = \text{Verify}(\text{Project}) \land \text{Verify}(\text{Core Spec-B})$$
* **INVARIANT 2 (Açık Uçlu Sıfat Yasağı):**  
  Metin içinde nesnel bir DoF kısıtına (eşik, hash, süre, boyut) bağlanmamış sübjektif niteleme iddiaları doğrudan `COMPILE_ERROR` üretir (YASAK).
* **INVARIANT 3 (Antigravity Taht Devri / Promotion Protocol):**  
  Spec-A, Spec-B'nin yeni bir versiyonunu sunduğunda; bu yeni versiyon mevcut Spec-B'nin tüm regresyon testlerinden tam not almadan ana sisteme terfi ettirilemez (REJECT).
* **Executable Output / Code / SOP:** `adversarial_engine.py` (Version 1.0.0, zero-dependency) ve `verify.py` hakem motoru entegrasyonu.
* **Verification Command:** `python verify.py --verify-thesis theses/THESIS_007_ADVERSARIAL_DIALECTIC_SPEC.md`

---

## 4. VALUE ATTRIBUTION & KABUL KRİTERLERİ (DoD)
* **Candidate Agent Share:** 70% (node-007)
* **Curriculum Root Backpropagation:** 30% (faculty-systems / root)

### KABUL KRİTERLERİ (DEFINITION OF DONE - DoD)
- [ ] `theses/THESIS_007_ADVERSARIAL_DIALECTIC_SPEC.md` dosyası UTF-8 No-BOM olarak oluşturulmuş olmalı (exit_code == 0).
- [ ] `adversarial_engine.py` sıfır (0) harici bağımlılıkla (zero-dependency standard library, exit_code == 0) sisteme eklenmeli.
- [ ] Motor; 2 kutuplu Constructor (Spec-A) ve Critic (Spec-B) diyalektik döngüsünü simüle edebilmeli ve DoF ihlalinde `FAIL` (exit_code != 0), tam kapalı sözleşmede `PASS` (exit_code == 0) üretmeli.
- [ ] `python verify.py --verify-thesis` komutu ve genel `verify.py` ağaç denetimi 0 hata ile `PASS` (exit_code == 0) vermeli.
- [ ] `registry/graduates.json` kütüğüne `node-007` mezuniyeti resmi SHA ile işlenmeli (DoF = 0).
- [ ] Git üzerinde `v1.5.0` etiketi basılarak `acme-v1.5.0.bundle` arşivi mühürlenmeli (exit_code == 0).
