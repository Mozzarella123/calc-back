from models.db import db
from sqlalchemy.orm import relationship


class Tag(db.Model):
    __tablename__ = 'Tags'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))

    WorkTypes = relationship('WorkType', secondary='TagWorkTypes')

    def to_json(self):
        return {
            'id': self.Id,
            'name': self.Name,
            'workTypes': list(map(lambda wt: wt.id, self.WorkTypes))
        }
