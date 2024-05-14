FROM python:3.9-slim AS builder
WORKDIR /app
COPY . /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /app/__pycache__ && \
    find /usr/local/lib/python3.9/ -name "*.pyc" -exec rm -f {} +



FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /app /app
CMD ["python", "app.py"]
