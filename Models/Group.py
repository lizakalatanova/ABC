from extensions import db
class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    groups = db.Column(db.String(30), unique=True, nullable=False)