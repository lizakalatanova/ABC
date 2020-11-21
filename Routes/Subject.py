from flask.blueprints import Blueprint
from flask import render_template
from Models.Subject import Subject

subject = Blueprint('subject', __name__,
                 template_folder='templates',
                 static_folder='static')


@subject.route('/subject')
def index3():
    return render_template('index3.html', subjects=Subject.query.all())