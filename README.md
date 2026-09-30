# Simple python API

Минимальное API на FastAPI.

### Стек

- Python 3.12+
- FastAPI
- Uvicorn

### 1. Виртуальное окружение

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Зависимости

```bash
pip install -r requirements.txt
```

### Локальный запуск

```bash
python -m uvicorn app.main:app --reload --port 8000
```

### URL


| Что          | Эндпоинт                           |
| ------------ | ---------------------------------- |
| Swagger UI   | http://localhost:8000/docs         |
| ReDoc        | http://localhost:8000/redoc        |
| OpenAPI JSON | http://localhost:8000/openapi.json |

### Поток

```text
HTTP-запрос (JSON)
    ↓
[Роутер]              ← валидация через схему, вызов сервиса
    ↓
[Сервис]              ← бизнес-логика, работа с БД через SQLAlchemy-модель
    ↓
[SQLAlchemy-модель]
    ↓
БД
```

### Описание структуры

```text
simple-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # Точка входа: создание FastAPI, подключение роутеров
│   ├── database.py          # Подключение к БД, сессии, Base
│   │
│   ├── models/              # SQLAlchemy-модели (таблицы)
│   │   ├── __init__.py
│   │   └── request_log.py
│   │
│   ├── schemas/             # Pydantic-схемы (валидация запросов/ответов)
│   │   ├── __init__.py
│   │   └── request_log.py
│   │
│   ├── api/                 # Роутеры (эндпоинты)
│   │   ├── __init__.py
│   │   └── request_logs.py
│   │
│   ├── services/            # Бизнес-логика
│   │   ├── __init__.py
│   │   └── request_log.py
│   │
│   └── core/                # Security, utils, exceptions (пока пусто)
│       └── __init__.py
│
├── .env                     # Секреты (не коммитится!)
├── .gitignore
├── requirements.txt
└── README.md
```

### Слои приложения
| Слой                 | Что содержит              |
| -------------------- | ------------------------- |
| Роутер `(api/)`      | HTTP, пути, коды ответа   |
| Сервис `(services/)` | Бизнес-логику, SQLAlchemy |
| Модель `(models/)`   | Таблицу БД                |
| Схема `(schemas/)`   | Форму запроса/ответа      |

### API
| Метод | Путь                        | Описание                    |
| ----- | --------------------------- | --------------------------- |
| POST  | `/api/logs`                 | Создать запись об обращении |
| GET   | `Бизнес-логику, SQLAlchemy` | Список всех записей         |