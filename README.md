# 📜 National Live Regulatory Intelligence Agent

A real-time policy intelligence system that continuously ingests updates from authoritative Indian government portals and converts regulatory noise into concise, actionable insights.

This project demonstrates **live data ingestion, change detection, signal extraction, and deterministic policy reasoning** across multiple public governance domains.

---

## 🚀 Project Overview

Government policy portals are information-dense, archive-heavy, and difficult to track in real time.  
This system addresses that problem by acting as a **live regulatory intelligence layer**.

It:
- Monitors official policy sources continuously  
- Detects updates automatically  
- Filters archival and navigational noise  
- Extracts only meaningful regulatory signals  
- Answers natural-language policy and eligibility questions  

The goal is **clarity, freshness, and relevance**, not document dumping.

---

## 🧠 Policy Domains Covered

| Sector | Authority |
|------|----------|
| 🎓 Education | Ministry of Education / UGC |
| 💰 Finance | Reserve Bank of India (RBI) |
| 🏥 Healthcare | Ministry of Health & Family Welfare |
| 👷 Labour | Ministry of Labour & Employment |
| 💻 Digital & IT | Ministry of Electronics & IT |

Each domain is ingested independently from its official source.

---


## 📂 Project Structure

live_regulatory_agent/
│
├── app.py # Streamlit UI
├── agent.py # Policy intelligence & summarization
├── pathway_pipeline.py # Policy retrieval logic
├── requirements.txt
├── README.md
│
├── ingestion/
│ ├── scraper_engine.py # Live ingestion & update detection
│ ├── internet_ingestion.py
│ └── sources.py # Source registry
│
├── data/
│ ├── education/
│ ├── finance/
│ ├── healthcare/
│ ├── labour/
│ └── digital/
│
└── .gitignore

## 🏗️ High-Level Architecture

Official Government Portals
↓
Live Ingestion Engine
(scraper_engine.py)
↓
Noise Filtering + Change Detection
↓
Sector-wise Policy Store (data/)
↓
Policy Retrieval & Prioritization
(pathway_pipeline.py)
↓
Policy Intelligence Layer
(agent.py)
↓
Streamlit Interface
(app.py)


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/RIAgent.git
cd RIAgent

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
Activate it: venv\Scripts\activate

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
▶️ Running the Application
```bash
streamlit run app.py

## ⚠️ Disclaimer

This project is built for academic and demonstrative purposes.  
It is **not a substitute for official legal or regulatory advice**.
