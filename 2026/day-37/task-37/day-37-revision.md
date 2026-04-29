## Day 37 – Docker Revision
- Run a container from Docker Hub (interactive + detached) - ```docker run -it twsdocker1/myflask-app```
- List, stop, remove containers and images - ```docker ps, docker stop <container-id>, docker rm <container-id>, docker rmi <imageid>```
- Explain image layers and how caching works
 - Image layers: Every Dockerfile instruction creates an immutable layer stacked to form the final image.
 - Caching: During builds, Docker reuses unchanged layers; if a layer changes, that layer and all layers after it are rebuilt.
 - Docker builds images in layers and reuses unchanged layers via caching to speed up builds.

- Write a Dockerfile from scratch with FROM, RUN, COPY, WORKDIR, CMD
```
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python","app.py"]
```
- Explain CMD vs ENTRYPOINT - CMD provides a default command that can be overridden, while ENTRYPOINT defines a fixed command that always runs unless explicitly replaced.

- Build and tag a custom image - ```docker build -t tag flask-app twsdocker1/flask-app:latest (Build creates the image, tag gives it a versioned name for sharing.)

- Create and use named volumes -```docker volume create my-volume``` use it with container ```docker run -d --name my-container -v my-volume:/app/data nginx```
  - my-volume = volume name
  - /app/data = path inside container
- Use bind mounts - ```-v <host_path>:<container_path>``` , - Your current folder is mounted to /app inside the container, Bind mount links a host directory to a container for real-time file sharing.
```
docker run -it \
  -v $(pwd):/app \
  python:3.12-slim \
  /bin/bash
  ```
- Create custom networks and connect containers - ```docker network create my-network```
```docker run -d --name web --network my-network -p 5000:5000 flask-app```
- Write a docker-compose.yml for a multi-container app(Flask + MySQL)
```
version: "3.9"

services:
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: test123
      MYSQL_DATABASE: my_db

  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      MYSQL_HOST: db
      MYSQL_USER: root
      MYSQL_PASSWORD: test123
      MYSQL_DB: my_db
    depends_on:
      - db
```
```
- 🧠 What’s happening
db → MySQL container
web → Flask app
MYSQL_HOST: db → connects using service name
depends_on → starts DB before web (basic order)
Docker Compose lets you run multiple containers together with one command.
```
- Use environment variables and .env files in Compose - Done

## Quick Fire Questions
1️⃣ Image vs Container
👉 Image = blueprint (read-only template)
👉 Container = running instance of that image

2️⃣ Data when container is removed
👉 Data inside container is lost unless stored in volumes/bind mounts

3️⃣ Communication on same custom network
👉 Containers communicate using container names (DNS)

4️⃣docker compose down vs down -v
down → removes containers, networks
down -v → also removes volumes (data deleted) ⚠️

5️⃣ Why multi-stage builds
👉 Reduce image size by keeping only required files in final image

6️⃣ COPY vs ADD
COPY → simple file copy
ADD → copy + extra features (URL fetch, auto-extract)
👉 Best practice: use COPY unless needed

7️⃣ -p 8080:80
👉 Maps:
8080 (host) → 80 (container)

8️⃣ Check Docker disk usage - ```docker system df```
- Note : Docker = images (templates), containers (runtime), networks (communication), volumes (data persistence)
  