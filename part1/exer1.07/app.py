from flask import Flask, jsonify
import random
import string
import datetime
import time
import threading
import uuid

app = Flask(__name__)

# Initialize variables
current_timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
current_uuid = 'Initial UUID'


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
    response = f"{current_timestamp}: {current_uuid}"
    return response


if __name__ == '__main__':
    import uuid  # Import the uuid module
    app.run(host='0.0.0.0', port=8080)
