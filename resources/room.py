from flask_restful import Resource
from flask import request, g
from models.Room import Room
from util.json import output_json
from models.db import db
from flask_expects_json import expects_json

json_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'}
    },
    'required': []
}


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

    @expects_json(json_schema)
    def put(self, room_id):
        session = db.create_scoped_session()
        room = session.query(Room).get(room_id)

        if room is None:
            return {'message': 'Room with this id not found.'}, 404

        room_json = g.data
        room.update_from_json(room_json)
        session.commit()
        session.close()

        return 'ok', 201
