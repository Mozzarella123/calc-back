from models.db import db


class ElementType(db.Model):
    __tablename__ = 'ElementTypes'

    id = db.Column(
        db.Integer,
        name='Id',
        primary_key=True
    )

    name = db.Column(
        db.Unicode,
        name='Name'
    )

    category = db.Column(
        db.Integer,
        db.ForeignKey('Categories.Id'),
        name='Category',
        nullable=False
    )

    formula = db.relationship('Formula')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'formula': self.formula
        }

    
