from flask import Flask
from flask_sslify import SSLify


app = Flask(__name__)
sslify = SSLify(app) # для https


#простая вьюха

@app.route('/')
def index():
    return '<h1>Test Flask app</h1>'

if __name__ == '__main__':
    app.run()