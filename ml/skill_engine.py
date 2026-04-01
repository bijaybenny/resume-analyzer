import json

# Load skill database
with open("ml/skills_db.json", "r") as f:
    SKILL_DB = json.load(f)


def normalize_text(text):
    return text.lower()


def extract_skills_advanced(text):
    text = normalize_text(text)

    direct = set()
    inferred = set()

    for skill, data in SKILL_DB.items():
        # Direct match
        if skill in text:
            direct.add(skill)

        # Alias match
        for alias in data["aliases"]:
            if alias in text:
                direct.add(skill)

        # Tool-based inference
        for tool in data["tools"]:
            if tool in text:
                inferred.add(skill)

    # ❗ Remove overlap
    inferred = inferred - direct

    return {
        "direct": list(direct),
        "inferred": list(inferred)
    }