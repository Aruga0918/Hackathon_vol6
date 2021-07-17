from database import db
from models import User, Template
import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from http import HTTPStatus


template = Blueprint("template", __name__)
logger = logging.getLogger("app")


@template.route("/template", methods=["GET"])
def get_template():
    try:
        template = Template.query.all()
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error:\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify([temp.to_dict() for temp in template]), HTTPStatus.OK


@template.route("/template", methods=["POST"])
@jwt_required
def post_template():
    try:
        payload = request.json
        description = payload.get("description")
        if description is None:
            raise ValueError("description is None")
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Bad request error"}), HTTPStatus.BAD_REQUEST

    user_id = get_jwt_identity()
    try:
        user_data = User.query.filter(User.id == user_id).first()
        if user_data is None:
            return jsonify({"message": "User data not found"}), HTTPStatus.UNAUTHORIZED
        user_id = user_data.id
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        template = Template(user_id, description)
        db.session.add(template)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify(template.to_dict()), HTTPStatus.OK


@template.route("/template/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})
