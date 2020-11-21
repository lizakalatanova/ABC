from flask.blueprints import Blueprint
from flask import render_template
from flask import request
from Models.Lecturer import Lecturer
from Manager.DatabaseManager import DatabaseManager
from extensions import db
db_manager = DatabaseManager(db)

add_lecturers = Blueprint('addlecturers', __name__,
                 template_folder='templates',
                 static_folder='static')


@add_lecturers.route('/addlecturers')
def index():
    return render_template('addlecturer.html')
@add_lecturers.route('/addlecturers',methods=['post','get'])
def add():
    if request.method == 'POST':
        lecturer=request.form.get('lecturer')
    if lecturer:
        db_manager.add_lecturer(lecturer=lecturer)
    return  render_template('addlecturer.html')
