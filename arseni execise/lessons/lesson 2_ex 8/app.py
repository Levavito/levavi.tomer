from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session
from interact_with_DB import interact_db


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

@app.route('/users')
def users_func():  # put application's code here
    query = 'select * from users'
    users = interact_db(query=query, query_type='fetch')
    return render_template('users.html', users=users)

@app.route('/insert_user', methods=['POST'])
def insert_user_func():  # put application's code here
    #get the dadt
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    query = "INSERT INTO users(name,email,password) VALUES ('%s', '%s', '%s');" % (name, email, password)
    interact_db(query=query, query_type='commit')

    return redirect('/users')




if __name__ == '__main__':
    app.run(debug=True)
