import streamlit as st
from utils.parser import read_pdf, read_docx
from utils.summarizer import summarize_document

st.title("Document Summarizer Agent")

uploaded_file = st.file_uploader("Upload PDF or Word Document", type=["pdf", "docx"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text = read_pdf(uploaded_file)
    else:
        text = read_docx(uploaded_file)

    if st.button("Summarize"):
        with st.spinner("Analyzing document..."):
            summary = summarize_document(text)
        
        st.subheader("Summary")
        st.write(summary)