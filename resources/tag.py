from flask_restful import Resource
from util.json import output_json
from models.Tag import Tag


class TagResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self):
        return Tag.query.all()

