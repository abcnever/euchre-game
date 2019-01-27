from flask import Flask
from flask_cors import CORS
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.routes import routes

import importlib

MODEL_DIRS = [
    'models',
]
MODEL_EXCLUDE_FILES = [
    '__init__.py',
]

def scan_models():
    for dirpath, dirnames, filenames in os.walk('./app/'):
        head, tail = os.path.split(dirpath)
        if tail in MODEL_DIRS:
            # there should be models
            for filename in filenames:
                if filename.endswith('.py') and \
                        filename not in MODEL_EXCLUDE_FILES:
                    # lets import the module
                    filename_no_ext, _ = os.path.splitext(
                        os.path.join(
                            dirpath, filename
                        )
                    )
                    # remove first . character
                    filename_no_ext = filename_no_ext[2:]
                    module_path = filename_no_ext.replace(os.sep, '.')
                    importlib.import_module(module_path)

app = Flask(__name__)
CORS(app)  # needed for cross-domain requests, allow everything by default

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "gjr39dkjn344_!67#"

# database setups
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory="./app/db/migrations")

# blueprint setups
app.register_blueprint(routes)

scan_models()

if __name__ == "__main__":
    app.run(extra_files=['./app/routes/*', './app/templates/*', './app/models/*'])
