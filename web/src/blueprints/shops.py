import logging
from flask import Blueprint, jsonify

from http import HTTPStatus

shops = Blueprint("shops", __name__)
logger = logging.getLogger("app")


@shops.route("/shops/<int:shop_id>", methods=["GET"])
def get_user_info(user_id):
    """
    店舗情報取得API

    Parameters
    ----------

    Returns
    -------
    {
        "id" : shop_id
        "name" : shop名
        "latitude" : 緯度
        "longitude" : 経度
        "description" : 説明
        "address" : 住所
        "menu" : メニューのリスト [
            {
                "menu_id" : menuのid
                "name": メニューの名前
                "price" : 価格
            }
            ...
        ],
    }
    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@shops.route("/shops/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
