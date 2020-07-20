from models.db import db


t_WorkTypeCategories = db.Table(
    'WorkTypeCategories', db.metadata,
    db.Column('WorkType_Id', db.ForeignKey('WorkTypes.Id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    db.Column('Category_Id', db.ForeignKey('Categories.Id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)
