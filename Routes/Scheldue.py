from flask.blueprints import Blueprint
from flask import render_template
from Models.Schedule import Schedule

schedule = Blueprint('schedule', __name__,
                 template_folder='templates',
                 static_folder='static')


@schedule.route('/schedule')
def index3():
    return render_template('scheldue.html', schedules=Schedule.query.all())