from flask import Flask ,redirect,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/US')
def US_func():  # put application's code here
    #TODO
    #DO SOMTHING WITH DB
    return redirect('/tomer')


@app.route('/tomer')
def TOMER_func():  # put application's code here
    return 'tomer levavi page!'

@app.route('/about' ,methods=['GET','POST'])
def about_func():  # put application's code here
    #TODO
    #DO SOMTHING WITH DB
    return redirect(url_for('catalog_func'))

@app.route('/catalog')
def catalog_func():  # put application's code here
    return 'catalog page!'

if __name__ == '_main_':
    app.run(debug=True)