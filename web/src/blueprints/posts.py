import logging

from http import HTTPStatus
from flask import jsonify, Blueprint

posts = Blueprint("posts", __name__)
logger = logging.getLogger("app")


@posts.route("/posts/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
