import gradio as gr
from src.model.inference import SciLLM
from src.retrieval.vector_store import SimpleIndex
from src.retrieval.retriever import Retriever
from src.retrieval.rag_pipeline import RAGPipeline

def summarize(text):
    llm = SciLLM()
    return llm.generate('Summarize: ' + text)

def ask(text, question):
    index = SimpleIndex()
    retriever = Retriever(index=index)
    llm = SciLLM()
    rag = RAGPipeline(retriever, llm)
    return rag.answer(question)

with gr.Blocks() as demo:
    gr.Markdown('# SciWise-AI — Lightweight Demo')
    with gr.Tab('Summarize'):
        txt = gr.Textbox(lines=12, label='Paper text')
        out = gr.Textbox(lines=6, label='Summary')
        btn = gr.Button('Summarize')
        btn.click(fn=summarize, inputs=txt, outputs=out)
    with gr.Tab('Ask'):
        paper = gr.Textbox(lines=12, label='Paper text (optional)')
        q = gr.Textbox(lines=2, label='Question')
        a = gr.Textbox(lines=6, label='Answer')
        ask_btn = gr.Button('Ask')
        ask_btn.click(fn=ask, inputs=[paper,q], outputs=a)

if __name__ == '__main__':
    demo.launch()
