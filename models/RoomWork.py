from models.db import db

t_RoomWork = db.Table(
    'RoomWork',
    db.metadata,
    db.Column(
        'Room_Id',
        db.ForeignKey('Rooms.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True
    ),
    db.Column(
        'Work_Id',
        db.ForeignKey('Works.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True
    )
)
