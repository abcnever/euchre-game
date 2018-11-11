from flask import Flask
from flask_cors import CORS
import os
from flask_migrate import Migrate
from app.models import db
from app.models import * # NOQA

app = Flask(__name__)
CORS(app)  # needed for cross-domain requests, allow everything by default

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db, directory="app/db/migrations")
