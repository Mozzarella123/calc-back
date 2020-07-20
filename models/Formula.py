from models.db import db
from sqlalchemy.orm import relationship


class Formula(db.Model):
    __tablename__ = 'Formulae'

    Id = db.Column(db.Integer, primary_key=True)
    Expression = db.Column(db.Unicode)
    Type = db.Column(db.Integer, nullable=False)
    ElementType_Id = db.Column(db.ForeignKey('ElementTypes.Id'), index=True)
    RoomType_Id = db.Column(db.ForeignKey('RoomTypes.Id'), index=True)

    ElementType = relationship('ElementType')
    RoomType = relationship('RoomType')
    Parameters = relationship('Parameter', secondary='ParameterFormulas')
