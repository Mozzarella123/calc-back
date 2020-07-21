from models.db import db
from sqlalchemy.orm import relationship


class WorkType(db.Model):
    __tablename__ = 'WorkTypes'

    Id = db.Column(db.Integer, primary_key=True)
    GUID = db.Column(db.Unicode)
    Name = db.Column(db.Unicode)
    PriceValue = db.Column(db.Float, nullable=False)
    Salary = db.Column(db.Float, nullable=False)
    Time = db.Column(db.Float, nullable=False)
    Order = db.Column(db.Integer, nullable=False)
    Description = db.Column(db.Unicode)
    MaterialsCount = db.Column(db.Unicode)
    Formula_Id = db.Column(db.ForeignKey('Formulae.Id'), index=True)

    Formula = relationship('Formula')
