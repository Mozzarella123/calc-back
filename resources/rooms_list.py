from flask_restful import Resource
from models.Document import Document
from util.json import view_output_json


class RoomsListResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': view_output_json
        }

    def get(self, document_id):
        document = Document.query.get(document_id)

        if document is None:
            return {'message': 'Document with this id not found'}, 404

        return document.rooms
