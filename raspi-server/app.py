import os

from flask import Flask, request, send_from_directory
from flask import Flask


app = Flask(__name__)
IMAGE_NAME = 'snacks.jpg'

@app.route('/')
def index():
    return 'Hello world'

@app.route('/image/')
def get_image():
    return send_from_directory('static', IMAGE_NAME)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
