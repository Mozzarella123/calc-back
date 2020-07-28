from models.db import db
from models.Formula import Formula


class WorkType(db.Model):
    __tablename__ = 'WorkTypes'

    id = db.Column(
        db.Integer,
        name='Id',
        primary_key=True
    )

    guid = db.Column(
        db.String(255),
        name='GUID'
    )

    name = db.Column(
        db.String(255),
        name='Name'
    )

    price_value = db.Column(
        db.Float,
        name='PriceValue',
        nullable=False
    )

    salary = db.Column(
        db.Float,
        name='Salary',
        nullable=False
    )

    time = db.Column(
        db.Float,
        name='Time',
        nullable=False
    )

    order = db.Column(
        db.Integer,
        name='Order',
        nullable=False
    )

    description = db.Column(
        db.Text,
        name='Description'
    )

    materials_count = db.Column(
        db.Text,
        name='MaterialsCount'
    )

    formula_id = db.Column(
        db.ForeignKey('Formulae.Id'),
        name='Formula_Id',
        index=True
    )

    formula = db.relationship('Formula')

    categories = db.relationship('Category', secondary='WorkTypeCategories')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'GUID': self.guid,
            'priceValue': self.price_value,
            'salary': self.salary,
            'time': self.time,
            'order': self.order,
            'descriptions': self.description,
            'materialsCount': self.materials_count,
            'formula': self.formula,
            'categories': list(map(lambda c: {'id': c.id}, self.categories))
        }

    @classmethod
    def from_json(cls, data):
        return WorkType(
            id=data.get('id', None),
            name=data['name'],
            guid=data['GUID'],
            price_value=data['priceValue'],
            salary=data['salary'],
            time=data['time'],
            order=data['order'],
            description=data['description'],
            materials_count=data['materialsCount'],
            formula=Formula.from_json(data['formula'])
        )
