from datetime import datetime
from dateutil.relativedelta import relativedelta

from app import db
from app import scan_models

scan_models()

# purposely break out of the context manager and leak this session so the
# operator can use it in a REPL.
session = db.session
