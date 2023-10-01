from flask import Flask, jsonify

app = Flask(__name__)

# Initialize the counter
counter = 0


@app.route('/pingpong', methods=['GET'])
def pingpong():
    global counter
    counter += 1
    response = f"pong {counter}"
    return jsonify({'message': response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
