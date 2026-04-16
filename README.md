# 🍽 Recipe Extractor & Meal Planner

## 📌 Project Overview
This project extracts recipe data from a blog URL using web scraping and AI.

---

## 🚀 Features

- Extract recipe from URL
- Display ingredients, instructions, nutrition
- AI-powered data extraction (Gemini)
- History tab to view past recipes

---

## 🛠 Tech Stack

- Backend: FastAPI (Python)
- Frontend: React
- Scraping: BeautifulSoup
- AI: Google Gemini
- Database: (Currently in-memory, can extend to PostgreSQL)

---

## ⚙️ Setup Instructions

### 🔹 Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
