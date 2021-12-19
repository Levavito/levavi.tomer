from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def home_func():  # put application's code here
    found = True
    if found:
        return render_template('web.html', username='tomer')
    else:
        return render_template('web.html')

@app.route('/about', methods=['GET', 'POST'])
def about_func():  # put application's code here
    name = 'tomer'
    second_name = 'levavi'
    uni = 'BGU'
    return render_template('About.html',
                           profile={'name' : 'tomer' , 'second_name' : 'levavi'},
                           name=name,
                           university=uni,
                           second_name=second_name,
                           degreas=['BSc', 'MSc', 'GrandMaster'],
                           hobies=('art', 'music', 'sql'))


@app.route('/catalog')
def catalog_func():  # put application's code here
    if 'user_login' in session:
        if session['user_login']:
            print('user_login')
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        return render_template('catalog.html', prod_name=product, prod_size=size)
    return render_template('catalog.html')

@app.route('/login', methods=['GET', 'POST'])
def login_func():  # put application's code here
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        #DB
        username = request.form['username']
        Password = request.form['password']
        found = True
        if found:
            session['username'] = username
            session['user_login'] = True
            return redirect(url_for('home_func'))
        else:
            return render_template('login.html')

@app.route('/logout')
def logiout_func():  # put application's code here
    session['username'] = ''
    return render_template('web.html')



if __name__ == '__main__':
    app.run(debug=True)
