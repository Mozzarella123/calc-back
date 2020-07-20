from models.db import db
from sqlalchemy.orm import relationship


class MaterialType(db.Model):
    __tablename__ = 'MaterialTypes'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Unicode)
    GUID = db.Column(db.Unicode)
    Unit = db.Column(db.Unicode)
    Formula_Id = db.Column(db.ForeignKey('Formula.Id'), index=True)
    WorkType_Id = db.Column(db.ForeignKey('WorkType.Id'), index=True)

    Formula = relationship('Formula')
    WorkType = relationship('WorkType')
