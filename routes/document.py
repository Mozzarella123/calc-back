from flask_restful import Resource
from util.json import output_json
from models.Document import Document


class DocumentResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self, document_id):
        return Document.query.get(document_id)

