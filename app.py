import streamlit as st
from transformers import pipeline

st.title("🛡️ Guardian's Pulse: AI Compliance Engine")
text_input = st.text_area("Enter AI Output to Audit:")

if text_input:
    # This is the 'Super Code' logic that audits the AI
    classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    result = classifier(text_input)
    st.write("Compliance Status:", result[0]['label'])
