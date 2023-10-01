from flask import Flask, send_from_directory

from datetime import datetime, timedelta
import requests
import os

app = Flask(__name__)


@app.route('/')
def hello():
    port = int(os.getenv("PORT", 8080))
    return f"Server started in port {port}\n"


@app.route('/version')
def version():
    return {"version": "0.6"}


CACHE_DIR = 'files/images'
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)
CACHE_FILENAME = os.path.join(CACHE_DIR, 'cached_image.jpg')
last_cached_timestamp = None
LOREM_PICSUM_URL = 'https://picsum.photos/1200'


def fetch_random_image():
    res = requests.get(LOREM_PICSUM_URL)
    if res.status_code == 200:
        with open(CACHE_FILENAME, 'wb') as f:
            f.write(res.content)


def get_cached_or_fetch_random_image():
    global last_cached_timestamp
    current_time = datetime.now()

    if last_cached_timestamp is None or (current_time - last_cached_timestamp) >= timedelta(days=1):
        fetch_random_image()
        last_cached_timestamp = current_time


@app.route('/random-pic')
def random_pic():
    get_cached_or_fetch_random_image()
    return send_from_directory(CACHE_DIR, 'cached_image.jpg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)))
