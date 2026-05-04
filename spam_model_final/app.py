import streamlit as st
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import time

# Sayfa ayarları
st.set_page_config(page_title="GüvenliMesaj", page_icon="🛡️", layout="centered")

# Modeli cache ile yükleme
@st.cache_resource
def load_model():
    model_path = "./benim_modelim" 
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

st.title("🛡️ GüvenliMesaj SMS Analizi")
st.markdown("Yapay zeka destekli Türkçe oltalama (phishing) ve spam tespit sistemi.")

try:
    tokenizer, model = load_model()
except Exception as e:
    st.error(f"Model yüklenirken bir hata oluştu: {e}")

# Kullanıcı Giriş Alanı (Sadece temiz bir textbox)
user_input = st.text_area("Mesaj Metni:", height=130, placeholder="Analiz edilecek mesajı buraya yapıştırın veya yazın...")

# Analiz Butonu
if st.button("Mesajı Analiz Et", type="primary", use_container_width=True):
    if user_input.strip() == "":
        st.warning("Lütfen analiz etmek için bir metin girin.")
    else:
        with st.spinner('BERT Modeli metnin bağlamını analiz ediyor...'):
            start_time = time.time() # Süre ölçümü başlat
            
            inputs = tokenizer(user_input, return_tensors="pt", truncation=True, max_length=512)
            with torch.no_grad():
                outputs = model(**inputs)
                predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
                
            spam_prob = predictions[0][1].item()
            inference_time = time.time() - start_time # Süre ölçümü bitir
            
            st.divider()
            st.subheader("📊 Yapay Zeka Kararı")
            
            # Sonuç Görselleştirmesi
            if spam_prob > 0.5:
                st.error("🚨 **DİKKAT! RİSKLİ MESAJ.** Bu metnin bir SPAM veya OLTALAMA olma ihtimali yüksek.")
            else:
                st.success("✅ **GÜVENLİ.** Bu mesaj kişisel veya zararsız görünüyor.")
                
            st.markdown(f"**Tehlike Skoru: %{spam_prob * 100:.1f}**")
            
            # JÜRİ İÇİN TEKNİK BİLGİ KUTUSU
            with st.expander("⚙️ Arka Plan Detayları (Tıklayınız)"):
                st.write(f"- **Kullanılan Mimari:** BERT (Sequence Classification)")
                st.write(f"- **Karar Süresi:** {inference_time:.3f} saniye")
                st.write(f"- **Sınıf 0 (Ham) Olasılığı:** %{(1 - spam_prob) * 100:.2f}")
                st.write(f"- **Sınıf 1 (Spam) Olasılığı:** %{spam_prob * 100:.2f}")