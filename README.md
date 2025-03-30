# Структура проекта:
project/ 
├── app/
│   ├── api/             # эндпоинты
│   ├── core/            # конфиги и celery
│   ├── cruds/           # CRUD-операции с БД
│   ├── db/              # подключение к БД
│   ├── models/          # модели таблиц
│   ├── schemas/         # схемы Pydantic
│   ├── services/        # алгоритмы и задачи
│   └── main.py          # точка входа
├── alembic/             # миграции
└── app.db               # SQLite база данных

# Запуск проекта:

# Установить зависимости

pip install -r requirements.txt

# Применить миграции

alembic upgrade head

# Запустить Redis (если нужен асинхронный поиск)

# Запустить Celery worker:

celery -A app.core.celery_app.celery worker --loglevel=info -Q search --pool=solo

# Запустить FastAPI сервер:

uvicorn app.main:app --reload

# Открыть Swagger UI: http://127.0.0.1:8000/docs

# Аутентификация:

POST /sign-up/ — регистрация (email + password)

POST /login/ — вход и получение JWT

GET /users/me/ — получить данные текущего пользователя

Для доступа к защищённым маршрутам — нажмите "Authorize" в Swagger и введите Bearer <ваш_токен>

# Работа с корпусами:

POST /upload_corpus — загрузить текстовый корпус (название + содержимое)

GET /corpuses — получить список всех корпусов

# Алгоритмы поиска:

# Реализовано два алгоритма нечеткого поиска

levenshtein — расстояние Левенштейна (через rapidfuzz)

ngram — метод N-грамм

# Эндпоинт: 

POST /search_algorithm

# Тело запроса:

{
  "query": "matrix",
  "algorithm": "levenshtein",
  "corpus_id": 1
}

# Ответ:

{
  "results": ["The Matrix"],
  "duration": 3.25
}

#Realtime (WebSocket)

ws://localhost:8000/ws/search

Можно подключиться через WebSocket-клиент и отправлять строки для поиска — ответы приходят в реальном времени.

#Асинхронный поиск через Celery

POST /search/async/ — запустить задачу поиска

GET /search/result/{task_id} — получить результат

# Реализовано в рамках лабораторной работы по теме "Нечеткий поиск" ПМ23-5 Толстопятенко А.О. 
