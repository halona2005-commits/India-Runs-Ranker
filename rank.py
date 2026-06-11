import json
import pandas as pd

from src.features import extract_features
from src.scorer import compute_score
from src.nlp import compute_similarity
from src.utils import combine_text

# Load candidates
with open("data/candidates.jsonl", "r") as f:
    candidates = [json.loads(line) for line in f]

# Load job description
with open("data/job_description.docx", "rb") as f:
    job_text = f.read().decode(errors="ignore")  # simple hack

job_skills = ["python", "machine learning", "deep learning", "nlp"]

# Prepare candidate texts for NLP
candidate_texts = [combine_text(c) for c in candidates]

# Compute similarity scores
similarities = compute_similarity(job_text, candidate_texts)

results = []

for i, candidate in enumerate(candidates):
    features = extract_features(candidate, job_skills)
    nlp_score = similarities[i]

    final_score = compute_score(features, nlp_score)

    results.append({
        "candidate_id": candidate.get("id"),
        "score": final_score
    })

# Sort and take top 100
top_candidates = sorted(results, key=lambda x: x["score"], reverse=True)[:100]

# Save CSV
df = pd.DataFrame(top_candidates)
df.to_csv("outputs/submission.csv", index=False)

print("✅ Top 100 candidates saved!")