def extract_features(candidate, job_skills):
    skills_raw = candidate.get("skills", [])

    skills = []
    for s in skills_raw:
        if isinstance(s, dict):
            skills.append(s.get("name", "").lower())
        else:
            skills.append(str(s).lower())

    matched = len(set(skills) & set(job_skills))
    skills_score = matched / (len(job_skills) + 1)

    experience_years = candidate.get("experience_years", 0)
    experience_score = min(experience_years / 10, 1)

    education = str(candidate.get("education", "")).lower()
    education_score = 1 if "computer" in education or "ai" in education else 0.5

    return {
        "skills_score": skills_score,
        "experience_score": experience_score,
        "education_score": education_score
    }