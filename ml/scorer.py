def compute_skill_score(matched, jd_skills):
    if len(jd_skills) == 0:
        return 0.0

    return len(matched) / len(jd_skills)


def compute_final_score(similarity_score, skill_score):
    # Weighting
    final = (0.7 * similarity_score) + (0.3 * skill_score)
    return round(final, 4)