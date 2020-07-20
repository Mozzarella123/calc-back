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

    json = db.Column(
        db.Unicode,
        name="Json",
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

    MultiProject = relationship('MultiProject')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
