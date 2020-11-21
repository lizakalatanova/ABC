from flask.blueprints import Blueprint
from flask import render_template
from Models.Interval import Interval

interval = Blueprint('interval', __name__,
                 template_folder='templates',
                 static_folder='static')


@interval.route('/interval')
def index1():
    return render_template('index1.html', intervals=Interval.query.all())