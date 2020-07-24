from flask_restful import Resource
from models.Document import Document
from util.json import view_output_json


class DocumentsListResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': view_output_json
        }

    def get(self, project_id):
        return Document.query.filter(Document.MultiProject_Id == project_id).all()

