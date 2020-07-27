from models.db import db
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'Categories'

    id = db.Column(
        db.Integer,
        name='Id',
        primary_key=True
    )

    order = db.Column(
        db.Integer,
        name='Order',
        nullable=False
    )

    name = db.Column(
        db.String(255),
        name='Name'
    )

    parent_id = db.Column(
        db.ForeignKey('Categories.Id'),
        name='Parent_Id',
        index=True
    )

    parent = relationship('Category', remote_side=[id])
    work_types = relationship('WorkType', secondary='WorkTypeCategories')

    def to_json(self):
        return {
            'id': self.id,
            'order': self.order,
            'name': self.name,
            'parent': {'id': self.parent_id},
            'workTypes': list(map(lambda wt: wt.id, self.work_types))
        }
