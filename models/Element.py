from models.db import db
from sqlalchemy.orm import relationship


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

    type = relationship("ElementType")

    room = relationship("Room")

    parameter_values = relationship('ParameterValue', secondary='ParameterWithValueElements')

    def to_json(self):
        return {
            'id': self.id,
            'count': self.count,
            'elementType': self.type,
            'parameters': self.parameter_values
        }
