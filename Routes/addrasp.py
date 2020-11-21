from flask.blueprints import Blueprint
from flask import render_template
from flask import request
from Models.Subject import Subject
from Models.Interval import Interval
from Models.Group import Group
from Models.Lecturer import Lecturer
from Models.Schedule import Schedule
from Manager.DatabaseManager import DatabaseManager
from Routes.addlecturers import Lecturer
from extensions import db
import sqlalchemy.connectors
db_manager = DatabaseManager(db)
add_rasp = Blueprint('addrasp', __name__,
                 template_folder='templates',
                 static_folder='static')
@add_rasp.route('/addrasp')
def index():
    return render_template('addrasp.html', lecturers = Lecturer.query.all(), intervals=Interval.query.all(), groups = Group.query.all(), subjects = Subject.query.all())
@add_rasp.route('/addrasp',methods=['post','get'])
def add():
    if request.method == 'POST':
        days = request.form.get('day')
        weeks = request.form.get('week')
        lecturers = request.form.get('lecturer')
        intervals = request.form.get('interval')
        groups = request.form.get('group')
        subjects = request.form.get('subject')
    if lecturers and intervals and groups and subjects:
        message="Correct data"
        lecturer_id = db.session.query(Lecturer.id).filter_by(lecturer=lecturers).first()
        interval_id = db.session.query(Interval.id).filter_by(interval=intervals).first()
        group_id = db.session.query(Group.id).filter_by(groups=groups).first()
        subject_id = db.session.query(Subject.id).filter_by(subjects=subjects).first()
        db_manager.add_schedule(day=days, chetn=weeks, group_id = group_id[0], interval_id = interval_id[0], subject_id = subject_id[0], lecturer_id= lecturer_id[0])
    return render_template('addrasp.html', message=message, prob=" ",lecturers = Lecturer.query.all(), intervals=Interval.query.all(), groups = Group.query.all(), subjects = Subject.query.all())