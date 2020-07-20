from flask import Flask
from models.db import db
from routes.documents import DocumentResource
from flask_restful import Api

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('default_config.py')

db.init_app(app)

api = Api(app=app)
api.add_resource(DocumentResource, '/document')

with app.app_context():
    db.create_scoped_session().execute("SELECT * FROM  'Documents'")

if __name__ == '__main__':
    app.run()
