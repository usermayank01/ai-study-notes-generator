# 🎓 AI Study Notes Generator

An AI-powered study assistant that reads uploaded study materials and generates summaries, revision notes, quizzes, key points, and answers student questions.

## 🚀 Features

- 📄 Upload study documents
- 🤖 AI-generated summaries
- 📚 Revision notes
- ❓ Automatic multiple-choice quizzes
- 📌 Key points extraction
- 💬 Ask questions about uploaded material
- 🔎 Retrieval-Augmented Generation (RAG)
- 🧠 Local HuggingFace embeddings
- ⚡ Local Llama 3.2 model using Ollama
- 💰 No paid AI API required

## 🛠️ Tech Stack

- Python
- FastAPI
- LangChain
- FAISS
- HuggingFace Sentence Transformers
- Ollama
- Llama 3.2
- HTML
- CSS
- JavaScript

## 🧠 How It Works

```text
Upload Documents
       ↓
Document Processing
       ↓
Text Chunking
       ↓
HuggingFace Embeddings
       ↓
FAISS Vector Database
       ↓
User Question / Study Tool
       ↓
Semantic Search
       ↓
Relevant Document Context
       ↓
Llama 3.2
       ↓
Generated Study Content