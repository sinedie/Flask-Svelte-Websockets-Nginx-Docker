from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, jwt_refresh_token_required

from flask_app.database import db, User

auth = Blueprint('auth', __name__, url_prefix="/api/auth")


# Standard login endpoint. Will return a fresh access token and
# a refresh token
@auth.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter_by(email=email).first()

    if user is not None and user.verify_password(password):
        ret = {
            'access_token': create_access_token(identity=user.id, fresh=True),
            'refresh_token': create_refresh_token(identity=user.id)
        }
        return jsonify(ret), 200

    return jsonify({"msg": "Bad email or password"}), 401


# Refresh token endpoint. This will generate a new access token from
# the refresh token, but will mark that access token as non-fresh,
# as we do not actually verify a password in this endpoint.
@auth.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user, fresh=False)
    return jsonify({'access_token': new_token}), 200


# Fresh login endpoint. This is designed to be used if we need to
# make a fresh token for a user (by verifying they have the
# correct email and password). Unlike the standard login endpoint,
# this will only return a new access token, so that we don't keep
# generating new refresh tokens, which entirely defeats their point.
@auth.route('/fresh-login', methods=['POST'])
def fresh_login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    user = User.query.filter_by(email=email).first()

    if user is not None and user.verify_password(password):
        new_token = create_access_token(identity=user.id, fresh=True)
        return jsonify({'access_token': new_token}), 200

    return jsonify({"msg": "Bad email or password"}), 401


@auth.route('/register', methods=["POST"])
def register():
    username = request.json.get('username', None)
    email    = request.json.get('email', None)
    password = request.json.get('password', None)

    # TODO check if mail already exist

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    new_user = User(username, email, password)

    db.session.add(new_user)
    db.session.commit()

    ret = {
        'access_token': create_access_token(identity=new_user.id, fresh=True),
        'refresh_token': create_refresh_token(identity=new_user.id)
    }
    return jsonify(ret), 200


@auth.route('/validate-token', methods=['GET'])
@jwt_required
def validate_token():
    current_user = get_jwt_identity()
    return jsonify({'logged_in_as': current_user}), 200