from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Aplicação Flask rodando com Docker!💪"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
