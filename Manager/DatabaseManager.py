from Models.Lecturer import Lecturer
from Models.Group import Group
from Models.Interval import Interval
from Models.Subject import Subject
from Models.Schedule import Schedule
class DatabaseManager:
    def __init__(self, db):
        self.db = db

    def add_lecturer(self, **kwargs):
        lecturer = Lecturer(lecturer=kwargs["lecturer"])
        self.db.session.add(lecturer)
        self.db.session.commit()

    def add_group(self, **kwargs):
        group = Group(groups=kwargs["groups"])
        self.db.session.add(group)
        self.db.session.commit()

    def add_interval(self, **kwargs):
        interval = Interval(interval=kwargs["interval"])
        self.db.session.add(interval)
        self.db.session.commit()

    def add_subject(self, **kwargs):
        subject = Subject(subjects=kwargs["subjects"])
        self.db.session.add(subject)
        self.db.session.commit()

    def add_schedule(self, **kwargs):
        schedule = Schedule(day=kwargs["day"],
                            chetn=kwargs["chetn"],
                            group_id = kwargs["group_id"],
                            interval_id = kwargs["interval_id"],
                            subject_id = kwargs["subject_id"] ,
                            lecturer_id= kwargs["lecturer_id"]
                            )
        self.db.session.add(schedule)
        self.db.session.commit()