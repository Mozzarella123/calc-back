from models.db import db
from models.WorkType import WorkType


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

    parent = db.relationship('Category', remote_side=[id])
    work_types = db.relationship('WorkType', secondary='WorkTypeCategories')

    def to_json(self):
        return {
            'id': self.id,
            'order': self.order,
            'name': self.name,
            'parent': {'id': self.parent_id} if self.parent_id is not None else None,
            'workTypes': list(map(lambda wt: wt.id, self.work_types))
        }

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get('id', None),
            order=data['order'],
            name=data['name'],
            parent_id=data['parent'],
            work_types=WorkType.query.filter(WorkType.id in data['workTypes'])
        )
