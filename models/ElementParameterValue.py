from models.db import db

t_ElementParameterValue = db.Table(
    'ElementParameterValue',
    db.metadata,
    db.Column(
        'ElementId',
        db.ForeignKey('Elements.Id', ondelete='CASCADE'),
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
