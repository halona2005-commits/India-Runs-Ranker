from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(job_text, candidate_texts):
    corpus = [job_text] + candidate_texts

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)

    job_vec = tfidf_matrix[0]
    cand_vecs = tfidf_matrix[1:]

    return cosine_similarity(job_vec, cand_vecs)[0]