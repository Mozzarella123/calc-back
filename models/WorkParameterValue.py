from models.db import db

t_WorkParameterValue = db.Table(
    'WorkParameterValue',
    db.metadata,
    db.Column(
        'WorkId',
        db.ForeignKey('Works.Id', ondelete='CASCADE'),
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
