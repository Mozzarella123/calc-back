from models.db import db

t_RoomParameterValue = db.Table(
    'RoomParameterValue',
    db.metadata,
    db.Column(
        'RoomId',
        db.ForeignKey('Rooms.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True
    ),
    db.Column(
        'ParameterValueId',
        db.ForeignKey('ParameterValues.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True
    )
)
