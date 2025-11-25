from src.retrieval.vector_store import SimpleIndex
import numpy as np

def test_index_add_search():
    idx = SimpleIndex()
    vecs = [np.random.rand(3).astype('float32') for _ in range(5)]
    ids = list(range(5))
    idx.add(vecs, ids)
    q = [vecs[0]]
    idxs, ids_out = idx.search(q, top_k=3)
    assert len(idxs) <= 3
