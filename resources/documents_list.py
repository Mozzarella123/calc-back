from flask_restful import Resource
from flask import request
from models.MultiProject import MultiProject
from util.json import view_output_json
from models.db import db
from models.Document import Document


class DocumentsListResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': view_output_json
        }

    def get(self, project_id):
        project = MultiProject.query.get(project_id)

        if project is None:
            return {'message': 'Project with this id not found.'}, 404

        return project.documents

    def post(self, project_id):
        session = db.create_scoped_session()
        project = session.query(MultiProject).get(project_id)

        if project is None:
            return {'message': 'Project with this id not found.'}, 404

        document = Document.from_json(request.json)
        document.project_id = project_id
        session.add(document)
        session.commit()

        session.refresh(document)

        return document.id
