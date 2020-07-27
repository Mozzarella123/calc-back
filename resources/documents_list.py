from flask_restful import Resource
from models.MultiProject import MultiProject
from util.json import view_output_json


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

