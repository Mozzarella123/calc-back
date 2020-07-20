from models.db import db
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'Categories'

    Id = db.Column(db.Integer, primary_key=True)
    Order = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.Unicode)
    Parent_Id = db.Column(db.ForeignKey('Categories.Id'), index=True)

    parent = relationship('Category', remote_side=[Id])
    WorkTypes = relationship('WorkType', secondary='WorkTypeCategories')
