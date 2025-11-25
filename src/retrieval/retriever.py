from sentence_transformers import SentenceTransformer
import numpy as np
class Retriever:
    def __init__(self, model_name='all-MiniLM-L6-v2', index=None):
        self.embedder = SentenceTransformer(model_name)
        self.index = index
    def embed_query(self, q):
        return self.embedder.encode([q], convert_to_numpy=True)
    def retrieve(self, q, top_k=5):
        vec = self.embed_query(q)
        idxs, ids = self.index.search(vec, top_k)
        return ids
