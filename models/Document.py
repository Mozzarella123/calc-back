from datetime import datetime
from models.db import db
from sqlalchemy.orm import relationship


class Document(db.Model):

    __tablename__ = "Documents"

    id = db.Column(
        db.Integer,
        primary_key=True,
        name="Id",
        nullable=False
    )

    name = db.Column(
        db.Unicode,
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

    MultiProject_Id = db.Column(
        db.ForeignKey('MultiProjects.Id'),
        index=True
    )

    rooms = db.relationship('Room', back_populates='document')

    MultiProject = relationship('MultiProject')

    def to_view_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'dateCreated': str(self.date_created),
            'dateModified': str(self.date_modified),
            'rooms': self.rooms
        }
