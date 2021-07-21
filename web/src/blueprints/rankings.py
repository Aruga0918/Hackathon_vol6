import logging
from flask import jsonify, Blueprint

from http import HTTPStatus

rankings = Blueprint("rankings", __name__)
logger = logging.getLogger("app")


@rankings.route("/rankings/shops/<int:shop_id>", methods=["GET"])
def get_rankings(shop_id):
    """
    ランキング取得API

    Parameters
    ----------
    n_cnt : int, default 3
        returnの数
    community_id : int. default None
        コミュニティid.　指定がない時は全投稿を用いたランキングを作成

    Returns
    -------
    [
        {
            "menu_id" : メニューid
            "name" : メニュー名
            "price" : 価格
            "posted_cnt" : 食べた人の数
        }
        ...
    ]

    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@rankings.route("/rankings/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
