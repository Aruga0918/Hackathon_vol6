
from models import User
import logging
from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from http import HTTPStatus


users = Blueprint("users", __name__)
logger = logging.getLogger("app")


@users.route("/users", methods=["GET"])
@jwt_required
def user_exp():
    user_id = get_jwt_identity()
    try:
        user_data = User.query.filter(User.id == user_id).first()
        if user_data is None:
            return jsonify({"message": "User data not found"}), HTTPStatus.UNAUTHORIZED

        uuid = user_data.uuid
        name = user_data.name

    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify({"name": name, "userid": uuid}), HTTPStatus.OK


@users.route("/users/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})
