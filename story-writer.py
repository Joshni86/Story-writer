from transformers import pipeline
import streamlit as st
st.title("Creati-story AI")
@st.cache_resource
def load_model():
    return pipeline("text-generation",model="mistralai/Mistral-7B-Instruct-v0.2")

model=load_model()

if "messages" not in st.session_state:
    st.session_state.messages = []

# messages are still there - stateful basically
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Write your story here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = model(prompt, max_length=200, do_sample=True, temperature=0.7, num_return_sequences=1)[0]['generated_text']
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        # with st.spinner("Generating story..."):
        st.markdown(response)
            