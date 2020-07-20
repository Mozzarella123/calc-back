from models.db import db

t_ParameterFormulas = db.Table(
    'ParameterFormulas', db.metadata,
    db.Column('Parameter_Id', db.ForeignKey('Parameters.Id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    db.Column('Formula_Id', db.ForeignKey('Formulae.Id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)
