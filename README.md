# 🤖 LLM-powered Data Query Bot

> Ask your database questions in plain English. Get SQL + results instantly. Built with LangChain, OpenAI, and Streamlit.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white)

---

## 💡 What It Does

Non-technical users type questions like:

> *"What were the top 5 restaurants by revenue last month in Bangalore?"*

The bot:
1. Converts the question to SQL using GPT-4
2. Runs the query against your database
3. Returns results + a plain-English explanation

---

## 🏗️ Architecture

```
User Input (natural language)
        │
        ▼
   LangChain Agent
        │
   ┌────┴────┐
   │  OpenAI │  ← generates SQL
   └────┬────┘
        │
        ▼
  SQLite / PostgreSQL
        │
        ▼
  Results + Explanation
        │
        ▼
  Streamlit UI
```

---

## 🚀 Quick Start

```bash
git clone https://github.com/YOUR_USERNAME/llm-data-query-bot
cd llm-data-query-bot
pip install -r requirements.txt
echo "OPENAI_API_KEY=your_key_here" > .env
streamlit run app/main.py
```

---

## 📁 Structure

```
llm-data-query-bot/
├── app/
│   ├── main.py           # Streamlit UI
│   └── query_engine.py   # LangChain + SQL logic
├── prompts/
│   └── system_prompt.txt # Custom prompt for SQL generation
├── utils/
│   └── db_utils.py       # DB connection helpers
└── requirements.txt
```

---

## 🔧 Example Queries

| Natural Language | Generated SQL |
|---|---|
| Top 5 cities by orders today | `SELECT city, COUNT(*) ... ORDER BY 2 DESC LIMIT 5` |
| Average delivery time this week | `SELECT AVG(delivery_time_mins) ...` |
| Restaurants with >10% cancellation | `SELECT ... HAVING cancellation_rate > 0.10` |

---

## 🌱 Inspired by my work at Swiggy

At Swiggy, ops teams often needed quick data answers but couldn't write SQL. This bot bridges that gap — a pattern applicable to any data-heavy organisation.
