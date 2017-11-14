from flask import Flask, session, render_template, request, redirect, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'lawf2963645hfbcjd'


@app.route('/')
def index():
    # return '<h1>hello world!!!</h1>'
    return render_template('index.html')


@app.route('/form-demo', methods = ['GET', 'POST'])
def form_demo():
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html', first_name=first_name)
        else:
            return render_template('form-demo.html', first_name=session.get('first_name'))

    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        return redirect(url_for('form_demo'))


@app.route('/mysong')
def mysong():
    return render_template('my-song.html')


@app.route('/users/<string:name>/')
def get_user(name):
    # return 'hello %s your age is %d' % (name, 20)
    return render_template('user.html', user_name=name)


@app.route('/songs')
def get_all_songs():
    songs = [
        'Paradise',
        'Yellow',
        'Viva La Vida'
    ]
    return render_template('songs.html', songs=songs)


@app.route('/users')
def show_all_users():
    return '<h2>this is the page for all users</h2>'


if __name__ == '__main__':
    app.run()
