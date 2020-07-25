from flask_restful import Resource
from util.json import output_json
from models.Category import Category


class CategoryResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self):
        return Category.query.all()

