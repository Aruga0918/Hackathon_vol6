import logging
from flask import Blueprint, jsonify

from http import HTTPStatus

from models import Shop, Menu

shops = Blueprint("shops", __name__)
logger = logging.getLogger("app")


@shops.route("/shops/<int:shop_id>", methods=["GET"])
def get_shop_info(shop_id):
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
    try:
        shop_data = Shop.query.filter(Shop.id == shop_id).first()
        if shop_data is None:
            return jsonify({"message": "Shop data not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        menu_data_list = Menu.query.filter(Menu.shop_id == shop_id).all()
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    menu_list = [
        {
            "menu_id": menu_data.id,
            "name": menu_data.name,
            "price": menu_data.price
        }
        for menu_data in menu_data_list
    ]

    return_data = {
        "id": shop_data.id,
        "name": shop_data.name,
        "latitude": str(shop_data.latitude),
        "longitude": str(shop_data.longitude),
        "description": shop_data.description,
        "address": shop_data.address,
        "menu": menu_list
    }

    return jsonify(return_data), HTTPStatus.OK


@shops.route("/shops/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
