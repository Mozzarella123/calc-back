from flask_restful import Resource
from util.json import output_json
from models.MultiProject import MultiProject
from models.db import db


class ProjectResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self, project_id):
        project = MultiProject.query.get(project_id)

        if project is None:
            return {'message': 'Project not found'}, 404

        return MultiProject.query.get(project_id)

    def delete(self, project_id):
        session = db.create_scoped_session()
        project = session.query(MultiProject).get(project_id)

        if project is None:
            return {'message': 'Project not found'}, 404

        session.delete(project)
        session.commit()
        session.close()

        return 'ok', 200
