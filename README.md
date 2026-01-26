# Agentic RAG System with Autonomous Reasoning and Self-Reflection

## Overview
This project extends a traditional Retrieval-Augmented Generation (RAG) chatbot
by adding an **agentic control layer** capable of autonomous reasoning, tool-calling,
self-reflection, and answer quality evaluation.

The system is **data-agnostic** — any data placed inside the `data/` directory
(PDFs, transcripts, text files) can be used without changing agent logic.

---

## Problem Statement
Standard RAG chatbots blindly retrieve documents for every query and may:
- return shallow or irrelevant answers
- hallucinate when data is missing
- lack transparency on answer quality

This project addresses these limitations by introducing an **AI agent layer**
that controls how and when retrieval happens, evaluates its own responses,
and transparently reports answer quality.

---

## System Architecture (High Level)
The system follows a modular agentic design:

User Query  
→ Agent Planner (decides action)  
→ Tool Executor (calls RAG if needed)  
→ Self-Reflection (retry if answer is weak)  
→ Evaluation (scores answer quality)  
→ Final Response  

---

## Key Features
- **RAG as a Tool**: Retrieval is abstracted and invoked only when required
- **Autonomous Planning**: Agent decides how to handle each query
- **Self-Reflection Loop**: Weak or ungrounded answers trigger retries
- **Evaluation Metrics**: Measures clarity, grounding, and answer completeness
- **No Hallucination**: If data does not support an answer, the agent declines safely
- **Framework-Agnostic**: Implemented without heavy agent frameworks for clarity

---

## Project Structure
agentic-rag/
│
├── agent/ # Planner, executor, reflector, agent loop
├── tools/ # RAG tool abstraction
├── evaluation/ # Answer evaluation metrics
├── data/ # User-provided data (PDFs, text, etc.)
├── config/ # Configurations
├── main.py # Entry point
└── README.md


---

## How to Run

### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Your Data

Place documents inside:
```bash
3. data/
```

### 4. Run the Agent
```bash
python main.py
```

### Evaluation Metrics

Each response is evaluated using simple, transparent metrics:

Length Score – response completeness

Clarity Score – confidence and certainty

Grounding Score – support from retrieved data

These metrics are used for inspection, not forced optimization.


## Why This Is Agentic (Not Just RAG)

Unlike standard RAG systems, this project:

reasons before retrieval

treats RAG as a callable tool

evaluates its own outputs

retries automatically when answers are weak

This design reflects how modern production AI agents are built.

## Future Improvements

LangGraph wrapper (optional)

Logging and monitoring

UI or API interface

Advanced evaluation metrics



### Author

Built as part of the AI Academy Capstone Project to demonstrate
end-to-end agentic AI system design.

Abdul Rahaman S | AI/ML Engineer