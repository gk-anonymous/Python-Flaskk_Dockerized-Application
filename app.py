from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dosto, LO HO GYA PYTHON APPLICATION BHI DOCKERIZED'

@app.route('/health')
def health():
    return 'Server is up and running'
