import streamlit as st
from rag_engine.rag_chain import generate_answer

st.set_page_config(page_title="Endian Sales Assistant", layout="wide")
st.title("💡 Endian Sales Assistant (RAG)")

query = st.text_area("Ask a question about your internal documents:")
if st.button("Get Answer") and query:
    with st.spinner("Thinking..."):
        answer = generate_answer(query)
        st.markdown(answer)

