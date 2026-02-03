# 🚀 RPA Automation Dashboard (FastAPI + Selenium + Streamlit)

## 📌 Overview
This project demonstrates an end-to-end RPA automation workflow where a user
triggers Selenium-based automation from a Streamlit UI, orchestrated via FastAPI,
and downloads structured data as a CSV file.

## 🧩 Architecture
Streamlit (UI) → FastAPI (API Layer) → Selenium (RPA) → CSV Output

## 🛠 Tech Stack
- Python 3.11
- FastAPI
- Uvicorn
- Selenium
- Streamlit
- Pandas

## ⚙️ Features
- UI-triggered automation
- REST API orchestration
- Selenium web automation
- CSV data generation and download
- Modular, production-style structure

## ▶️ How to Run

### 1️⃣ Setup Virtual Environment
```bash
python -m venv autodash.venv
autodash.venv\Scripts\activate
pip install -r requirements.txt
2️⃣ Start FastAPI Backend
bash
Copy code
python -m uvicorn backend.main:app --reload
3️⃣ Start Streamlit UI
bash
Copy code
streamlit run frontend/app.py
4️⃣ Open Browser
Streamlit UI: http://localhost:8501

FastAPI Docs: http://localhost:8000/docs

📤 Output
Automation generates a downloadable CSV file containing extracted data.

🎯 Use Case
RPA dashboards

Automation orchestration

Data extraction pipelines

Enterprise automation demos

yaml
Copy code

---

## 🧾 Next (Optional but Powerful Enhancements)

If you want to level this up further:
- ✅ Add logging (`logs/automation.log`)
- ✅ Add scheduler (cron / APScheduler)
- ✅ Add Dockerfile
- ✅ Add multiple automation types (News / Jobs / Stocks)
- ✅ Add API authentication

---

## 🏁 Final Verdict

✔ **Automation worked**  
✔ **Project is GitHub-worthy**  
✔ **Demonstrates real enterprise automation skills**  

👉 Next step:  
**Push this to GitHub** and I’ll help you write:
- Resume bullet points
- LinkedIn post
- Interview explanation

Just say **“Next”** 👍

## 🎥 Demo Video
A complete walkthrough of the automation execution:
- FastAPI backend
- Streamlit UI
- Selenium automation
- CSV output

📺 Video: https://drive.google.com/file/d/1JtxdJuNUq7OwBxqMGHbe1advzJaXNwAC/view?usp=sharing
