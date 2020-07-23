from models.db import db
from sqlalchemy.orm import relationship
from util.IntEnum import IntEnum
from enum import Enum


class FormulaType(Enum):
    Default = 0
    BottomPerimeter = 1
    TopPerimetr = 2
    TopArea = 3
    BottomArea = 4
    WallArea = 5


class Formula(db.Model):
    __tablename__ = 'Formulae'

    id = db.Column(
        db.Integer,
        name='Id',
        primary_key=True
    )

    expression = db.Column(
        db.Unicode,
        name='Expression'
    )

    type = db.Column(
        IntEnum(FormulaType),
        name='Type',
        nullable=False
    )

    element_type_id = db.Column(
        db.ForeignKey('ElementTypes.Id'),
        name='ElementType_Id',
        index=True
    )

    room_type_id = db.Column(
        db.ForeignKey('RoomTypes.Id'),
        name='RoomType_Id',
        index=True
    )

    element_type = relationship('ElementType')
    room_type = relationship('RoomType', back_populates='formulas')
    parameters = relationship('Parameter', secondary='ParameterFormulas')
