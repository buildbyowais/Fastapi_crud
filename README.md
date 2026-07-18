# 📝 Todo API with JWT Authentication

A secure and well-structured **RESTful Todo API** built with **FastAPI**, **SQLAlchemy**, **MySQL**, **Alembic**, and **JWT Authentication**. This project demonstrates complete CRUD (Create, Read, Update, Delete) operations with user authentication and authorization while following a clean, modular architecture.

---

## 🚀 Features

- User Registration
- User Login
- JWT Access Token Authentication
- JWT Refresh Token Support
- Protected Todo Endpoints
- Create a new Todo
- View all Todos
- Get a Todo by ID
- Update an existing Todo
- Delete a Todo
- Request validation using Pydantic
- Database migrations using Alembic
- Modular project structure
- Interactive API documentation with Swagger UI

---

## 🛠️ Tech Stack

- **FastAPI**
- **SQLAlchemy**
- **MySQL**
- **Alembic**
- **Pydantic**
- **Python-Jose (JWT)**
- **Passlib (Password Hashing)**
- **Python Dotenv**
- **Uvicorn**

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
│   │   ├── auth.py
│   │   └── todo.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── security.py
│   │
│   ├── crud/
│   │   ├── user.py
│   │   └── todo.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── todo.py
│   │
│   ├── schemas/
│   │   ├── user.py
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

### Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

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

JWT_SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

## 🔄 Database Migration

Generate Migration

```bash
alembic revision --autogenerate -m "Initial Migration"
```

Apply Migration

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

## 🔐 Authentication

This project uses **JWT (JSON Web Token)** for authentication.

### Authentication Flow

1. Register a new user.
2. Login with username and password.
3. Receive:
   - Access Token
   - Refresh Token
4. Use the Access Token in the Authorization header:

```
Authorization: Bearer <access_token>
```

5. Use the Refresh Token to generate a new Access Token when it expires.

---

## 📖 API Documentation

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | User login |
| POST | `/auth/refresh` | Refresh JWT Token |

---

### Todos (Protected)

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/todos` | Create Todo |
| GET | `/todos` | Get All Todos |
| GET | `/todos/{id}` | Get Todo by ID |
| PUT | `/todos/{id}` | Update Todo |
| DELETE | `/todos/{id}` | Delete Todo |

> **Note:** All Todo endpoints require a valid JWT Access Token.

---

## 🔒 Security

- JWT Authentication
- Access Tokens
- Refresh Tokens
- Password Hashing using Passlib (bcrypt)
- Protected API Routes
- Environment Variables for Sensitive Data

---

## 🏗️ Architecture

The project follows a clean layered architecture.

- **Models** – SQLAlchemy database models
- **Schemas** – Pydantic request and response validation
- **CRUD** – Database operations
- **API** – Route definitions
- **Core** – Database configuration, JWT, and security utilities

This structure makes the project scalable, maintainable, and easy to extend.

---

## 🎯 Learning Objectives

This project demonstrates:

- REST API development using FastAPI
- JWT Authentication
- Access & Refresh Tokens
- Password Hashing
- User Authentication & Authorization
- CRUD Operations
- SQLAlchemy ORM
- MySQL Integration
- Alembic Database Migrations
- Environment Variable Management
- Dependency Injection
- Clean Project Architecture

---

## 📄 License

This project is developed for learning and educational purposes.