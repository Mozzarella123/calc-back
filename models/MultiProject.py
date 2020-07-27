from models.db import db


class MultiProject(db.Model):
    __tablename__ = 'MultiProjects'

    id = db.Column(
        db.Integer,
        name='Id',
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        name='Name'
    )

    documents = db.relationship('Document')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
