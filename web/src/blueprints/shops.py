import logging
from flask import Blueprint, jsonify

from http import HTTPStatus

shops = Blueprint("shops", __name__)
logger = logging.getLogger("app")


@shops.route("/shops/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
