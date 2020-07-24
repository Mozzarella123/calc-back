from models.db import db

t_ElementParameterValue = db.Table(
    'ParameterWithValueElements',
    db.metadata,
    db.Column(
        'ParameterWithValue_Id',
        db.ForeignKey('ParameterWithValues.Id', ondelete='CASCADE'),
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
