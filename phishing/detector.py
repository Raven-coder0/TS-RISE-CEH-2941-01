import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlparse
import re
import joblib
import os


def rule_based_check(url):
    suspicious = 0

    if re.match(r"https?://\d{1,3}(\.\d{1,3}){3}", url): suspicious += 1
    if len(url) > 75: suspicious += 1
    if "@" in url: suspicious += 1
    if "-" in urlparse(url).netloc: suspicious += 1
    if not url.startswith("https://"): suspicious += 1
    if url.count('.') > 4: suspicious += 1
    if "//" in url[8:]: suspicious += 1

    return True if suspicious >= 3 else False 
def extract_ml_features(url):
    return [[
        len(url),
        1 if re.match(r"https?://\d{1,3}(\.\d{1,3}){3}", url) else 0,
        1 if "@" in url else 0,
        1 if "-" in urlparse(url).netloc else 0,
        1 if url.startswith("https://") else 0,
        urlparse(url).netloc.count('.')
    ]]

if not os.path.exists("phishing/phishing_model.pkl"):
    messagebox.showerror("Model Not Found", "Please train the model first using train_model.py.")
    exit()
model = joblib.load("phishing/phishing_model.pkl")

def detect_url():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter an URL.")
        return

    rule_result = rule_based_check(url)
    ml_prediction = model.predict(extract_ml_features(url))[0]

    if rule_result and ml_prediction == 1:
        result = "🛑 Definitely a Phishing Website!"
        color = "#ff4444"
    elif rule_result or ml_prediction == 1:
        result = "⚠️ Possibly Suspicious Website!"
        color = "#ffaa00"
    else:
        result = "✅ Legitimate Website."
        color = "#00ffcc"

    result_label.config(text=result, fg=color)

root = tk.Tk()
root.title("Hybrid Phishing Detector")
root.geometry("650x350")
root.configure(bg="black")

tk.Label(root, text="🔐 HYBRID PHISHING DETECTION SYSTEM", fg="#00ffff", bg="black",
         font=("Consolas", 16, "bold")).pack(pady=20)

url_entry = tk.Entry(root, font=("Consolas", 12), width=55,
                     bg="#1a1a1a", fg="#00ffff", insertbackground="#00ffff")
url_entry.pack(pady=10)

tk.Button(root, text="Analyze URL", command=detect_url,
          bg="#001f33", fg="#00ffff", font=("Consolas", 12),
          activebackground="#003344", width=20).pack(pady=10)

result_label = tk.Label(root, text="", font=("Consolas", 14, "bold"),
                        bg="black", fg="#00ffff")
result_label.pack(pady=20)

root.mainloop()
