from flask_restful import Resource
from util.json import output_json
from models.ElementType import ElementType


class ElementTypeResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self):
        return ElementType.query.all()

