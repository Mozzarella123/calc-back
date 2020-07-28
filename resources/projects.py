from flask_restful import Resource
from flask import request
from models.MultiProject import MultiProject
from util.json import output_json
from models.db import db


class ProjectResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self):
        return MultiProject.query.all()

    def post(self):
        session = db.create_scoped_session()
        project = MultiProject.from_json(request.json)

        session.add(project)
        session.commit()

        session.refresh(project)

        return project.id
