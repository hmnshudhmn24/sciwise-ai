from fastapi import FastAPI
from pydantic import BaseModel
from src.model.inference import SciLLM
from src.retrieval.vector_store import SimpleIndex
from src.retrieval.retriever import Retriever
from src.retrieval.rag_pipeline import RAGPipeline

app = FastAPI(title='SciWise-AI (Lightweight)')

class Query(BaseModel):
    query: str

# lightweight init
index = SimpleIndex()
retriever = Retriever(index=index)
llm = SciLLM()
rag = RAGPipeline(retriever, llm)

@app.post('/query')
async def query(q: Query):
    answer = rag.answer(q.query)
    return {'answer': answer}

@app.get('/')
def root():
    return {'message': 'SciWise-AI lightweight API'}
