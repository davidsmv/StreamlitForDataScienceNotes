import streamlit as st
from transformers import pipeline
import openai
from openai import OpenAI
import json

st.title("Hugging Face Demo")
text = st.text_input("Enter text to analize")

@st.cache_resource()
def get_model():
    return pipeline("sentiment-analysis")
model = get_model()

if text:
    result = model(text)
    st.write("Sentiment: ", result[0]["label"])
    st.write("Confidence: ", result[0]["score"])



st.title("OpenAI Version")
analyze_button = st.button("Analyze Text")
openai.api_key = st.secrets["OPENAI_API_KEY"]

if analyze_button:
    client = OpenAI()

    messages = [
        {"role": "system",
         "content":  """You are a helpful sentiment analysis assistant.
            You always respond with the sentiment of the text you are given and the confidence of your sentiment analysis with a number between 0 and 1"""},
        {"role": "user",
         "content": f"Sentiment analysis of the following text: {text}"}
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    sentiment = response.choices[0].message.content
    st.write(sentiment)