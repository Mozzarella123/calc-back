from models.db import db
from enum import Enum
from util.IntEnum import IntEnum


class ParameterType(Enum):
    Default = 0
    BottomPerimeter = 1
    TopPerimetr = 2
    TopArea = 3
    BottomArea = 4
    CommonArea = 5
    WallArea = 6
    Price = 7
    ClearBottomPerimeter = 8
    ClearTopPerimeter = 9
    ClearTopArea = 10
    ClearBottomArea = 11
    ClearCommonArea = 12
    ClearWallArea = 13


class Parameter(db.Model):
    __tablename__ = 'Parameters'

    id = db.Column(
        db.Integer,
        name='Id',
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        name='Name'
    )

    type = db.Column(
        IntEnum(ParameterType),
        name='Type',
        nullable=False
    )

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': str(self.type.name)
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get('id', None),
            type=ParameterType[data['type']],
            name=data['name']
        )
