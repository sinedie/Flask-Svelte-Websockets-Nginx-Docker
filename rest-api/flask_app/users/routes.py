from flask import Blueprint, jsonify
from flask_jwt_extended import fresh_jwt_required

from flask_app.database import User


users = Blueprint('users', __name__, url_prefix="/api/users")


@users.route('/', methods=['GET'])
@fresh_jwt_required
def get_users():
    users = User.query.order_by(User.username).all()
    usernames = [user.username for user in users]
    return jsonify({'msg': usernames}), 200