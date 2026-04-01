from ml.skill_engine import extract_skills_advanced
from ml.skill_matcher import compare_skills
from ml.scoring_engine import compute_score

resume_text = "Worked with PyTorch and TensorFlow for deep learning"
job_text = "Looking for machine learning and deep learning experience"

resume_skills = extract_skills_advanced(resume_text)
job_skills = extract_skills_advanced(job_text)

match_result = compare_skills(resume_skills, job_skills)

score, explanation = compute_score(match_result)

print("Score:", score)
print("Explanation:", explanation)