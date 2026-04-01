from ml.skill_extractor import extract_skills
from ml.skill_matcher import match_skills
from ml.similarity import compute_similarity
from ml.scorer import compute_skill_score, compute_final_score
from ml.feedback_generator import generate_feedback
from ml.recommender import generate_recommendations

# -------------------------------
# Sample Resume Text
# -------------------------------
resume_text = """
Experienced in Python, data analysis, and Excel.
Worked on machine learning models using pandas and numpy.
Strong communication and teamwork skills.
"""

# -------------------------------
# Sample Job Description
# -------------------------------
jd_text = """
Looking for candidates with Python, SQL, and machine learning experience.
Strong data analysis and problem solving skills required.
"""

# -------------------------------
# Extract Skills
# -------------------------------
resume_output = extract_skills(resume_text)
jd_output = extract_skills(jd_text)

resume_skills = resume_output["dictionary_skills"]
jd_skills = jd_output["dictionary_skills"]

# -------------------------------
# Match Skills
# -------------------------------
match_result = match_skills(resume_skills, jd_skills)

# -------------------------------
# ML Similarity
# -------------------------------
similarity_score = compute_similarity(resume_text, jd_text)

# -------------------------------
# Skill Score
# -------------------------------
skill_score = compute_skill_score(match_result["matched"], jd_skills)

# -------------------------------
# Final Score
# -------------------------------
final_score = compute_final_score(similarity_score, skill_score)

# -------------------------------
# Generate Feedback
# -------------------------------
feedback = generate_feedback(
    final_score,
    match_result["matched"],
    match_result["missing"],
    match_result["additional"]
)

# -------------------------------
# Print Results
# -------------------------------
print("\n========== FINAL RESULT ==========")

print(f"\nFinal Score: {final_score:.4f}")

print("\nFeedback:")
print(feedback)



# -------------------------------
# Generate Recommendations
# -------------------------------
recommendations = generate_recommendations(match_result["missing"])

print("\nRecommendations:")
print(recommendations)