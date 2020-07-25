from models.db import db


class Room(db.Model):

    __tablename__ = "Rooms"

    id = db.Column(
        db.Integer,
        name="Id",
        primary_key=True,
        nullable=False
    )

    name = db.Column(
        db.Unicode,
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

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'factor': self.factor,
            'salaryFactor': self.salary_factor,
            'type': self.room_type,
            'parameters': self.parameter_values,
            'works': self.works,
            'elements': self.elements
        }
