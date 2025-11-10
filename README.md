


# 🚀 Topdoer Incident Tracker

Маленький сервис для учёта инцидентов, реализованный на **FastAPI** с использованием **PostgreSQL**, **SQLAlchemy**, **Alembic** и **Docker**.

---

## 📦 <Быстрый старт>

### 1️⃣ Клонирование репозитория
```bash
git clone https://github.com/AndreyFinyak/topdoer_Incident_tracker.git
cd topdoer_Incident_tracker
```

---

### 3️⃣ Запуск контейнеров

Собери и запусти проект:

Cопируй файл `.env.example` в `.env` и заполни его данными.

```bash
docker compose up -d --build
```

Эта команда:
- поднимет контейнер с **PostgreSQL**,
- применит **Alembic миграции**,
- запустит **FastAPI**-приложение на `http://localhost:8000`.

---

### 3️⃣ Проверка логов приложения

```bash
docker compose logs -f app
```

Если всё работает корректно, ты увидишь:

```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

### 5️⃣ Swagger-документация

После запуска перейди по адресу:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧱 Стек технологий

- **FastAPI** — основной веб-фреймворк
- **PostgreSQL** — база данных
- **SQLAlchemy** — ORM
- **Alembic** — миграции
- **Docker Compose** — оркестрация сервисов
- **Poetry** — управление зависимостями

---

## ⚙️ Полезные команды

Применить миграции вручную:
```bash
alembic upgrade head
```

Создать новую миграцию:
```bash
alembic revision --autogenerate -m "some message"
```

---

## ✅ Готово!

Теперь проект доступен по адресу:
👉 **http://localhost:8000**

---

## 📸 Примеры работы

> Скриншоты примеров работы сохранены в папке `examples/` в корне проекта.
