from models.db import db
from enum import Enum


class RoleName(Enum):
    admin = 1
    measurer = 2
    manager = 3


class Role(db.Model):

    __tablename__ = 'role'

    id = db.Column(
        db.Integer,
        name='id',
        nullable=False,
        primary_key=True
    )

    name = db.Column(
        db.Enum(RoleName),
        name='name',
        nullable=False
    )

    @staticmethod
    def get_by_name(name):
        return Role.query.filter(Role.name == name).first()
