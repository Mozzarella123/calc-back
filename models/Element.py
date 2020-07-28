from models.db import db
from models.ParameterValue import ParameterValue


class Element(db.Model):

    __tablename__ = "Elements"

    id = db.Column(
        db.Integer,
        name="Id",
        primary_key=True,
        nullable=False
    )

    count = db.Column(
        db.Integer,
        name="Count",
        nullable=False
    )

    element_type_id = db.Column(
        db.Integer,
        db.ForeignKey("ElementTypes.Id"),
        name="ElementType_Id",
        nullable=False
    )

    room_id = db.Column(
        db.Integer,
        db.ForeignKey("Rooms.Id"),
        name="Room_Id",
        nullable=False
    )

    type = db.relationship("ElementType")

    room = db.relationship("Room")

    parameter_values = db.relationship(
        'ParameterValue',
        secondary='ParameterWithValueElements',
        single_parent=True,
        cascade="all, delete-orphan"
    )

    def to_json(self):
        return {
            'id': self.id,
            'count': self.count,
            'elementType': self.type,
            'parameters': self.parameter_values
        }

    def update_from_json(self, data):
        self.count = data['count'],
        self.element_type_id = data['elementType'],
        self.parameter_values = ParameterValue.array_from_json(data['parameters'], self.parameter_values)

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get('id', None),
            count=data['count'],
            element_type_id=data['elementType'],
            parameter_values=list(map(ParameterValue.from_json, data['parameters']))
        )

    @classmethod
    def array_from_json(cls, data, prev_array=[]):
        res = []

        for idx, item in enumerate(data):
            prev_item = next((x for x in prev_array if x.id == item['id']), None)

            if prev_item is not None:
                prev_item.update_from_json(item)
            else:
                prev_item = Element.from_json(item)

            res.append(prev_item)

        return res
