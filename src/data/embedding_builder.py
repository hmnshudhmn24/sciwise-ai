from sentence_transformers import SentenceTransformer
import numpy as np, os, json

class EmbeddingBuilder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
    def encode(self, texts):
        return self.model.encode(texts, show_progress_bar=False, convert_to_numpy=True)
    def save(self, embeddings, meta, out_path):
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        np.save(out_path, embeddings)
        with open(out_path+'.meta.json','w') as fh:
            json.dump(meta, fh)
