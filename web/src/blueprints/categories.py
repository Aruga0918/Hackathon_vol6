import logging
from flask import Blueprint, jsonify, request

from http import HTTPStatus

from models import Category, Shop, ShopCategory, Post, CommunityUser

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
    try:
        category_data_list = Category.query.all()
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return_data = []
    for category_data in category_data_list:
        try:
            shop_cnt = ShopCategory.query.filter(ShopCategory.category_id == category_data.id).count()
        except Exception as e:
            logger.error(e)
            return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR
        
        return_data.append(
            {
                "id": category_data.id,
                "name": category_data.name,
                "shop_cnt": shop_cnt
            }
        )

    return jsonify(return_data), HTTPStatus.OK


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
    payload = request.json
    community_id = payload.get("community_id")

    try:
        category_data = Category.query.filter(Category.id == category_id).first()
        if category_data is None:
            return jsonify({"message": "Category data not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        shop_category_data_list = ShopCategory.query.filter(ShopCategory.category_id == category_id).all()
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return_data = []
    for shop_category_data in shop_category_data_list:
        try:
            shop_data = Shop.query.filter(Shop.id == shop_category_data.shop_id).first()
            if shop_data is None:
                return jsonify({"message": "Shop data not found"}), HTTPStatus.BAD_REQUEST
        except Exception as e:
            logger.error(e)
            return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

        if community_id is None:
            try:
                posted_cnt = Post.query.filter(Post.shop_id == shop_data.id).count()
            except Exception as e:
                logger.error(e)
                return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR
        else:
            try:
                community_user_data_list = CommunityUser.query.filter(CommunityUser.community_id == community_id).all()
            except Exception as e:
                logger.error(e)
                return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

            user_id_list = [community_user_data.user_id for community_user_data in community_user_data_list]
            try:
                posted_cnt = Post.query.filter(Post.shop_id == shop_data.id, Post.user_id.in_(user_id_list)).count()
            except Exception as e:
                logger.error(e)
                return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

        return_data.append(
            {
                "id": shop_data.id,
                "name": shop_data.name,
                "icon_url": shop_data.icon_url,
                "posted_cnt": posted_cnt,
                "latitude": str(shop_data.latitude),
                "longitude": str(shop_data.longitude),
                "description": shop_data.description,
                "address": shop_data.address
            }
        )

    return jsonify(return_data), HTTPStatus.OK


@categories.route("/categories/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
