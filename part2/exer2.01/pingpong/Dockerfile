FROM python:3.11.5-slim-bookworm

WORKDIR /usr/src/app

ENV PORT=8080

COPY requirements.txt ./

# Mounting a persistent volume overwrites these
# and breaks the python user's permissions over the directory
RUN adduser python && \
  pip install --no-cache-dir -r requirements.txt && \
  mkdir files && touch files/pingpong-logs.txt && \
  chown python:python files/

COPY --chown=python:python . .

EXPOSE $PORT

# USER python

ENTRYPOINT ["python", "app.py"]
