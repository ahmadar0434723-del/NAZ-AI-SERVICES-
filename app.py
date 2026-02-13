import streamlit as st
import google.generativeai as genai

# آپ کی API Key
API_KEY = "AIzaSyCLMzdNy4KCnqgaWIaRa9wErF5PjImhgZw"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="NAZ AI", page_icon="💎")
st.title("💎 NAZ AI PRO")

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("مجھ سے کچھ بھی پوچھیں..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # جدید ترین ماڈل جو 404 نہیں دے گا
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error("گوگل سسٹم ابھی آپ کی Key ایکٹیو کر رہا ہے، براہ کرم 1 منٹ انتظار کریں۔")
