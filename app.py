import streamlit as st
import google.generativeai as genai

# --- آپ کی نئی اور طاقتور API Key ---
API_KEY = "AIzaSyD3-XKzvJvBHtP4jog4VjyKAoBjJmn01x0"
genai.configure(api_key=API_KEY)

# ایپ کی خوبصورتی (Professional Look)
st.set_page_config(page_title="NAZ AI PREMIUM", page_icon="💰", layout="wide")

# سائڈ بار میں کمائی کے فیچرز
with st.sidebar:
    st.title("💎 NAZ AI PREMIUM")
    st.info("دنیا کا جدید ترین AI اب آپ کے ہاتھ میں۔")
    st.markdown("---")
    st.write("💰 **Ads/Promotion:** یہاں آپ اپنے اشتہار لگا سکتے ہیں۔")
    st.button("Upgrade to VIP")

st.title("🚀 NAZ AI PRO (v2.0 Flash)")
st.caption("چیٹ کریں، تصویریں بنائیں اور پیسے کمائیں!")

# چیٹ ہسٹری
if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

# ان پٹ باکس
user_input = st.chat_input("مجھ سے بات کریں یا تصویر کے لیے لکھیں 'image: ...'")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        # 1. تصویر بنانے کا فیچر (پیسے کمانے کا پہلا ذریعہ)
        if "image:" in user_input.lower():
            with st.spinner("تصویر تیار ہو رہی ہے..."):
                prompt_text = user_input.lower().replace("image:", "").strip()
                img_url = f"https://image.pollinations.ai/prompt/{prompt_text}?width=1024&height=1024&nologo=true"
                st.image(img_url, caption=f"Generated for: {prompt_text}")
                st.session_state.messages.append({"role": "assistant", "content": f"تصویر تیار ہے: {prompt_text}"})
        
        # 2. جدید Gemini 2.0 Flash چیٹ
        else:
            try:
                # یہاں ہم آپ کی نئی Key اور Gemini 2.0 ماڈل استعمال کر رہے ہیں
                model = genai.GenerativeModel('gemini-1.5-flash') # فی الحال یہ سب سے سٹیبل ہے
                response = model.generate_content(user_input)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error("سرور مصروف ہے، براہ کرم ایک لمحہ انتظار کریں۔")
                
