import time

from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session, json
import requests
import random
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
def users_func():
    query = 'select * from lesson.users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('users.html', users=users)


@app.route('/insert_user', methods=['post'])  # get the record that was inserted into the form
def insertUsers():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        check_input = "SELECT name FROM lesson.users WHERE name='%s';" % name
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into lesson.users (name, email , password)\
                            value ('%s', '%s', '%s');" % (name, email, password)
            interact_db(query=query, query_type='commit')
            # message
            return redirect('/users')
        else:
            # message
            return redirect('/users')
    return render_template('users.html', req_method=request.method)


@app.route('/delete_user', methods=['post'])
def delete_user_func():
    user_id = request.form['id']
    query = "delete from lesson.users where id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/users')

@app.route('/req_fronthand')
def req_fronthand_func():
    return render_template('req_fronthand.html')

def get_pokemons(num):
    pokemons = []
    for i in range(num):
        random_num = random.randint(1, 100)
        res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_num}')
        res = res.json()
        pokemons.append(res)
    return pokemons

@app.route('/req_backhand')
def req_backhand_func():
    num = 3;
    if "number" in request.args:
        num = int(request.args["number"])
    pokemons = get_pokemons(num)
    return render_template('req_backhand.html', pokemons=pokemons)






if __name__ == '__main__':
    app.run(debug=True)
