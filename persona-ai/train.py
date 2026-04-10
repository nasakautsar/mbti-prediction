import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

df = pd.read_csv("mbti_1.csv", encoding="latin-1")

X = df["posts"]
y = df["type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=3000)),
    ("clf", LogisticRegression(max_iter=2000))
])

model.fit(X_train, y_train)

joblib.dump(model, "model_mbti.pkl")

print("Model berhasil dibuat!")