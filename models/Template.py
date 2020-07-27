from models.db import db


class Template(db.Model):
    __tablename__ = 'Templates'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Content = db.Column(db.Text)
