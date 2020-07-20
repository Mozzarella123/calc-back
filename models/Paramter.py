from models.db import db


class Parameter(db.Model):
    __tablename__ = 'Parameters'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Unicode)
    Type = db.Column(db.Integer, nullable=False)
