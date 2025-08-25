# InnoComments

**InnoComments** — это платформа для автоматического комментирования кода, основанная на FastAPI. Она предлагает API, которые в будущем можно будет использовать в различных инструментах разработки и интеграциях.

## Описание проекта

InnoComments предоставляет:

- Надёжное API для автокомментирования участков кода.
- Возможность масштабирования и доработки — возможность легко подключить новые языковые модели, расширить функционал, интегрировать с CI/CD или IDE.
- Простую архитектуру на базе FastAPI, с возможностью развертывания как локально, так и в облаке.

## Установка и запуск

```bash
# Клонируем репозиторий
git clone https://github.com/Black-persik/InnoCom-Test.git
cd InnoCom-Test

# Создаем виртуальное окружение
python -m venv venv
source venv/bin/activate  # или `venv\Scripts\activate` на Windows

# Устанавливаем зависимости
pip install -r requirements.txt

# Задаём необходимые переменные окружения
export DATABASE_URL={URL базы данных PostgreSQL}

# Меняем url в файле alembic.ini
sqlalchemy.url = {DATABASE_URL}

# Запуск приложения на сервере Render (старторвая команда)
uvicorn main:app --host 0.0.0.0 --port 10000 

# Миграции в базу данных
В терминале необходимо запустить команду
alembic revision --autogenerate -m "Add new tables"
alembic upgrade head
```
## Структура проекта
InnoCom-Test/
├── .idea/             # Конфигурация IDE (PyCharm/WebStorm и т.п.)
├── migrations/        # Миграции базы данных
├── models/            # SQLAlchemy / Pydantic модели
├── routers/           # Эндпоинты FastAPI (HTTP-маршруты)
├── schemas/           # Pydantic схемы для валидации запросов/ответов
├── utils/             # Утилитарный код (общие функции, вспомогательные классы)
├── LLM.py             # Логика взаимодействия с языковой моделью (LLM)
├── main.py            # Точка входа: создание приложения FastAPI, подключение роутеров
├── alembic.ini        # Конфигурация Alembic для миграций
└── requirements.txt   # Список зависимостей Python



