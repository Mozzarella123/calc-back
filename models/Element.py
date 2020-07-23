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

    type = relationship("ElementType")

    parameter_values = relationship('ParameterValue', secondary='ElementParameterValue')
