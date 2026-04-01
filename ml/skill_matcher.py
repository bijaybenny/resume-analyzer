def match_skills(resume_skills, jd_skills):
    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    matched = resume_set & jd_set
    missing = jd_set - resume_set
    additional = resume_set - jd_set

    return {
        "matched": matched,
        "missing": missing,
        "additional": additional
    }