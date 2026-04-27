# 🐳 Flask + MySQL 2-Tier Application

## 📌 Overview

This is a simple Flask application that interacts with a MySQL database. Users can submit messages via a frontend form, which are then stored in a MySQL database and displayed on the frontend.

---

## ⚙️ Tech Stack

* Python (Flask)
* MySQL
* Docker
* Docker Compose

---

## 🚀 How to Run the Application

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd <your-project-folder>
```

---

### 2. Run using Docker Compose

```bash
docker-compose up --build
```

---

### 3. Access the app

Open your browser:

```
http://localhost:5000
```

---

## 🔐 Environment Variables

### For Web (Flask App)

* `MYSQL_HOST` = db
* `MYSQL_USER` = root
* `MYSQL_PASSWORD` = test@123
* `MYSQL_DB` = my_db

### For Database (MySQL)

* `MYSQL_ROOT_PASSWORD` = test@123
* `MYSQL_DATABASE` = my_db

---

## 🧪 Features

* Flask web interface
* MySQL database integration
* Dockerized setup
* Multi-container architecture using Docker Compose

---

## 📦 Docker Hub Image

```
https://hub.docker.com/r/yourdockerhubusername/flask-app
```

---

## 🧠 Learnings

* Containerization using Docker
* Multi-container setup with Docker Compose
* Environment variable management
* Healthchecks and service dependencies

---
