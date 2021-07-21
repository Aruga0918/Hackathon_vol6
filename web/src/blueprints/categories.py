import logging
from flask import Blueprint, jsonify

from http import HTTPStatus

categories = Blueprint("categories", __name__)
logger = logging.getLogger("app")


@categories.route("/categories/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
