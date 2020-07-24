from models.db import db

t_WorkParameterValue = db.Table(
    'WorkParameterWithValues',
    db.metadata,
    db.Column(
        'Work_Id',
        db.ForeignKey('Works.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True
    ),
    db.Column(
        'ParameterWithValue_Id',
        db.ForeignKey('ParameterWithValues.Id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        index=True
    )
)
