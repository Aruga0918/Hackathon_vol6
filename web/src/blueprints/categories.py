import logging
from flask import Blueprint, jsonify

from http import HTTPStatus

categories = Blueprint("categories", __name__)
logger = logging.getLogger("app")


@categories.route("/categories", methods=["GET"])
def get_categories():
    """
    カテゴリ一覧取得API

    Parameters
    ----------

    Returns
    -------
    [
        {
            "id" : カテゴリid
            "name" : カテゴリ名
            "shop_cnt" : そのカテゴリに属する店の数
        }
    ]
    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@categories.route("/categories/<int:category_id>/shops", methods=["GET"])
def get_shops(category_id):
    """
    カテゴリからショップの一覧を取得するAPI

    Parameters
    ----------
    community_id : int, default None
        コミュニティのid．「投稿数」の取得に使用．指定がない時は全てのコミュニティでの投稿数をカウント

    Returns
    -------
    [
        {
            "id" : shop_id
            "name" : shop名
            "icon_url" : shop iconのurl
            "posted_cnt" : 投稿の数（コミュニティ単位で）
            "latitude" : 緯度
            "longitude" : 経度
            "description" : 説明
            "address" : 住所
        }
    ]
    """
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@categories.route("/categories/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
