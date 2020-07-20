from models.db import db
from sqlalchemy.orm import relationship


class Tag(db.Model):
    __tablename__ = 'Tags'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Unicode)

    WorkTypes = relationship('WorkType', secondary='TagWorkTypes')
