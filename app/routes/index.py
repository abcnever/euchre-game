from . import routes
from flask import Flask, request, jsonify, make_response, render_template

@routes.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

# HTTP Errors handlers
@routes.errorhandler(404)
def url_error(e):
    return """
    Wrong URL!
    <pre>{}</pre>""".format(e), 404

@routes.errorhandler(500)
def server_error(e):
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
