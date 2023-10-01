FROM python:3.11.5-slim-bookworm

WORKDIR /usr/src/app

ENV PORT=8080

COPY requirements.txt ./

RUN adduser python && \
  pip install --no-cache-dir -r requirements.txt && \
  mkdir -p files/images && chown python:python files/

COPY --chown=python:python . .

EXPOSE $PORT

# USER python

ENTRYPOINT ["python", "app.py"]
