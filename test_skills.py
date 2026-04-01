from ml.extractor import extract_text_from_pdf, clean_text
from ml.nlp_processor import process_text
from ml.skill_extractor import extract_skills

pdf_path = "sample_resume.pdf"

text = extract_text_from_pdf(pdf_path)
cleaned = clean_text(text)
tokens = process_text(cleaned)

skills = extract_skills(cleaned, tokens)

print("Extracted Skills:", skills)