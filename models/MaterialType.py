from models.db import db
from sqlalchemy.orm import relationship


class MaterialType(db.Model):
    __tablename__ = 'MaterialTypes'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    GUID = db.Column(db.String(255))
    Unit = db.Column(db.String(255))
    Formula_Id = db.Column(db.ForeignKey('Formulae.Id'), index=True)
    WorkType_Id = db.Column(db.ForeignKey('WorkTypes.Id'), index=True)

    Formula = relationship('Formula')
    WorkType = relationship('WorkType')
