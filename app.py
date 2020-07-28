from flask import Flask, send_from_directory
import os
import logging
from models.db import db
from resources.documents_list import DocumentsListResource
from resources.projects_list import ProjectsListResource
from resources.document import DocumentResource
from resources.work_type import WorkTypeResource
from resources.element_type import ElementTypeResource
from resources.category import CategoryResource
from resources.room_type import RoomTypeResource
from resources.tag import TagResource
from resources.rooms_list import RoomsListResource
from resources.room import RoomResource
from resources.project import ProjectResource
from routes.auth import auth_blueprint
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('default_config.py')
api_url_prefix = '/api'

db.init_app(app)

api = Api(app=app, prefix=api_url_prefix)
api.add_resource(ProjectsListResource, '/projects')
api.add_resource(ProjectResource, '/projects/<int:project_id>')
api.add_resource(DocumentsListResource, '/projects/<int:project_id>/documents')
api.add_resource(DocumentResource, '/documents/<int:document_id>')
api.add_resource(RoomsListResource, '/documents/<int:document_id>/rooms')
api.add_resource(RoomResource, '/rooms/<int:room_id>')
api.add_resource(WorkTypeResource, '/workTypes')
api.add_resource(ElementTypeResource, '/elementTypes')
api.add_resource(RoomTypeResource, '/roomTypes')
api.add_resource(CategoryResource, '/categories')
api.add_resource(TagResource, '/tags')

app.register_blueprint(auth_blueprint, url_prefix='/api')

jwt = JWTManager(app)


@app.route(api_url_prefix + '/<path:path>')
def not_found_api(path):
    return 'Not found', 404


@app.route('/assets/<path:path>', methods=['GET'])
def get_asset(path):
    return send_from_directory(app.config['ASSETS_PATH'], path)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_fe(path):
    path_dir = os.path.abspath(app.config['FE_BUILD_PATH'])

    if path != "" and os.path.exists(os.path.join(path_dir, path)):
        return send_from_directory(os.path.join(path_dir), path)
    else:
        return send_from_directory(os.path.join(path_dir), 'index.html')


with app.app_context():
    # res = db.create_scoped_session().query(Document).all()
    migrate = Migrate(app, db)


if __name__ == '__main__':
    logging.basicConfig(filename='calc.log', level=logging.DEBUG)
    app.run(host=app.config['HOST'], port=app.config['PORT'])
