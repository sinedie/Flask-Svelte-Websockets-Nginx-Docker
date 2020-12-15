from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, fresh_jwt_required


api = Blueprint('api', __name__, url_prefix="/api")


@api.route('/', methods=["GET"])
def healt_check():
    return jsonify({'msg': 'Server is healty'}), 200


@api.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify({'logged_in_as': current_user}), 200


@api.route('/protected-fresh', methods=['GET'])
@fresh_jwt_required
def protected_fresh():
    username = get_jwt_identity()
    return jsonify({'fresh_logged_in_as': username}), 200