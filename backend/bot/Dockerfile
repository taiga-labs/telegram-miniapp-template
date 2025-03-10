FROM python:3.12-slim

WORKDIR /bot

RUN apt-get update && \
    apt-get install -y libpq-dev gcc curl

COPY src/ .
# RUN chown -R 1000:1000 /bot

RUN pip install -r requirements.txt --no-cache-dir --no-deps

# ENTRYPOINT python main.py