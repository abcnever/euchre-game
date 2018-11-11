from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

__all__ = ["cards", "rooms", "teams"]
