from models.db import db


class MultiProject(db.Model):
    __tablename__ = 'MultiProjects'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Unicode)
