import os
import time
import json
import requests
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")  # убедись, что ключ в .env под этим именем
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
last_request_time = 0

def analyze_entry(text: str) -> dict:
    global last_request_time
    if time.time() - last_request_time < 1:
        raise Exception("Слишком частые запросы")
    last_request_time = time.time()

    prompt = f"""
    Прочитай следующий дневниковый текст и выполни анализ:

    1. Определи настроение (например: радостное, тревожное, усталое и т.п.)
    2. Выдели основные эмоции
    3. Дай короткий совет на основе текста

    Текст:
    \"\"\"{text}\"\"\"

    Ответ верни в JSON формате:
    {{
        "mood": ...,
        "emotions": [...],
        "advice": ...
    }}
    """

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "Ты психолог и аналитик дневников."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500,
    }

    response = requests.post(TOGETHER_API_URL, headers=headers, json=data)

    if response.status_code != 200:
        return {"error": f"HTTP {response.status_code}", "details": response.text}

    try:
        answer = response.json()["choices"][0]["message"]["content"]
        return json.loads(answer)
    except Exception as e:
        return {"error": "Ошибка при разборе ответа модели", "raw": response.text}
