# 📦 Day 36 - Docker Project

## 🚀 Application Chosen

I chose a **Flask + MySQL 2-tier web application**.

### Why this app?
* It demonstrates **real-world architecture** (frontend + database)
* Helps understand **container networking**
* Covers important DevOps concepts like:

  * Environment variables
  * Multi-container setup
  * Healthchecks
* Useful for interviews as it shows **practical implementation**

---

## 🐳 Dockerfile (with explanation)

```dockerfile
# Use a lightweight Python base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create a non-root user
RUN useradd -m shweta

# Give ownership of app files to non-root user
RUN chown -R shweta:shweta /app

# Switch to non-root user
USER shweta

# Run the application
CMD ["python", "app.py"]
```

---

## ⚠️ Challenges Faced & Solutions

### 1. ❌ MySQL connection error

**Error:**
`Can't connect to local server through socket`

**Cause:**
Flask was trying to connect to `localhost` instead of MySQL container.

**Solution:**

* Used Docker network
* Updated host to `mysql-container`

---

### 2. ❌ mysqlclient build failure

**Error:**
`pkg-config: not found`

**Cause:**
Missing system dependencies in slim image.

**Solution:**
Installed:

* `gcc`
* `default-libmysqlclient-dev`
* `pkg-config`

---

### 3. ❌ Flask & Werkzeug version conflict

**Cause:**
Incompatible versions in `requirements.txt`

**Solution:**
Upgraded Flask to match Werkzeug version.

---

### 4. ❌ MySQL not ready when Flask starts

**Cause:**
Container startup timing issue.

**Solution:**

* Added **healthcheck**
* Used `depends_on` with `service_healthy`

---

## 📦 Final Image Size

```bash
docker images
```

Example output:

```
flask-app   latest   xxxMB
```

👉 Final Image Size: **~400-500 MB** (approx, depends on build)

---

## 🔗 Docker Hub Link

👉 https://hub.docker.com/repository/docker/twsdocker1/myflask-app

---

## 🎯 Key Learnings

* Dockerfile optimization
* Handling system dependencies
* Container networking
* Environment variable management
* Healthchecks and service dependencies

---
