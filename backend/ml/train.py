import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import joblib
import os

# Create artifacts folder if it doesn't exist
os.makedirs("ml/artifacts", exist_ok=True)

# Load some data
X, y = load_iris(return_X_y=True)

# Train a model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, "ml/artifacts/model.joblib")

# Load dataset
df = pd.read_csv("data/tickets.csv")

# Rename columns for consistency (BEST PRACTICE)
df = df.rename(columns={
    "Ticket Description": "text",
    "Ticket Type": "category"
})

# Drop rows with missing values
df = df.dropna(subset=["text", "category"])

X = df["text"]
y = df["category"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

X_train_vec = vectorizer.fit_transform(X_train)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Save artifacts
joblib.dump(model, "ml/artifacts/model.joblib")
joblib.dump(vectorizer, "ml/artifacts/vectorizer.joblib")

print("Model trained and saved successfully")
