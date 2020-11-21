from flask.blueprints import Blueprint
from flask import render_template
from Models.Group import Group
group = Blueprint('group', __name__,
                 template_folder='templates',
                 static_folder='static')
@group.route('/group')
def index2():
    return render_template('index2.html', groups=Group.query.all())