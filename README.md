# 🧠 AI-Diary — Анализ Дневника с Together AI

Этот проект — микросервис на FastAPI, который принимает текстовые записи из дневника пользователя и возвращает их психологический анализ с помощью языковой модели `Mixtral-8x7B-Instruct` от Together AI.

---

## 📦 Возможности

- Определение **настроения**
- Выделение **основных эмоций**
- Генерация **полезного совета**
- Работа с **бесплатной LLM** (через Together.ai)
- Защита от **частых запросов** (rate limiting)
- Возврат результата в **удобном JSON-формате**

---

## 🚀 Установка и запуск

1. **Клонировать репозиторий**:

```bash
git clone https://github.com/your-username/ai-diary.git
cd ai-diary

Создать и активировать виртуальное окружение:

bash
Копировать
Редактировать
python -m venv .venv
.venv\Scripts\activate
Установить зависимости:

bash
Копировать
Редактировать
pip install -r requirements.txt
Создать файл .env:

env
Копировать
Редактировать
TOGETHER_API_KEY=your_api_key_here
TOGETHER_API_URL=https://api.together.xyz/v1/chat/completions
API-ключ можно получить на: https://api.together.xyz/settings/api-keys

🧠 Пример запроса
bash
Копировать
Редактировать
POST /analyze
Content-Type: application/json

{
  "content": "Сегодня я был на лекции, потом гулял в одиночестве. На душе было тревожно, но под вечер стало легче."
}

🔁 Ответ:
json
Копировать
Редактировать
{
  "mood": "тревожное, но улучшающееся",
  "emotions": ["тревога", "одиночество", "облегчение"],
  "advice": "Попробуйте чаще гулять в компании или с близкими, это поможет справляться с тревожными мыслями."
}

🧾 Структура проекта
 
 ---

⚙️ Зависимости
fastapi

uvicorn

requests

python-dotenv

Установить можно командой:

bash
Копировать
Редактировать
pip install fastapi uvicorn requests python-dotenv

📌 Примечания
В качестве модели используется Mixtral-8x7B-Instruct, так как она доступна бесплатно на Together AI.

Функция analyze_entry ограничивает частоту вызова до 1 запроса в секунду.

🧑‍💻 Автор
Разработка: [@Egor SELIFANOV]

📜 Лицензия
Проект распространяется под MIT License.

