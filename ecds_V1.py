from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

ecds_df = pd.read_csv("ecds_df.csv")

model = SentenceTransformer('all-MiniLM-L6-v2')

output_embeddings = []
for i, row in ecds_df.iterrows():
    keywords = [kw.strip() for kw in row["ECDS_SearchTerms"].split(",")]
    keyword_embeddings = model.encode(keywords)
    avg_embedding = keyword_embeddings.mean(axis=0)
    output_embeddings.append(avg_embedding)

ecds_df["embedding"] = output_embeddings


def best_match(user_input):
    input_embedding = model.encode([user_input])
    sims = cosine_similarity(input_embedding, list(ecds_df["embedding"]))[0]
    best_idx = sims.argmax()
    result = ecds_df.iloc[best_idx]["SNOMED_UK_Preferred_Term"], sims[best_idx]
    return result[0], float(result[1])


def top_matches(user_input, n=5):
    input_embedding = model.encode([user_input])
    sims = cosine_similarity(input_embedding, list(ecds_df["embedding"]))[0]
    top_indices = sims.argsort()[::-1][:n]
    results = [(ecds_df.iloc[i]["SNOMED_UK_Preferred_Term"], sims[i]) for i in top_indices]
    return results
