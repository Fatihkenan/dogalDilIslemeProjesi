# 🛡️ BERT ile Türkçe ve İngilizce Spam Mesaj Algılama (SMS)

Bu proje, **BERT (Turkish Cased)** mimarisi kullanılarak metin tabanlı mesajların "Güvenli (Ham)" veya "Spam" olarak sınıflandırılması amacıyla geliştirilmiştir.

## 📊 Performans ve Test Sonuçları

Modelin başarısı, karmaşıklık matrisi (confusion matrix) ve sınıflandırma raporları ile doğrulanmıştır. 

### 1. Türkçe Veri Seti Analizi
![Türkçe Veri Sonucu](turkce_veri_analizi.png)
*   **Doğruluk (Accuracy):** %86
*   **Analiz:** Model, Türkçe karakter yapısına duyarlı olduğu için yerel SMS kalıplarında yüksek başarı sergilemiştir.

### 2. İngilizce (Global) Veri Seti Analizi
![İngilizce Veri Sonucu](ingilizce_veri_analizi.png)
*   **Doğruluk (Accuracy):** %82
*   **Analiz:** Modelin farklı dillerdeki genel spam karakteristiğini anlama kapasitesi ölçülmüştür.

---

## 🚀 Kurulum ve Kullanım

### ⚠️ Önemli: Model Ağırlıkları
GitHub dosya boyutu limitleri nedeniyle, modelin ana ağırlık dosyası (`model.safetensors`) bu depoda yer almamaktadır. 

1. Aşağıdaki linkten ana model dosyasını indirin:
    *   🔗 **[Model Ağırlıklarını İndir (https://drive.google.com/file/d/1tVSFfuttv-ChKdvGP_EgqZqODUiZ5yTZ/view?usp=drive_link)]**
2. İndirdiğiniz dosyayı `spam_model_final/` klasörünün içine yerleştirin.
3. ARAYÜZ 
<img width="847" height="758" alt="Ekran görüntüsü 2026-06-02 120218" src="https://github.com/user-attachments/assets/c50a4657-64b6-4e07-9422-d3c7b5cc1d53" />


