# Live Regulatory Intelligence Agent (Track 1 – Synaptix Frontier)

## What this project does
This is a **live agentic AI system** that continuously ingests regulatory documents
and updates its answers instantly when documents are added or modified.

This demonstrates **Pathway's live indexing** (not static RAG).

---

## Folder Structure
live_regulatory_agent/
├── data/regulations/     # LIVE DATA SOURCE (edit files here)
├── pathway_pipeline.py   # Pathway ingestion + vector store
├── agent.py              # Reasoning + answer generation
├── app.py                # Streamlit UI
├── requirements.txt
└── README.md

---

## STEP-BY-STEP RUN INSTRUCTIONS

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add regulatory documents
Edit or add text files inside:
```
data/regulations/
```

### 3. Run the app
```bash
streamlit run app.py
```

### 4. LIVE DEMO
- Ask a question
- Edit a document in `data/regulations/`
- Ask again → answer updates instantly

---

## WHAT TO CHANGE (IMPORTANT)
- Replace OpenAI API key in `agent.py`
- Replace document text to show live updates

---

## Why this wins
✔ No re-embedding  
✔ No redeploy  
✔ Real-time reasoning  
✔ Clear demo