from flask import Flask


app = Flask(__name__)


#простая вьюха

@app.route('/')
def index():
    return '<h1>Test Flask app</h1>'

if __name__ == '__main__':
    app.run()