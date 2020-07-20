from models.db import db


class RoomType(db.Model):
    __tablename__ = 'RoomTypes'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Unicode)
    GUID = db.Column(db.Unicode)
    Image = db.Column(db.Binary)
    