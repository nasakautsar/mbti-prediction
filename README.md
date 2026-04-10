# PersonaAI - MBTI Personality Predictor

PersonaAI is an AI-powered web application that predicts a user's MBTI personality type based on text input using Natural Language Processing (NLP).

## Features

- Predict MBTI personality type from text
- Confidence score for predictions
- Interactive web interface (Streamlit)

## How It Works

The system processes user text using TF-IDF vectorization and applies a machine learning classification model to predict one of the 16 MBTI personality types.

## Tech Stack

- Python
- Scikit-learn
- Streamlit
- NLP (TF-IDF)

## Run Locally

pip install -r requirements.txt
streamlit run app.py

## Example

Input:
"I enjoy spending time alone and thinking deeply about ideas"

Output:
INFP (with confidence score)

## Future Improvements

- Improve model using Deep Learning (BERT)
- Add personality explanations
- Deploy to cloud for public access

## Live Demo
https://mbti-prediction-xxxxx.streamlit.app/

## Author
Nasaka

Developed as an AI portfolio project combining Machine Learning and Psychology.
