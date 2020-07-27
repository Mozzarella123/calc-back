from flask_restful import Resource
from models.Room import Room
from util.json import output_json


class RoomResource(Resource):

    def __init__(self):
        self.representations = {
            'application/json': output_json
        }

    def get(self, room_id):
        room = Room.query.get(room_id)

        if room is None:
            return {'message': 'Room with this id not found.'}, 404

        return room
