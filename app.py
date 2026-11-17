import streamlit as st
import requests

st.set_page_config(page_title="چت‌بات من", page_icon="🤖")
st.title("🤖 چت‌بات هوش مصنوعی")

API_KEY = "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"
URL = "https://api.groq.com/openai/v1/chat/completions"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("پیامت رو بنویس..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("در حال فکر کردن..."):
            headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
            data = {
                "model": "openai/gpt-oss-120b",
                "messages": [{"role": "system", "content": "فقط فارسی جواب بده"}] + st.session_state.messages
            }
            r = requests.post(URL, headers=headers, json=data)
            if r.status_code == 200:
                response = r.json()["choices"][0]["message"]["content"]
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
