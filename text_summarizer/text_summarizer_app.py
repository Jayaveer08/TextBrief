import streamlit as st
from transformers import pipeline
import os

# Change directory to the one containing the model (if necessary)
# os.chdir(r"C:\Users\N .JAYAVEER\OneDrive\Desktop\Task 2\text_summarizer")

# Load the summarizer model
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# Streamlit UI
st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📝 Text Summarizer App")
st.write("Enter any long text below and get a summarized version using NLP!")

input_text = st.text_area("Enter Text to Summarize", height=300)

if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(input_text, max_length=130, min_length=30, do_sample=False)
            st.success("Summary Generated:")
            st.write(summary[0]['summary_text'])

# To run the app, use the following command in your terminal:
# streamlit run text_summarizer_app.py
