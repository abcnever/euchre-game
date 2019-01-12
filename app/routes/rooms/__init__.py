from .. import routes
from flask import render_template

@routes.route('/rooms', methods=['POST'])
def create():
    # TODO: create room logic here
    return render_template("index.html")

@routes.route('/rooms/<id>', methods=['GET'])
def fetch():
    # TODO: fetch single room logic here
    pass

@routes.route('/rooms', methods=['GET'])
def fetch():
    # TODO: fetch rooms logic here
    pass

@routes.route('/rooms/<id>', methods=['PUT'])
def update():
    # TODO: update rooms logic here
    pass

@routes.route('/rooms/<id>', methods=['DELETE'])
def update():
    # TODO: delete single room logic here
    pass
