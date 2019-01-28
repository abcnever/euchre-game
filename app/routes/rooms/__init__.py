from .. import routes
from app import db
from app.models.rooms import Room
from flask import render_template


@routes.route("/rooms", methods=["POST"])
def create():
    room = Room()
    db.session.add(room)
    db.session.commit()
    return render_template("index.html", room=room)


@routes.route("/rooms/<id>", methods=["GET"])
def fetch(room_id):
    room = Room.query.get(room_id)
    # do some stuff?
    return render_template("index.html", room=room)


@routes.route("/rooms/<id>", methods=["PUT"])
def update(room_id):
    room = Room.query.get(room_id)
    # stuff
    return render_template("index.html", room=room)


@routes.route("/rooms/<id>", methods=["DELETE"])
def delete(room_id):
    db.session.delete(Room.query.get(room_id))
    db.session.commit()
    return render_template("index.html")
