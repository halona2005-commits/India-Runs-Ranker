def clean_text(text):
    return text.lower().strip()

def combine_text(candidate):
    skills = candidate.get("skills", [])

    # Extract skill names safely
    skill_names = []
    for s in skills:
        if isinstance(s, dict):
            skill_names.append(s.get("name", ""))
        else:
            skill_names.append(str(s))

    return " ".join(skill_names)