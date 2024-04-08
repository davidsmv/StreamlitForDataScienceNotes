import streamlit as st
from transformers import pipeline

st.title("Hugging Face Demo")
text = st.text_input("Enter text to analize")
model = pipeline("sentiment-analysis")

if text:
    result = model(text)
    print(result)
    st.write("Sentiment: ", result[0]["label"])
    st.write("Confidence: ", result[0]["score"])