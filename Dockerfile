FROM python:3.9.7-slim-buster as builder

WORKDIR /app
COPY . /app

RUN pip install gunicorn

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9.7-slim-buster

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

WORKDIR /app
COPY . /app

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

