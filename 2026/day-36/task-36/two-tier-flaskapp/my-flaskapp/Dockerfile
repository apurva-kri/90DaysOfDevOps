FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# prevents pip from storing downloaded packages in cache, Keeps your Docker image smaller, Avoids unnecessary files inside the container
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

# using non root user for security
RUN useradd -m shweta

RUN chown -R shweta:shweta /app

USER shweta

CMD ["python","app.py"]









