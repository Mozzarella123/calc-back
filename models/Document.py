from datetime import datetime
from models.db import db
from sqlalchemy.orm import relationship
from models.Room import Room
from models.RoomType import RoomType


class Document(db.Model):

    __tablename__ = "Documents"

    id = db.Column(
        db.Integer,
        primary_key=True,
        name="Id",
        nullable=False
    )

    name = db.Column(
        db.String(255),
        name="Name",
        nullable=False
    )

    type = db.Column(
        db.Integer,
        name="DocumentType",
        nullable=False
    )

    date_created = db.Column(
        db.DateTime,
        name="DateCreated",
        nullable=False,
        default=datetime.now()
    )

    date_modified = db.Column(
        db.DateTime,
        name="DateModified",
        nullable=False,
        default=datetime.now()
    )

    project_id = db.Column(
        db.ForeignKey('MultiProjects.Id'),
        name='MultiProject_Id',
        index=True
    )

    rooms = db.relationship(Room, back_populates='document')

    project = relationship('MultiProject')

    def to_view_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'dateCreated': str(self.date_created),
            'dateModified': str(self.date_modified)
        }

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'documentType': self.type,
            'dateCreated': str(self.date_created),
            'dateModified': str(self.date_modified),
            'rooms': self.rooms
        }

    def update_from_json(self, data):
        self.name = data['name']
        self.type = data['documentType']
        self.date_modified = datetime.now()
        self.rooms = Room.array_from_json(data['rooms'], self.rooms)

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            type=data['documentType'],
            rooms=list(map(Room.from_json, data['rooms']))
        )
