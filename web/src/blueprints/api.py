from flask import jsonify, Blueprint
import logging


api = Blueprint("api", __name__)
logger = logging.getLogger("app")


@api.route("/api/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})
