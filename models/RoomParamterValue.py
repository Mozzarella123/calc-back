from models.db import db

t_RoomParameterValue = db.Table(
    'ParameterWithValueRooms',
    db.metadata,
    db.Column(
        'ParameterWithValue_Id',
        db.ForeignKey('ParameterWithValues.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True
    ),
    db.Column(
        'Room_Id',
        db.ForeignKey('Rooms.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True
    )
)
