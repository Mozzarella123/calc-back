from flask_restful import Resource
from util.json import output_json
from models.Document import Document
from models.db import db
from flask import request


class DocumentResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self, document_id):
        return Document.query.get(document_id)

    def put(self, document_id):
        session = db.create_scoped_session()
        document = session.query(Document).get(document_id)

        if document is None:
            return {'message': 'Document not found'}, 404

        document.update_from_json(request.json)
        session.commit()
        session.close()

        return 'ok', 201

    def delete(self, document_id):
        session = db.create_scoped_session()
        document = session.query(Document).get(document_id)

        if document is None:
            return {'message': 'Document not found'}, 404

        session.delete(document)
        session.commit()
        session.close()

        return 'ok', 200
