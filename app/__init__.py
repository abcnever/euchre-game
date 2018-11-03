from flask import Flask
from flask_cors import CORS
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app) # needed for cross-domain requests, allow everything by default

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://euchre:euchre@db:5432/euchre"

db = SQLAlchemy(app)
migrate = Migrate(app, db, directory="./app/db/migrations")

from app import routes