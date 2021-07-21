import logging
from flask import jsonify, Blueprint

from http import HTTPStatus

rankings = Blueprint("rankings", __name__)
logger = logging.getLogger("app")


@rankings.route("/rankings/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
