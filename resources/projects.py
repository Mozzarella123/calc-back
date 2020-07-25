from flask_restful import Resource
from models.MultiProject import MultiProject
from util.json import output_json


class ProjectResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self):
        return MultiProject.query.all()
