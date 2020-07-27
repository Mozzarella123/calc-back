from models.db import db
from sqlalchemy.orm import relationship


class WorkType(db.Model):
    __tablename__ = 'WorkTypes'

    id = db.Column(
        db.Integer,
        name='Id',
        primary_key=True
    )

    guid = db.Column(
        db.Unicode,
        name='GUID'
    )

    name = db.Column(
        db.Unicode,
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
        db.Unicode,
        name='Description'
    )

    materials_count = db.Column(
        db.Unicode,
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
            'categories': list(map(lambda c: c.id, self.categories))
        }


