def compute_score(features, nlp_score):
    return (
        0.4 * features["skills_score"] +
        0.3 * features["experience_score"] +
        0.1 * features["education_score"] +
        0.2 * nlp_score
    )