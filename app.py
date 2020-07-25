from flask import Flask, Blueprint
from models.db import db
from resources.documents_list import DocumentsListResource
from resources.projects import ProjectResource
from resources.document import DocumentResource
from resources.work_type import WorkTypeResource
from resources.element_type import ElementTypeResource
from resources.category import CategoryResource
from resources.room_type import RoomTypeResource
from resources.tag import TagResource
from routes.auth import auth_blueprint
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('default_config.py')

db.init_app(app)

api = Api(app=app, prefix='/api')
api.add_resource(DocumentsListResource, '/projects/<int:project_id>/documents')
api.add_resource(ProjectResource, '/projects')
api.add_resource(DocumentResource, '/documents/<int:document_id>')
api.add_resource(WorkTypeResource, '/workTypes')
api.add_resource(ElementTypeResource, '/elementTypes')
api.add_resource(RoomTypeResource, '/roomTypes')
api.add_resource(CategoryResource, '/categories')
api.add_resource(TagResource, '/tags')

app.register_blueprint(auth_blueprint, url_prefix='/api')

jwt = JWTManager(app)

with app.app_context():
    # res = db.create_scoped_session().query(Document).all()
    migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])
