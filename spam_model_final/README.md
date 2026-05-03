# 🛡️ BERT ile Türkçe Spam Mesaj Algılama (SMS)

Bu proje, **BERT (Turkish Cased)** mimarisi kullanılarak metin tabanlı mesajların "Güvenli (Ham)" veya "Spam" olarak sınıflandırılması amacıyla geliştirilmiştir. Proje kapsamında modelimiz hem global İngilizce veri setleri hem de kapsamlı Türkçe SMS veri setleri üzerinde test edilmiştir.

## 📊 Başarı Metrikleri ve Analiz

Modelimiz özellikle Türkçe spam mesajları yakalamada üstün bir performans sergilemiştir.

### 1. Türkçe Veri Seti Sonuçları (En Yüksek Başarı)
![Türkçe Veri Seti Analizi](Screenshot_20_2.png)
*   **Spam Yakalama Oranı (Recall): %98**
*   **Analiz:** 747 adet gerçek spam mesajın **730 tanesi** model tarafından doğru tespit edilmiştir. 
*   **Güvenli Mesaj Koruması:** Gerçek mesajları spam olarak işaretleme hatası (False Positive) minimum düzeyde tutulmuştur.

### 2. İngilizce Veri Seti Sonuçları
![İngilizce Veri Seti Analizi](Screenshot_19_2.png)
*   **Doğruluk (Accuracy): %82**
*   **Analiz:** Modelin global metinlerdeki genel karakteristiğini ölçmek için kullanılmıştır.

---

## 🚀 Model Dosyalarına Erişim

GitHub dosya boyutu limitleri (25MB+) nedeniyle ana ağırlık dosyası (`model.safetensors`) harici olarak tutulmaktadır. 

1.  `spam_model_final` klasöründeki yardımcı dosyaları indirin.
2.  Aşağıdaki linkten ana model dosyasını indirip aynı klasöre yerleştirin:
       🔗 [Model Ağırlıklarını İndir]([LİNKİ_BURAYA_YAPISTIR](https://drive.google.com/file/d/1tVSFfuttv-ChKdvGP_EgqZqODUiZ5yTZ/view?usp=drive_link)

## 🛠️ Teknik Özellikler
*   **Mimari:** BERT-base-turkish-cased
*   **Kapasite:** 512 Token (Ortalama 400-500 kelimeye kadar yüksek performans)
*   **Kütüphaneler:** Transformers, PyTorch, Scikit-learn, Pandas


