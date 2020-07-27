from models.db import db
from sqlalchemy.orm import relationship


class TemplateBlock(db.Model):
    __tablename__ = 'TemplateBlocks'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Content = db.Column(db.Text)
    Order = db.Column(db.Integer, nullable=False)
    TemplateBlockType = db.Column(db.Integer, nullable=False)
    Template_Id = db.Column(db.ForeignKey('Templates.Id'), index=True)

    Template = relationship('Template')
