from flask import Flask, Blueprint
from models.db import db
from models.Document import Document
from routes.documents_list import DocumentsListResource
from routes.projects import ProjectResource
from routes.document import DocumentResource
from flask_restful import Api
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('default_config.py')

db.init_app(app)

# api_bp = Blueprint('api', __name__)
api = Api(app=app, prefix='/api')
api.add_resource(DocumentsListResource, '/projects/<int:project_id>/documents')
api.add_resource(ProjectResource, '/projects')
api.add_resource(DocumentResource, '/documents/<int:document_id>')

with app.app_context():
    # res = db.create_scoped_session().query(Document).all()
    migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
