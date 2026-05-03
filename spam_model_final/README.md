# 🛡️ BERT ile Türkçe ve İngilizce Spam Mesaj Algılama (SMS)

Bu proje, **BERT (Turkish Cased)** mimarisi kullanılarak metin tabanlı mesajların "Güvenli (Ham)" veya "Spam" olarak sınıflandırılması amacıyla geliştirilmiştir. Proje, hem yerel Türkçe SMS veri setleri hem de global İngilizce veri setleri üzerinde test edilerek çok dilli başarı performansı ölçülmüştür.

## 📊 Performans ve Test Sonuçları

Modelin başarısı, karmaşıklık matrisi (confusion matrix) ve sınıflandırma raporları ile doğrulanmıştır. 

### 1. Türkçe Veri Seti Analizi
![Türkçe Veri Sonucu](turkce_veri_analizi.png)
*   **Doğruluk (Accuracy):** %86
*   **Analiz:** Model, Türkçe karakter yapısına (Turkish-Cased) duyarlı olduğu için yerel SMS kalıplarında yüksek başarı sergilemiştir.

### 2. İngilizce (Global) Veri Seti Analizi
![İngilizce Veri Sonucu](ingilizce_veri_analizi.png)
*   **Doğruluk (Accuracy):** %82
*   **Analiz:** Modelin farklı dillerdeki genel spam karakteristiğini anlama kapasitesi ölçülmüştür.

---

## 🚀 Kurulum ve Kullanım

### ⚠️ Önemli: Model Ağırlıkları
GitHub'ın dosya boyutu limitleri (25MB+) nedeniyle, modelin ana ağırlık dosyası olan **`model.safetensors`** (yaklaşık 442MB) bu depoda yer almamaktadır. 

Modeli çalıştırmak için:
1.  Bu depodaki tüm dosyaları indirin.
2.  Aşağıdaki Google Drive linkinden ana model dosyasını indirin:
    *   🔗 **[Model Ağırlıklarını İndir ((https://drive.google.com/file/d/1tVSFfuttv-ChKdvGP_EgqZqODUiZ5yTZ/view?usp=drive_link))]**
3.  İndirdiğiniz `model.safetensors` dosyasını `spam_model_final/` klasörünün içine yerleştirin.

### Teknik Özellikler
*   **Mimari:** BERT-base-turkish-cased
*   **Giriş Limiti:** 512 Token (Ortalama 400-500 kelimeye kadar tam metin analizi sağlar).
*   **Kütüphaneler:** Transformers, PyTorch, Pandas, Scikit-learn.

---

## 📂 Proje Yapısı
```text
├── spam_model_final/       # Model konfigürasyon dosyaları
├── dataset/                # Eğitim ve test veri setleri
├── projenin_kodlari.ipynb  # Ana çalışma dosyası
├── turkce_veri_analizi.png  # Türkçe başarı metriği görseli
├── ingilizce_veri_analizi.png # İngilizce başarı metriği görseli
└── README.md               # Proje dokümantasyonu
