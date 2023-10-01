from flask import Flask
import datetime
import time
import threading

app = Flask(__name__)

# Initialize variables
current_timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")


# Function to update timestamp and UUID in the background
def update_values():
    global current_timestamp
    with open('files/timestamp-logs.txt', 'a') as f:
        while True:
            current_timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            f.write(current_timestamp + '\n')
            f.flush()  # Flush the buffer to write immediately
            time.sleep(5)   


# Start a background thread to continuously update values
update_thread = threading.Thread(target=update_values)
update_thread.daemon = True
update_thread.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
