from flask import Blueprint, render_template
from interact_with_DB import interact_db

# assignment10 blueprint definition
assignment10 = Blueprint('/assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')


# Routes
@assignment10.route('/assignment10')
def index():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)
