from flask_restful import Resource
from models.Document import Document
from util.json import output_json


class DocumentResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self):
        docs = Document.query.all()
        return docs

