import pandas as pd
import re
from urllib.parse import urlparse
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib


def extract_features(url):
    return {
        "url_length": len(url),
        "has_ip": 1 if re.match(r"https?://\d{1,3}(\.\d{1,3}){3}", url) else 0,
        "has_at": 1 if "@" in url else 0,
        "has_hyphen": 1 if "-" in urlparse(url).netloc else 0,
        "has_https": 1 if url.startswith("https://") else 0,
        "subdomain_count": urlparse(url).netloc.count('.')
    }

df = pd.read_csv("phishing/dataset.csv")
df_features = df["url"].apply(extract_features).apply(pd.Series)
X = df_features
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))

joblib.dump(model, "phishing_model.pkl")
print("💾 Model saved as phishing_model.pkl")
