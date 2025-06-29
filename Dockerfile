# syntax=docker/dockerfile:1.3
FROM python:3.8-slim-buster

WORKDIR /application

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy only requirements to leverage caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Use gunicorn for production WSGI serving
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "application:app"]

