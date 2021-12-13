from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)


@app.route('/')
def Home():  # put application's code here
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


@app.route('/catalog')
def catalog_func():  # put application's code here
    return 'catalog page!'


if __name__ == '__main__':
    app.run(debug=True)
