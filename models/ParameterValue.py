from models.db import db
from sqlalchemy.orm import relationship
from models.Parameter import Parameter


class ParameterValue(db.Model):

    __tablename__ = "ParameterWithValues"

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

    def to_json(self):
        return {
            'id': self.id,
            'parameter': self.parameter,
            'value': self.value
        }

    def update_from_json(self, data):
        self.value = data['value']

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get('id', None),
            value=data['value'],
            parameter=Parameter.from_json(data['parameter'])
        )

    @classmethod
    def array_from_json(cls, data, prev_array=[]):
        res = []

        for idx, item in enumerate(data):
            prev_item = next((x for x in prev_array if x.id == item['id']), None)

            if prev_item is not None:
                prev_item.update_from_json(item)
            else:
                prev_item = ParameterValue.from_json(item)

            res.append(prev_item)

        return res
