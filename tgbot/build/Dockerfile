FROM python:3.10-slim

WORKDIR /bot_template

RUN apt-get update && \
    apt-get install -y libpq-dev gcc curl

COPY . /bot_template
RUN chown -R 1000:1000 /bot_template

RUN pip install -r requirements.txt --no-cache-dir --no-deps

# ENTRYPOINT python -m src.bot