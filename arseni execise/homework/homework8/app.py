from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session

from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '1234'
app.config.from_pyfile('settings.py')

users = {'user1': {'name': 'Yossi', 'email': 'yo@gmail.com'},
         'user2': {'name': 'Tomer', 'email': 'to@gmail.com'},
         'user3': {'name': 'Ariel', 'email': 'ar@gmail.com'},
         'user4': {'name': 'Bar', 'email': 'ba@gmail.com'},
         'user5': {'name': 'Nir', 'email': 'ni@gmail.com'},
         }


@app.route('/')
def Home_func():  # put application's code here
    found = True
    if found:
        return render_template('cv1.html', username='tomer')
    else:
        return render_template('cv1.html')

@app.route('/assignment8', methods=['GET', 'POST'])
def about_func():  # put application's code here
    name = 'tomer'
    second_name = 'levavi'
    uni = 'BGU'
    return render_template('assignment8.html',
                           username='tomer',
                           profile={'name' : 'tomer' , 'second_name' : 'levavi'},
                           name=name,
                           university=uni,
                           second_name=second_name,
                           degreas=['BSc', 'MSc', 'GrandMaster'],
                           hobies=('art', 'music', 'sql'))

@app.route('/assignment9', methods=['GET', 'POST'])
def login_func():  # put application's code here
    print(users.values())
    if request.method == 'GET':
        if session['username']:
            if 'search_user' in request.args:
                search_user = request.args['search_user']
                return render_template('assignment9.html', username=session['username']
                                       , search_user=search_user
                                       , users=users)
            return render_template('assignment9.html', users=users, username=session['username'])
        return render_template('assignment9.html', users=users)
    if request.method == 'POST':
        print('fffff')
        #DB
        username = request.form['username']
        Password = request.form['password']
        found = True
        if found:
            session['username'] = username
            session['user_login'] = True
            print('sssss')
            return render_template('assignment9.html', username=username, users=users)
        else:
            print('mmmm')
            return render_template('assignment9.html')

@app.route('/logout')
def logiout_func():  # put application's code here
    session['username'] = ''
    return render_template('cv1.html')



###### Pages
## assignment10
from Pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


@app.route('/insert_user', methods=['POST'])  # get the record that was inserted into the form
def insert_user_func():
    # get the data
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    #insert to db
    query = "insert into users(name,email,password) values ('name', 'email', 'password');"
    interact_db(query=query, query_type='commit')

    #come back to users
    return redirect('/users')


@app.route('/delete_user', methods=['post'])
def delete_user_func():
    user_id = request.form['id']
    query = "delete from users where id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/users')


@app.route('/catalog')
def catalog_func():  # put application's code here
    return 'catalog page!'


if __name__ == '__main__':
    app.run(debug=True)
