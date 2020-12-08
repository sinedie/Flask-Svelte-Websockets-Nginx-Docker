from flask import Blueprint, jsonify, request


API = Blueprint('api', __name__, url_prefix="/api")


@API.route('/say_hi', methods=["GET"])
def say_hey():
    return {'message': 'Hey from normal request'}