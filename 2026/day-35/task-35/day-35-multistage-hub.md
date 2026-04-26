# Day 35 – Multi-Stage Builds & Docker Hub

## Single Stage Image

Base Image: node:18  
Image Size: ~1.09 GB

Problem:
- Includes build tools
- Includes npm cache
- Large attack surface

---

## Multi-Stage Image

Builder Stage: node:18  
Runtime Stage: node:18-alpine

Image Size: ~170 MB

### Why Smaller?

Multi-stage builds copy only the final application
and discard build dependencies.

>`RUN npm ci --only=production` **ci means Continuous Integration install**

This command:
- reads package.json
- updates package-lock.json if needed
- may install slightly different dependency versions

That flexibility is convenient for development but **dangerous** for repeatable builds.

>`--target /app/lib` also add on RUN command to put all dependencies to this directory and also change the directory name as i wish


---

## Docker Hub

Repository:
https://hub.docker.com/repository/docker/twsdocker1/multi-stage/general

Commands used:

docker login
docker tag multi-stage twsdocker1/node-demo:v1
docker push twsdocker1/node-demo:v1

---

## Best Practices Applied

- Used alpine base image
- Added non-root user
- Combined RUN commands
- Used specific tag