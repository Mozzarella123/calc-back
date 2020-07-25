from models.db import db
from flask_bcrypt import Bcrypt
from flask import current_app


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(
        db.Integer,
        name='id',
        primary_key=True,
        nullable=False
    )

    name = db.Column(
        db.String(100),
        name='name',
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(100),
        name='email',
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.String(100),
        name='password',
        nullable=False
    )

    roles = db.relationship(
        "Role",
        secondary='user_role',
        backref=db.backref('user'),
        single_parent=True
    )

    def set_password(self, password):
        """Set password."""
        bcrypt = Bcrypt(current_app)
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        bcrypt = Bcrypt(current_app)
        return bcrypt.check_password_hash(self.password, value)
