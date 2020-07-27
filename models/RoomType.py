from models.db import db


class RoomType(db.Model):
    __tablename__ = 'RoomTypes'

    id = db.Column(
        db.Integer,
        name='Id',
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        name='Name'
    )

    guid = db.Column(
        db.String(255),
        name='GUID'
    )

    image_path = db.Column(
        db.String(255),
        name='Image_Path',
        nullable=True
    )

    formulas = db.relationship('Formula', back_populates='room_type')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'guid': self.guid,
            'imagePath': self.image_path,
            'formulas': self.formulas
        }

    def to_view_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
    