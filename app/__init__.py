from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # needed for cross-domain requests, allow everything by default

from app import routes