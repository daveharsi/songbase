from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello world!!!</h1>'


@app.route('/users/<string:name>/')
def get_user(name):
    return 'hello %s your age is %d' % (name, 20)


@app.route('/users')
def show_all_users():
    return '<h2>this is the page for all users</h2>'


if __name__ == '__main__':
    app.run(debug=True)
