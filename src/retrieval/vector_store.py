import numpy as np

class SimpleIndex:
    def __init__(self):
        self.vectors = []
        self.ids = []
    def add(self, vecs, ids):
        self.vectors.extend(list(vecs))
        self.ids.extend(list(ids))
    def search(self, qvec, top_k=5):
        # naive L2 search
        if not self.vectors:
            return [], []
        arr = np.stack(self.vectors)
        q = qvec[0]
        dists = ((arr - q)**2).sum(axis=1)
        idx = dists.argsort()[:top_k]
        return idx.tolist(), [self.ids[i] for i in idx]
