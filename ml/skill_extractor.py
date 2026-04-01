import json
import re
import os

# -------------------------------
# Load Skills Database
# -------------------------------
BASE_DIR = os.path.dirname(__file__)
SKILL_DB_PATH = os.path.join(BASE_DIR, "skills_db.json")

with open(SKILL_DB_PATH, "r") as f:
    SKILLS_DB = json.load(f)


# -------------------------------
# Clean Text
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# -------------------------------
# Dictionary Skill Extraction
# -------------------------------
def extract_from_dictionary(text):
    text = clean_text(text)
    found = set()

    for skill, synonyms in SKILLS_DB.items():
        terms = [skill] + synonyms

        for term in terms:
            pattern = r'\b' + re.escape(term.lower()) + r'\b'
            if re.search(pattern, text):
                found.add(skill)

    return found





# -------------------------------
# Final Skill Extraction Function
# -------------------------------
def extract_skills(text):
    text = clean_text(text)

    dict_skills = extract_from_dictionary(text)

    # Build meaningful phrases ONLY from detected skills
    phrase_skills = set()

    for skill in dict_skills:
        words = skill.split()

        if len(words) >= 2:
            phrase_skills.add(skill)

    return {
        "dictionary_skills": dict_skills,
        "phrases": phrase_skills,
        "combined": dict_skills.union(phrase_skills)
    }