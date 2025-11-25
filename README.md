# 🧪 SciWise-AI  
### **Lightweight Developer Template for Domain-Adaptive Scientific RAG Systems**

SciWise-AI is a **minimal, developer-friendly scaffold** for building a **Retrieval-Augmented Generation (RAG)** system specialized for **scientific literature**.  
It provides a clean starting point with placeholders for real models, datasets, and pipelines—without the heavy complexity of a full production system.

You can plug in **your own embeddings**, **LLM**, **retriever**, and **scientific corpus** while keeping the project structure simple and extensible.



## 🚀 Features

- **Domain-adaptive RAG scaffold** tailored for scientific texts  
- Lightweight module structure for:
  - Data ingestion
  - Chunking & preprocessing
  - Embedding generation (placeholder)
  - Vector retrieval (FAISS placeholder)
  - Response synthesis (LLM wrapper)
- **FastAPI backend** with minimal RAG pipeline endpoint  
- **Gradio demo UI** for interactive querying  
- Fully editable template — replace placeholder logic with production components  
- Clean folder layout for rapid prototyping and expansion



## 🗂 Directory Structure

```
sciwise-ai/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── data_loader.py
│   ├── embedder.py
│   ├── retriever.py
│   ├── rag_pipeline.py
│   │
│   ├── app/
│   │   ├── api.py
│   │   └── gradio_ui.py
│   │
│   └── utils/
│       └── text_processing.py
│
└── data/
```



## ⚡ Quickstart

### 1. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Gradio Demo

```bash
python src/app/gradio_ui.py
```

### 3. Run the FastAPI Server

```bash
uvicorn src.app.api:app --reload
```



## 🔧 How to Customize

### Replace the embedding model  
Edit `src/embedder.py` and plug in your own model.

### Swap in your vector store  
`src/retriever.py` uses FAISS — replace with any store.

### Extend the RAG logic  
Modify `src/rag_pipeline.py`.

### Add a real scientific dataset  
Place your PDFs into `data/`.


## 🧱 Architecture Overview

Scientific Docs → Loader → Chunker → Embedder → Vector DB → Retriever → LLM → Response

