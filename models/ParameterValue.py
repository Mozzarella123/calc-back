from models.db import db
from sqlalchemy.orm import relationship


class ParameterValue(db.Model):

    __tablename__ = "ParameterValues"

    id = db.Column(
        db.Integer,
        name="Id",
        primary_key=True,
        nullable=False
    )

    value = db.Column(
        db.Float,
        name='Value',
        nullable=False
    )

    parameter_id = db.Column(
        db.Integer,
        db.ForeignKey("Parameters.Id"),
        nullable=False
    )

    parameter = relationship("Parameter")
