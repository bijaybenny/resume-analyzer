from ml.extractor import extract_text_from_pdf, clean_text
from ml.nlp_processor import process_text
from ml.skill_extractor import extract_skills
from ml.similarity import compute_similarity
from ml.scorer import calculate_skill_match, final_score
from ml.recommender import generate_suggestions

# Input
pdf_path = "sample_resume.pdf"
job_desc = "Looking for a candidate with Python, SQL, NLP skills"

# Resume processing
resume_text = extract_text_from_pdf(pdf_path)
cleaned_resume = clean_text(resume_text)
resume_tokens = process_text(cleaned_resume)
resume_skills = extract_skills(cleaned_resume, resume_tokens)

# Job processing
cleaned_job = clean_text(job_desc)
job_tokens = process_text(cleaned_job)
job_skills = extract_skills(cleaned_job, job_tokens)

# Similarity
sim_score = compute_similarity(cleaned_resume, cleaned_job)

# Skill match
skill_score, matched = calculate_skill_match(resume_skills, job_skills)
missing = list(set(job_skills) - set(resume_skills))

# Final score
final = final_score(sim_score, skill_score)

# Suggestions
suggestions = generate_suggestions(missing)

# Output
print("Similarity Score:", sim_score)
print("Skill Match Score:", skill_score)
print("Final Score:", final)

print("\nMatched Skills:", matched)
print("Missing Skills:", missing)

print("\nSuggestions:")
for s in suggestions:
    print("-", s)