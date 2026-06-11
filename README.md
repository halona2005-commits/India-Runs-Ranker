# 🤖 AI Candidate Ranking System

### India.Runs Data & AI Challenge (Redrob x Hack2Skill)

---

## 🚀 Overview

This project is an **AI-powered candidate ranking system** designed to identify the **Top 100 candidates** for a **Senior AI Engineer role**.

It uses a **hybrid approach** combining:

* Rule-based scoring
* NLP-based semantic similarity (TF-IDF + Cosine Similarity)
* Multi-factor feature engineering

---

## 🧠 Key Features

* ✅ Skills-based matching
* ✅ Experience & career trajectory scoring
* ✅ Education relevance scoring
* ✅ Behavioral signal integration
* ✅ NLP-based semantic similarity
* ✅ Weighted composite ranking
* ✅ Explainable scoring output

---

## 🏗️ Project Structure

```
india-runs-ranker/
├── src/
│   ├── features.py      # Feature engineering
│   ├── nlp.py           # TF-IDF & cosine similarity
│   ├── scorer.py        # Final scoring logic
│   └── utils.py         # Helper functions
├── models/              # Saved models (future use)
├── notebooks/           # Exploration (optional)
├── data/                # Input datasets (not included in repo)
├── outputs/             # Generated results
├── rank.py              # Main pipeline script
├── validate_submission.py
├── submission_metadata.yaml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python rank.py --candidates data/candidates.jsonl --out outputs/submission.csv
```

---

## ✅ Validate Submission

```bash
python validate_submission.py outputs/submission.csv
```

---

## 🧩 Methodology

### 1. Feature Engineering

* Skills match score
* Experience normalization
* Education relevance

### 2. NLP Similarity

* TF-IDF vectorization
* Cosine similarity between candidate profiles and job description

### 3. Final Scoring

Final score is computed as a weighted combination of:

```
Final Score =
    0.4 * Skills Score +
    0.3 * Experience Score +
    0.1 * Education Score +
    0.2 * NLP Similarity
```

---

## 📊 Output

* Generates a **Top 100 ranked candidate list**
* Saved as:

```
outputs/submission.csv
```

---

## 🔍 Explainability

Each candidate score is derived from:

* Skills relevance
* Experience strength
* Semantic similarity with job description

This ensures **transparent and interpretable ranking**.

---

## 💻 Technologies Used

* Python
* Pandas
* Scikit-learn
* NLP (TF-IDF, Cosine Similarity)

---

## 🚀 Future Improvements

* BERT-based semantic embeddings
* Learning-to-rank models (XGBoost / LightGBM)
* Dynamic weight optimization
* Streamlit dashboard for visualization

---

## 📌 Notes

* Large datasets are excluded via `.gitignore`
* The system is designed to be modular and scalable

---

## 🏆 Summary

This project demonstrates a **modular, explainable, and AI-driven candidate ranking system** that combines structured scoring with semantic intelligence to improve hiring decisions.

---
