from extensions import db
class Lecturer(db.Model):
    __tablename__ = 'lecturer'
    id = db.Column(db.Integer, primary_key=True)
    lecturer = db.Column(db.String(30))
