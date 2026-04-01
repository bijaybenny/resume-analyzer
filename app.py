from flask import Flask, render_template, request
from ml.extractor import extract_text_from_pdf
from ml.skill_extractor import extract_skills
from ml.skill_matcher import match_skills
from ml.similarity import compute_similarity
from ml.scorer import compute_skill_score, compute_final_score
from ml.feedback_generator import generate_feedback
from ml.recommender import generate_recommendations

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    jd_text = request.form['job_description']

    # Extract text from PDF
    resume_text = extract_text_from_pdf(file)

    # Skill extraction
    resume_output = extract_skills(resume_text)
    jd_output = extract_skills(jd_text)

    resume_skills = resume_output["dictionary_skills"]
    jd_skills = jd_output["dictionary_skills"]

    # Matching
    match_result = match_skills(resume_skills, jd_skills)

    # ML similarity
    similarity_score = compute_similarity(resume_text, jd_text)

    # Scoring
    skill_score = compute_skill_score(match_result["matched"], jd_skills)
    final_score = compute_final_score(similarity_score, skill_score)

    # Feedback + recommendations
    feedback = generate_feedback(
        final_score,
        match_result["matched"],
        match_result["missing"],
        match_result["additional"]
    )

    recommendations = generate_recommendations(match_result["missing"])

    return render_template(
        'result.html',
        score=round(final_score * 100, 2),
        feedback=feedback,
        recommendations=recommendations,
        matched=match_result["matched"],
        missing=match_result["missing"],
        additional=match_result["additional"]
    )


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)