from models.db import db


class RoomType(db.Model):
    __tablename__ = 'RoomTypes'

    id = db.Column(
        db.Integer,
        name='Id',
        primary_key=True
    )

    name = db.Column(
        db.Unicode,
        name='Name'
    )

    guid = db.Column(
        db.Unicode,
        name='GUID'
    )

    image = db.Column(
        db.Binary,
        name='Image'
    )

    formulas = db.relationship('Formula', back_populates='room_type')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'guid': self.guid,
            'formulas': self.formulas
        }
    