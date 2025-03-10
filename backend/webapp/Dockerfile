FROM python:3.12-slim

WORKDIR /webapp

RUN apt-get update && \
    apt-get install -y libpq-dev gcc curl

COPY src/ .
# RUN chown -R 1000:1000 /webapp

RUN pip install -r requirements.txt --no-cache-dir --no-deps

# ENTRYPOINT python main.py