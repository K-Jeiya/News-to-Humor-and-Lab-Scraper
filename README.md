# News to Humor & Labs Scraper – Data Engineering Assignment

### 🧠 Overview
This repository contains two parts of my data engineering assignment:
1. **News to Humor API:**  
   A Python + Flask application that fetches news from NewsAPI and converts the descriptions into humorous versions using an LLM API.

2. **Labs Scraper:**  
   A Python web scraper that extracts test details from 10 lab pages on [Marham.pk](https://www.marham.pk/labs).

---

### ⚙️ Tech Stack
- Python
- Flask
- Requests
- BeautifulSoup
- NewsAPI
- LLM APIs (Groq, Hugging Face)
- CSV, JSON, REST API

---

### 🧩 Files
- `humourous_app_jeiyakumari.py` → Flask App for Humor News API  
- `marham_app_jeiyakumari.py` → Web Scraper for Lab Tests  
- `requirements.txt` → Dependencies  
- `labs_data.csv` → Scraped Lab Data  
- `news.json` → Fetched News Data  

---

### 🚫 Note
`.env` file is not included (for API key security).  
You can create your own `.env` file with:
- NEWS_API_KEY=your_api_key
- LLM_API_KEY=your_api_key
