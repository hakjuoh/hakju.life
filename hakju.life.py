from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/redirect')
def redirect():
    return ''


@app.route('/privacy')
def privacy():
    return ''


if __name__ == '__main__':
    app.run()
