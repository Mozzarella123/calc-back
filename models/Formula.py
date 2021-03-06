from models.db import db
from sqlalchemy.orm import relationship
from util.IntEnum import IntEnum
from enum import Enum
from models.Parameter import Parameter


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
        db.String(1024),
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

    def to_json(self):
        return {
            'id': self.id,
            'expression': self.expression,
            'type': str(self.type.name),
            'parameters': self.parameters
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get('id', None),
            expression=data['expression'],
            type=FormulaType[data['type']],
            parameters=list(map(Parameter.from_json, data['parameters']))
        )
