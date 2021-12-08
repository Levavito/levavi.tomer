from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
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
    return 'catalog page!'


if __name__ == '__main__':
    app.run(debug=True)
