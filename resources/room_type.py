from flask_restful import Resource
from util.json import output_json
from models.RoomType import RoomType


class RoomTypeResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self):
        return RoomType.query.all()

