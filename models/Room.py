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

    report_salary = db.Column(
        db.Integer,
        name="RoomReportSalary",
        nullable=True
    )

    type_id = db.Column(
        db.Integer,
        db.ForeignKey('RoomTypes.Id'),
        name='RoomType_Id',
        nullable=False
    )

    document_id = db.Column(
        db.Integer,
        db.ForeignKey('Documents.Id'),
        name='Document_Id',
        nullable=False
    )

    document = db.relationship('Document', back_populates='rooms')

    room_type = db.relationship('RoomType')

    parameter_values = db.relationship('ParameterValue', secondary='RoomParameterValue')

    works = db.relationship('Work', secondary='RoomWork')

    elements = db.relationship('Element', secondary='RoomElement')
