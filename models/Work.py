from models.db import db
from models.ParameterValue import ParameterValue


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
        db.String(255),
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

    def update_from_json(self, data):
        self.is_volume_manual = data['isVolumeManual']
        self.volume = data['volume']
        self.worker = data['worker']
        self.price_value = data['priceValue']
        self.parameter_values = ParameterValue.array_from_json(data['parameters'], self.parameter_values)
        self.work_type_id = data['workType']

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get('id', None),
            is_volume_manual=data['isVolumeManual'],
            volume=data['volume'],
            worker=data['worker'],
            price_value=data['priceValue'],
            parameter_values=list(map(ParameterValue.from_json, data['parameters'])),
            work_type_id=data['workType']
        )

    @classmethod
    def array_from_json(cls, data, prev_array=[]):
        res = []

        for idx, item in enumerate(data):
            prev_item = next((x for x in prev_array if x.id == item['id']), None)

            if prev_item is not None:
                prev_item.update_from_json(item)
            else:
                prev_item = Work.from_json(item)

            res.append(prev_item)

        return res
