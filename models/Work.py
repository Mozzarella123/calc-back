from models.db import db


class Work(db.Model):

    __tablename__ = 'Works'

    id = db.Column(
        db.Integer,
        name='Id',
        primary_key=True,
        nullable=False
    )

    is_volume_manual = db.Column(
        db.Boolean,
        name='IsVolumeManual',
        nullable=False,
        default=False
    )

    volume = db.Column(
        db.Float,
        name='Volume',
        nullable=False
    )

    worker = db.Column(
        db.Unicode,
        name='Worker',
        nullable=True
    )

    report_salary_sum = db.Column(
        db.Float,
        name='ReportSalarySum',
        nullable=False
    )

    report_salary = db.Column(
        db.Float,
        name='ReportSalary',
        nullable=False
    )

    is_price_manual = db.Column(
        db.Boolean,
        name='IsPriceManual',
        nullable=False,
        default=False
    )

    price_value = db.Column(
        db.Float,
        name='PriceValue',
        nullable=False
    )

    work_type_id = db.Column(
        db.Integer,
        db.ForeignKey('WorkTypes.Id'),
        name='WorkType_Id',
        nullable=False
    )

    type = db.relationship('WorkType')

    parameter_values = db.relationship('ParameterValue', secondary='WorkParameterValue')
