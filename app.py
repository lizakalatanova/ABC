from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from Routes.addlecturers import add_lecturers
from Routes.Group import group
from Routes.Interval import interval
from Routes.Subject import subject
from Routes.addrasp import add_rasp
from Routes.Lecturers import lecturers
app = Flask (__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.register_blueprint(add_lecturers)
app.register_blueprint(lecturers)
app.register_blueprint(group)
app.register_blueprint(add_rasp)
if __name__ == '__main__':
   app.run()
