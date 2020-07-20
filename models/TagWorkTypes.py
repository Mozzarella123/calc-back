from models.db import db


t_TagWorkTypes = db.Table(
    'TagWorkTypes', db.metadata,
    db.Column('Tag_Id', db.ForeignKey('Tags.Id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    db.Column('WorkType_Id', db.ForeignKey('WorkTypes.Id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)
