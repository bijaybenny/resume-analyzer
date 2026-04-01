import spacy
from sentence_transformers import SentenceTransformer

# Load spaCy
nlp = spacy.load("en_core_web_sm")
doc = nlp("I love machine learning")

print("spaCy working:", [token.lemma_ for token in doc])

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')
emb = model.encode("Test sentence")

print("Embedding length:", len(emb))