import random

def generate_recommendations(missing_skills):

    if not missing_skills:
        return "The profile already aligns well with the job requirements."

    templates = [
        "Strengthening {skill} through practical projects would improve profile alignment.",
        "Building hands-on experience in {skill} can enhance your suitability for this role.",
        "Improving proficiency in {skill} will help better match job expectations.",
        "Consider gaining deeper knowledge in {skill} to strengthen your profile.",
        "Developing real-world exposure in {skill} would be beneficial."
    ]

    recommendations = []

    for skill in sorted(list(missing_skills))[:5]:
        template = random.choice(templates)
        recommendations.append(template.format(skill=skill.title()))

    return " ".join(recommendations)