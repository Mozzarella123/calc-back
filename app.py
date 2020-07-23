from flask import Flask
from models.db import db
from models.Document import Document
from routes.documents import DocumentResource
from flask_restful import Api
from flask_migrate import Migrate

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('default_config.py')

db.init_app(app)

api = Api(app=app)
api.add_resource(DocumentResource, '/document')

with app.app_context():
    db.create_scoped_session().query(Document).all()
    migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()
