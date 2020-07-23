from models.db import db

t_RoomElement = db.Table(
    'RoomElement',
    db.metadata,
    db.Column(
        'Room_Id',
        db.ForeignKey('Rooms.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True
    ),
    db.Column(
        'Element_Id',
        db.ForeignKey('Elements.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True
    )
)
