import datetime
import re
import time
import threading
import uuid

from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Initialize variables
current_timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
current_uuid = ""


# Function to update timestamp and UUID in the background
def update_values():
    global current_timestamp, current_uuid
    while True:
        current_uuid = str(uuid.uuid4())
        current_timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        time.sleep(5)


# Start a background thread to continuously update values
update_thread = threading.Thread(target=update_values)
update_thread.daemon = True
update_thread.start()


@app.route('/')
def index():
    pingpong = (
        requests.get("http://exer2-01-pingpong-svc/pingpong")
        .json()
        .get("message", "")
    )
    counter = re.findall("\d+", pingpong)[0]
    
    response = f"""{current_timestamp}: {current_uuid}
    Ping / Pongs {counter}"""
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
