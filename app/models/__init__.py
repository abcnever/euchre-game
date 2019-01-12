from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

__all__ = ["cardhandjoins", "cards", "hands", "plays", "rooms", "rounds", "teams", "tricks", "users", "userteamjoins"]
