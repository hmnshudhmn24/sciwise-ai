class RAGPipeline:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm
    def answer(self, query, top_k=5):
        ids = self.retriever.retrieve(query, top_k)
        context = ' '.join([f'[doc {i}]' for i in (ids or [])])
        prompt = f'Context: {context}\nQuestion: {query}\nAnswer:'
        return self.llm.generate(prompt)
