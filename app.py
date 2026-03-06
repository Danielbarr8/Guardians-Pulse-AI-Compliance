import sentry_sdk

sentry_sdk.init(
    dsn="https://a023deae6c13e140b4d502d9db98303b@o4510993280139264.ingest.us.sentry.io/4510996074004480",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
)
import streamlit as st
from transformers import pipeline

st.title("🛡️ Guardian's Pulse: AI Compliance Engine")
text_input = st.text_area("Enter AI Output to Audit:")

if text_input:
    # This is the 'Super Code' logic that audits the AI
    classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    result = classifier(text_input)
    st.write("Compliance Status:", result[0]['label'])
