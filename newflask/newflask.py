from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!你好世界！'

@app.route('/user/<username>')
def user(username):
    return "hello,%s" % username

if __name__ == '__main__':
    app.run(debug=True)
