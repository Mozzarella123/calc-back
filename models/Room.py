from models.db import db
from models.ParameterValue import ParameterValue
from models.Element import Element
from models.Work import Work


class Room(db.Model):
    __tablename__ = "Rooms"

    id = db.Column(
        db.Integer,
        name="Id",
        primary_key=True,
        nullable=False
    )

    name = db.Column(
        db.String(255),
        name='Name',
        nullable=False
    )

    factor = db.Column(
        db.Integer,
        name="Factor",
        nullable=False
    )

    salary_factor = db.Column(
        db.Integer,
        name="SalaryFactor",
        nullable=False
    )

    type_id = db.Column(
        db.Integer,
        db.ForeignKey('RoomTypes.Id'),
        name='RoomType_Id',
        nullable=True
    )

    document_id = db.Column(
        db.Integer,
        db.ForeignKey('Documents.Id'),
        name='Document_Id',
        nullable=True
    )

    document = db.relationship('Document', back_populates='rooms')

    room_type = db.relationship('RoomType')

    parameter_values = db.relationship('ParameterValue', secondary='ParameterWithValueRooms')

    works = db.relationship('Work')

    elements = db.relationship('Element')

    def to_view_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'roomType': self.room_type
        }

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'factor': self.factor,
            'salaryFactor': self.salary_factor,
            'roomType': self.room_type,
            'parameters': self.parameter_values,
            'works': self.works,
            'elements': self.elements
        }

    def update_from_json(self, data):
        self.name = data['name']
        self.factor = data['factor']
        self.salary_factor = data['salaryFactor']
        self.type_id = data['roomType']
        self.works = Work.array_from_json(data['works'], self.works)
        self.elements = Element.array_from_json(data['elements'], self.elements)
        self.parameter_values = ParameterValue.array_from_json(data['parameters'], self.parameter_values)

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get('id', None),
            name=data['name'],
            factor=data['factor'],
            salary_factor=data['salaryFactor'],
            type_id=data['roomType'],
            works=list(map(Work.from_json, data['works'])),
            elements=list(map(Element.from_json, data['elements'])),
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
                prev_item = Room.from_json(item)

            res.append(prev_item)

        return res
