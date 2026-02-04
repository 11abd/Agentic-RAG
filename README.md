# 🎓 Agentic AI Knowledge Assistant

This project extends a previously built local RAG chatbot into a full AI-Agentic system capable of autonomous reasoning, tool-based action, self-reflection, and transparent evaluation.

The system is designed to demonstrate real-world agentic AI foundations, not just retrieval or prompting. It focuses on correctness, inspectability, and modular design rather than latency or cloud scale.


## 🎯 Capstone Objective

 > Build upon my previous RAG chatbot (https://github.com/11abd/rag-chatbot-genai) to develop an AI-Agentic system capable of performing autonomous reasoning, taking meaningful tool-based actions, and reflecting on its own decisions and performance.

This project satisfies that objective by:

- Reusing the existing RAG pipeline as a tool
- Introducing an agent planner
- Adding self-reflection and retry logic
- Exposing the system via an API-first interface
- Logging and evaluating each response with transparent metrics

## 🛠️ Technology Stack
| Layer               | Technology                                 |
| ------------------- | ------------------------------------------ |
| Language            | Python 3.10                                |
| Agent Orchestration | Custom agent loop (planner + tools)        |
| PDF Parsing         | PyMuPDF                                    |
| Audio Transcription | OpenAI Whisper (local, CPU-only)           |
| Embeddings          | sentence-transformers (`all-MiniLM-L6-v2`) |
| Vector DB           | ChromaDB (local, persistent)               |
| Retrieval           | Hybrid (Vector + Keyword/BM25)             |
| LLM                 | Ollama (local models)                      |
| API                 | FastAPI                                    |                     |



## 🧱 System Architecture (High Level)

```
User Query
   ↓
Agent Planner
(decides next action)
   ↓
Tool Executor
(RAG / Pipeline / Retrieval)
   ↓
Self-Reflection
(answer quality check, retry if weak)
   ↓
Evaluation
(scoring & logging)
   ↓
Final Response
```

## 🔧 Tooling & Agent Capabilities

**🔹 Tools Available to the Agent**

 - RAG Query Tool – retrieve grounded answers from local knowledge base

**🔹 Agent Behaviors**

- Determines whether retrieval is required
- Evaluates response quality
- Retries retrieval if confidence or grounding is low
- Produces a final, grounded response

## 📊 Self-Reflection & Evaluation

Each response is evaluated using simple, transparent metrics:

| Metric              | Purpose                                |
| ------------------- | -------------------------------------- |
| **Length Score**    | Checks response completeness           |
| **Clarity Score**   | Measures confidence and certainty      |
| **Grounding Score** | Measures support from retrieved chunks |

📌 These metrics are:

Logged for inspection

Used to guide retries

Not used for forced optimization or fine-tuning

This keeps the system explainable and debuggable.

## 📁 Project Structure

```
Agentic-RAG/
├── api/                    # FastAPI application
│   └── app.py
├── ingestion/              # PDF & audio ingestion
├── processing/             # Cleaning & chunking
├── embeddings/             # Embedding + ChromaDB
├── retrieval/              # Hybrid retrieval logic
├── generation/             # Prompting & LLM calls
├── agent/                  # Agent planner, tools, reflection, evaluation
├── utils/                  # Logging & helpers
├── data/                   # PDFs, audio, transcripts, chunks
├── vector_db/              # Persistent ChromaDB store
├── rag_pipeline.py             # End-to-end RAG pipeline
├── main.py                 # Optional CLI agent
├── requirements.txt
└── README.md
```

## ⚙️ Environment Setup
1️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```
2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
3️⃣ Install Ollama (Required)
- 👉 https://ollama.com/download

Verify:
```
ollama --version
```
Pull a model:
```
ollama pull mistral
```

## 📥 How to Add New Data

1️⃣ Add PDFs

Place all PDF files into:
```
data/pdfs/
```
2️⃣ Add Videos

Place videos (.mp4) into:
```
data/audio/
```
🔄 Run the RAG Pipeline

The pipeline performs extraction → cleaning → chunking → embedding → vector store rebuild.
```
python rag_pipeline.py
```

### What this does:

1. Extracts text from PDFs
2. Converts videos to audio and transcribes them
3. Cleans and merges all text
4. Deletes old chunks
5. Creates new chunks
6. Rebuilds ChromaDB embeddings from scratch

✅ Safe to run multiple times
✅ No duplication
✅ Deterministic behavior


## 💬 Running the Agent
**🔹 API**
```
uvicorn api.app:app --reload
```

Interactive API docs:
```
http://localhost:8000/docs
```
Example request :
```
{
  "question": "Tell me about hybrid retrieval?"
}
```

or it can be run via  CLI
```
python main.py
```

## 🧠 How Grounded Answering Is Enforced

- Retrieval happens before generation
- Retrieved chunks are injected into the prompt
- LLM is instructed to answer only from context
- If grounding is weak → agent retries or responds with “I don’t know”

This reduces hallucination and improves trust.

## 🧪 Design Decisions

- Agent logic separated from retrieval
- Manual pipeline execution (no background jobs)
- Local-only execution
- Emphasis on inspectability over speed
- These choices make the system easier to evaluate and reason about.

## Limitations

- CPU-only
- No UI
- Not real-time
- No cloud scaling

All limitations are intentional for learning and evaluation clarity.

## 👨‍💻 Author

> Abdul Rahaman S   |   
AI / ML Engineer