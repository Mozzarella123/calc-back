from models.db import db


class ElementType(db.Model):
    __tablename__ = 'ElementTypes'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Unicode)
    Category = db.Column(db.Integer, nullable=False)

    
