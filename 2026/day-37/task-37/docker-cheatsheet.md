# 🐳 Docker Cheat Sheet

## 📦 Container Commands

* `docker run -d -p 5000:5000 --name app image` → Run container in background with port mapping
* `docker ps` → List running containers
* `docker ps -a` → List all containers
* `docker stop <container>` → Stop a running container
* `docker rm <container>` → Remove a container
* `docker exec -it <container> /bin/bash` → Access container shell
* `docker logs <container>` → View container logs

---

## 🖼️ Image Commands

* `docker build -t name:tag .` → Build image from Dockerfile
* `docker pull image:tag` → Download image from registry
* `docker push name:tag` → Push image to Docker Hub
* `docker tag src:tag dest:tag` → Tag image for registry
* `docker images` → List images
* `docker rmi <image>` → Remove image

---

## 💾 Volume Commands

* `docker volume create name` → Create named volume
* `docker volume ls` → List volumes
* `docker volume inspect name` → View volume details
* `docker volume rm name` → Remove volume

---

## 🌐 Network Commands

* `docker network create name` → Create custom network
* `docker network ls` → List networks
* `docker network inspect name` → View network details
* `docker network connect net container` → Connect container to network

---

## ⚙️ Compose Commands

* `docker compose up -d --build` → Start services in background (build if needed)
* `docker compose down` → Stop and remove containers
* `docker compose ps` → List compose services
* `docker compose logs` → View logs
* `docker compose build` → Build services

---

## 🧹 Cleanup Commands

* `docker system prune` → Remove unused data (containers, networks, images)
* `docker system prune -a` → Remove all unused images
* `docker system df` → Show Docker disk usage

---

## 📝 Dockerfile Instructions

* `FROM` → Base image
* `RUN` → Execute command during build
* `COPY` → Copy files from host to image
* `WORKDIR` → Set working directory
* `EXPOSE` → Document container port
* `CMD` → Default command (overridable)
* `ENTRYPOINT` → Fixed command

---
