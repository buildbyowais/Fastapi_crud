# 📝 Todo API

A simple and well-structured **RESTful Todo API** built with **FastAPI**, **SQLAlchemy**, **MySQL**, and **Alembic**. This project demonstrates complete CRUD (Create, Read, Update, Delete) operations while following a clean, modular architecture.

---

## 🚀 Features

* Create a new Todo
* View all Todos
* Get a Todo by ID
* Update an existing Todo
* Delete a Todo
* Request validation using Pydantic
* Database migrations using Alembic
* Modular project structure
* Interactive API documentation with Swagger UI

---

## 🛠️ Tech Stack

* **FastAPI**
* **SQLAlchemy**
* **MySQL**
* **Alembic**
* **Pydantic**
* **Python Dotenv**
* **Uvicorn**

---

## 📁 Project Structure

```text
project/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   ├── api/
│   │   └── todo.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── crud/
│   │   └── todo.py
│   │
│   ├── models/
│   │   └── todo.py
│   │
│   ├── schemas/
│   │   └── todo.py
│   │
│   └── __init__.py
│
├── .env
├── alembic.ini
├── main.py
└── requirements.txt
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Configuration

Create a `.env` file in the project root.

```env
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=todo_db
```

---

## 🔄 Run Database Migrations

Generate a migration:

```bash
alembic revision --autogenerate -m "Initial Migration"
```

Apply the migration:

```bash
alembic upgrade head
```

---

## ▶️ Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

| Method | Endpoint      | Description           |
| ------ | ------------- | --------------------- |
| POST   | `/todos`      | Create a new Todo     |
| GET    | `/todos`      | Retrieve all Todos    |
| GET    | `/todos/{id}` | Retrieve a Todo by ID |
| PUT    | `/todos/{id}` | Update a Todo         |
| DELETE | `/todos/{id}` | Delete a Todo         |

---

## 🏗️ Architecture

The project follows a layered architecture:

* **Models** – SQLAlchemy database models
* **Schemas** – Pydantic request and response validation
* **CRUD** – Database operations
* **API** – Route definitions and HTTP endpoints
* **Core** – Database connection and configuration

This separation keeps the code clean, reusable, and easy to maintain.

---

## 🎯 Learning Objectives

This project demonstrates:

* REST API development with FastAPI
* CRUD operations
* SQLAlchemy ORM
* MySQL database integration
* Alembic migrations
* Environment variable management
* Modular backend architecture
* Dependency Injection using FastAPI

---

## 📄 License

This project is developed for learning and educational purposes.
