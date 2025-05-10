from flask import Flask
from logic import add
app = Flask(__name__)

@app.route('/')


def home():
    return str(add(9,11))

if __name__ == '__main__':
    app.run(debug=True)
