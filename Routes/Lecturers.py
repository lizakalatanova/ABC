from flask.blueprints import Blueprint
from flask import render_template
from Models.Lecturer import Lecturer
import datetime
from Models.Subject import Subject
from Models.Interval import Interval
from Models.Group import Group
from Models.Schedule import Schedule
from Manager.DatabaseManager import DatabaseManager
from extensions import db
lecturers = Blueprint('lecturers', __name__,
				template_folder='templates',
				static_folder='static')
@lecturers.route('/')
def index():
	today = datetime.date.today()
	days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
	trv = ['9:30 - 11:05','11:20 - 12:50','13:10 - 14:45','15:25 - 17:00']
	return render_template('index.html', curdate = today.strftime('%d-%m-%Y'), days = days, trvs = trv, lecturers=Lecturer.query.all(),subjects=Subject.query.all(),intervals=Interval.query.all(),groups=Group.query.all(),schedules=Schedule.query.all())

