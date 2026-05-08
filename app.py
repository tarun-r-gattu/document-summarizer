import streamlit as st
from utils.parser import read_pdf, read_docx
from utils.summarizer import summarize_content
from utils.folder_summarizer import summarize_folder
import os

st.title("Document Summarizer Agent")

# uploaded_file = st.file_uploader("Upload PDF or Word Document", type=["pdf", "docx"])
# if uploaded_file:
#     if uploaded_file.type == "application/pdf":
#         text = read_pdf(uploaded_file)
#     else:
#         text = read_docx(uploaded_file)

#     if st.button("Summarize"):
#         with st.spinner("Analyzing document..."):
#             summary = summarize_content(text)
        
#         st.subheader("Summary")
#         st.write(summary)

st.subheader("Summarize Documents within a folder")

folder_path = st.text_input("Enter folder path (local machine)")

if st.button("Summarize Folder"):
    if not folder_path:
        st.error("Please enter a folder path")
    else:
        try:
            with st.spinner("Processing folder..."):
                results = summarize_folder(folder_path)

            for file, summary in results.items():
                filename = os.path.basename(file)

                with st.expander(f"📄 {filename}"):
                    st.write(summary)
                    
        except Exception as e:
            st.error(f"Error: {str(e)}")
