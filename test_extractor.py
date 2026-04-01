from ml.extractor import extract_text_from_pdf, clean_text

pdf_path = "sample_resume.pdf"  # put a resume file in root

raw_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(raw_text)

print("\nRAW TEXT:\n", raw_text[:500])
print("\nCLEANED TEXT:\n", cleaned_text[:500])