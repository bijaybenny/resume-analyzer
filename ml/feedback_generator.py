def format_skill(skill):
    """Handle proper capitalization"""
    special_cases = {
        "sql": "SQL",
        "html": "HTML",
        "css": "CSS",
        "javascript": "JavaScript"
    }
    return special_cases.get(skill.lower(), skill.title())


def format_skills(skill_set):
    return ", ".join([format_skill(s) for s in list(skill_set)[:5]])


def generate_feedback(final_score, matched, missing, additional):

    # -------------------------------
    # Format skills
    # -------------------------------
    matched_str = format_skills(matched) if matched else None
    missing_str = format_skills(missing) if missing else None
    additional_str = format_skills(additional) if additional else None

    # -------------------------------
    # Special Case: NO MATCH
    # -------------------------------
    if not matched:
        paragraph = "The candidate shows limited alignment with the job requirements. "

        if missing_str:
            paragraph += f"Key required skills such as {missing_str} are not sufficiently reflected in the profile. "

        if additional_str:
            paragraph += f"However, the candidate does demonstrate strengths in areas like {additional_str}, which may be valuable in broader contexts."

        return paragraph.strip()

    # -------------------------------
    # Normal Case
    # -------------------------------
    if final_score >= 0.75:
        intro = "The candidate demonstrates a strong alignment with the job requirements."
    elif final_score >= 0.5:
        intro = "The candidate shows a moderate alignment with the job requirements."
    else:
        intro = "The candidate shows limited alignment with the job requirements."

    paragraph = intro + " "

    if matched_str:
        paragraph += f"The profile highlights key competencies such as {matched_str}, indicating relevant technical strength. "

    if missing_str:
        paragraph += f"However, certain areas such as {missing_str} are not strongly reflected and could be improved. "

    if additional_str:
        paragraph += f"Additionally, the presence of skills like {additional_str} adds further depth and versatility to the profile."

    return paragraph.strip()