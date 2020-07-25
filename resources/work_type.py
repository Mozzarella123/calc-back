from flask_restful import Resource
from util.json import output_json
from models.WorkType import WorkType


class WorkTypeResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self):
        return WorkType.query.all()

