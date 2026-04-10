import streamlit as st
import joblib

model = joblib.load("model_mbti.pkl")

st.set_page_config(page_title="PersonaAI", page_icon="🧠")

st.title("🧠 PersonaAI - MBTI Predictor")
st.caption("Discover your personality type using AI")

user_input = st.text_area("Tell me about yourself...")

if st.button("Predict"):
    if user_input:
        pred = model.predict([user_input])[0]
        prob = model.predict_proba([user_input]).max()

        st.success(f"🧬 Your MBTI: {pred}")
        st.write(f"Confidence: {prob*100:.2f}%")

        descriptions = {
            "INFP": "Idealistic, creative, and guided by strong values.",
            "INTJ": "Strategic thinker with long-term vision.",
            "ENTP": "Energetic innovator who loves challenges.",
        }

        if pred in descriptions:
            st.info(descriptions[pred])
    else:
        st.warning("Please enter some text.")