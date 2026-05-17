import streamlit as st
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import time

# Sayfa ayarları
st.set_page_config(page_title="GüvenliMesaj Bot", page_icon="🛡️", layout="centered")

# Modeli cache ile yükleme
@st.cache_resource
def load_model():
    model_path = "./benim_modelim" 
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    return tokenizer, model

st.title("🛡️ GüvenliMesaj Sohbet Botu")
st.markdown("Şüphelendiğiniz SMS veya mesajları bana gönderin, inceleyip güvenli olup olmadığını söyleyeyim!")

try:
    tokenizer, model = load_model()
except Exception as e:
    st.error(f"Model yüklenirken bir hata oluştu: {e}")

# 1. Sohbet hafızasını (geçmişi) başlatma
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Merhaba! Ben GüvenliMesaj Bot. Şüpheli bir mesaj mı aldın? Buraya yapıştır, senin için hemen analiz edeyim."}
    ]

# 2. Geçmiş mesajları ekranda gösterme döngüsü
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Alttaki mesaj yazma çubuğu (Chat Input)
if prompt := st.chat_input("Analiz edilecek mesajı buraya yapıştırın..."):
    
    # Kullanıcının mesajını ekrana ve hafızaya ekle
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Yapay Zekanın düşünme ve cevap verme aşaması
    with st.chat_message("assistant"):
        with st.spinner("Bağlamı analiz ediyorum..."):
            start_time = time.time() # Süre ölçümü başlat
            
            # BERT inference (Senin orijinal kodun)
            inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
            with torch.no_grad():
                outputs = model(**inputs)
                predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
                
            spam_prob = predictions[0][1].item()
            inference_time = time.time() - start_time # Süre ölçümü bitir
            
            # Sonuca göre yapay zekanın sohbet cevabını hazırlama
            if spam_prob > 0.5:
                bot_response = f"🚨 **DİKKAT! RİSKLİ MESAJ.**\n\nYaptığım analize göre bu metnin bir **SPAM veya OLTALAMA** olma ihtimali çok yüksek. Lütfen içindeki linklere tıklamayın!\n\n**Tehlike Skoru:** %{spam_prob * 100:.1f}"
            else:
                bot_response = f"✅ **GÜVENLİ.**\n\nBu mesaj kişisel veya zararsız görünüyor. İçiniz rahat olabilir.\n\n**Tehlike Skoru:** %{spam_prob * 100:.1f}"
            
            # Jüri için teknik arka plan detaylarını cevabın altına ekliyoruz
            teknik_detay = f"\n\n---\n*⚙️ **Teknik Bilgi:** Karar Süresi: {inference_time:.3f} sn | Sınıf 0: %{(1 - spam_prob) * 100:.2f} | Sınıf 1: %{spam_prob * 100:.2f}*"
            
            full_response = bot_response + teknik_detay
            
            # Cevabı ekrana bas
            st.markdown(full_response)
            
    # Botun cevabını hafızaya ekle
    st.session_state.messages.append({"role": "assistant", "content": full_response})