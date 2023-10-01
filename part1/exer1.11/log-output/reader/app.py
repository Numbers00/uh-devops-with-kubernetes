from flask import Flask
import os, uuid

app = Flask(__name__)


@app.route('/')
def index():
    current_timestamp = ""
    # From https://stackoverflow.com/a/54278929
    with open('files/timestamp-logs.txt', 'rb') as f:
        try:  # catch OSError in case of a one line file 
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        current_timestamp = f.readline().decode().strip()

    counter = 0
    with open('files/pingpong-logs.txt', 'rb') as f:
        try:  # catch OSError in case of a one line file 
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        counter = f.readline().decode().strip()
    
    current_uuid = str(uuid.uuid4())
    response = f"{current_timestamp}: {current_uuid}\nPing / Pongs: {counter}"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
