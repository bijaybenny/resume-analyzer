from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Load model once (global)
# -------------------------------
model = SentenceTransformer('all-MiniLM-L6-v2')


# -------------------------------
# Compute similarity
# -------------------------------
def compute_similarity(text1, text2):
    # Safety check
    if not text1.strip() or not text2.strip():
        return 0.0

    emb1 = model.encode(text1)
    emb2 = model.encode(text2)

    score = cosine_similarity([emb1], [emb2])[0][0]

    return float(score)