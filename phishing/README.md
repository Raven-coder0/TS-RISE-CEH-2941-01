# Hybrid Phishing Detection System

A Python-based desktop application that uses **rule-based heuristics** and a **machine learning model** to detect phishing URLs. This hybrid approach improves accuracy by combining pattern recognition with predictive learning.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Overview

The Hybrid Phishing Detection System is a real-time phishing URL analyzer that classifies websites as:
- **Legitimate**
- **Suspicious**
- **Phishing**

The detection logic is based on a combination of:
1. **Heuristic Rules** (e.g., IP-based domains, abnormal URL structure)  
2. **Machine Learning Model** (trained with features derived from phishing datasets)

---

## Features

- Rule-based phishing detection  
- Machine learning-based URL classification  
- Interactive Tkinter GUI  
- Colored classification results  
- Input validation and error handling  
- Offline prediction (no internet required)  

---

## Technologies Used

| Technology       | Purpose                    |
|------------------|----------------------------|
| Python           | Core programming           |
| Tkinter          | GUI interface              |
| `re`             | URL pattern matching       |
| `urlparse`       | URL parsing                |
| `joblib`         | Loading trained ML model   |
| `scikit-learn`   | Model training (external)  |

---

## System Architecture

```
User Input → Rule-Based Checks → Feature Extraction → ML Prediction → Result Display
```

The system combines both methods and outputs:

- **Phishing** → If both rule-based and ML classify negatively  
- **Suspicious** → If either method flags it  
- **Legitimate** → If both mark it as safe  

---

## How It Works

### Rule-Based Heuristics

Flags the URL as **suspicious** if 3 or more of the following conditions are met:
- Use of IP address instead of domain  
- Length > 75 characters  
- Presence of `@` symbol  
- Hyphens in domain  
- No HTTPS  
- Excessive subdomains  
- Double slashes `//` mid-URL  

### Machine Learning Features

The model is trained on:
- URL length  
- Presence of IP address  
- Use of `@` symbol  
- Hyphen in domain  
- HTTPS usage  
- Number of dots in domain  

Model is saved as `phishing/phishing_model.pkl`.

---

## Usage

### Prerequisites

- Python 3.x  
- `joblib`  
- `scikit-learn` (for training only)  

### Installation

```bash
git clone https://github.com/yourusername/hybrid-phishing-detector.git
cd hybrid-phishing-detector
```

### Running the App

Ensure the trained model file is located at:
```
phishing/phishing_model.pkl
```

To launch the app:

```bash
python app.py
```

If the model doesn't exist, you'll be prompted to train it using `train_model.py`.

---



## Future Enhancements

- Integration with phishing databases (e.g., PhishTank API)  
- URL shortener support with expansion  
- Real-time browser extension integration  
- Exportable detection history or reports  
- Display model confidence score  

---

## License

This project is intended for **educational and ethical use only**. Unauthorized scanning of third-party websites without consent is strictly discouraged.
