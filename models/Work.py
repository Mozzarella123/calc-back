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

    room_id = db.Column(
        db.Integer,
        db.ForeignKey('Rooms.Id'),
        name='ParentRoom_Id',
        nullable=False
    )

    type = db.relationship('WorkType')

    parameter_values = db.relationship('ParameterValue', secondary='WorkParameterWithValues')

    room = db.relationship('Room')

    def to_json(self):
        return {
            'id': self.id,
            'isVolumeManual': self.is_volume_manual,
            'volume': self.volume,
            'worker': self.worker,
            'priceValue': self.price_value,
            'parameters': self.parameter_values,
            'workType': self.type
        }
