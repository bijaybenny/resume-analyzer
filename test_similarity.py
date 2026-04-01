from ml.similarity import compute_similarity

resume_text = "I have experience in Python and Machine Learning"
job_desc = "Looking for a candidate skilled in ML and Python"

score = compute_similarity(resume_text, job_desc)

print("Similarity Score:", score)