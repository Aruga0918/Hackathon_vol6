import logging

from http import HTTPStatus
from flask import jsonify, Blueprint

from flask_jwt_extended import jwt_required

posts = Blueprint("posts", __name__)
logger = logging.getLogger("app")


@posts.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    """
    投稿取得API

    Parameters
    ----------

    Returns
    -------
    [
        {
            "user_name" : ユーザーの名前,
            "user_id" : (数字の方の)ユーザーid,
            "uid" : (文字列の方の)ユーザーid,
            "user_icon_url" : ユーザーiconのurl
            "shop_id" : ショップのid,
            "shop_name" : ショッピの名前
            "shop_icon_url" : ショップiconのurl
            "message" : 投稿のコメント,
            "menu" : メニューのリスト [
                {
                    "menu_id" : menuのid
                    "name": メニューの名前
                    "price" : 価格
                }
                ...
            ],
            "created_at" : 投稿時間
        }
        ...
    ]
    """
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@posts.route("/posts/users/<int:user_id>", methods=["GET"])
def get_user_posts(user_id):
    """
    ユーザー投稿取得API

    Parameters
    ----------

    Returns
    -------
    [
        {
            "user_name" : ユーザーの名前,
            "user_id" : (数字の方の)ユーザーid,
            "uid" : (文字列の方の)ユーザーid,
            "user_icon_url" : ユーザーiconのurl
            "shop_id" : ショップのid,
            "shop_name" : ショッピの名前
            "shop_icon_url" : ショップiconのurl
            "message" : 投稿のコメント,
            "menu" : メニューのリスト [
                {
                    "menu_id" : menuのid
                    "name": メニューの名前
                    "price" : 価格
                }
                ...
            ],
            "created_at" : 投稿時間
        }
        ...
    ]
    """
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@posts.route("/posts/shops/<int:shop_id>", methods=["GET"])
def get_shop_posts(shop_id):
    """
    ショップ投稿取得API

    Parameters
    ----------

    Returns
    -------
    [
        {
            "user_name" : ユーザーの名前,
            "user_id" : (数字の方の)ユーザーid,
            "uid" : (文字列の方の)ユーザーid,
            "user_icon_url" : ユーザーiconのurl
            "shop_id" : ショップのid,
            "shop_name" : ショッピの名前
            "shop_icon_url" : ショップiconのurl
            "message" : 投稿のコメント,
            "menu" : メニューのリスト [
                {
                    "menu_id" : menuのid
                    "name": メニューの名前
                    "price" : 価格
                }
                ...
            ],
            "created_at" : 投稿時間
        }
        ...
    ]
    """
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@posts.route("/posts/communities/<int:community_id>", methods=["GET"])
@jwt_required
def get_community_posts(community_id):
    """
    コミュニティ投稿取得API

    Parameters
    ----------

    Returns
    -------
    [
        {
            "user_name" : ユーザーの名前,
            "user_id" : (数字の方の)ユーザーid,
            "uid" : (文字列の方の)ユーザーid,
            "user_icon_url" : ユーザーiconのurl
            "shop_id" : ショップのid,
            "shop_name" : ショッピの名前
            "shop_icon_url" : ショップiconのurl
            "message" : 投稿のコメント,
            "menu" : メニューのリスト [
                {
                    "menu_id" : menuのid
                    "name": メニューの名前
                    "price" : 価格
                }
                ...
            ],
            "created_at" : 投稿時間
        }
        ...
    ]
    """
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@posts.route("/posts/users/<int:user_id>/shops/<int:shop_id>", methods=["POST"])
@jwt_required
def post(user_id, shop_id):
    """
    投稿を作成するAPI

    Parameters
    ----------
    menus : List[int]
        メニューidのリスト
    message : str
        投稿コメント

    Returns
    -------
    """
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@posts.route("/posts/<int:post_id>", methods=["PATCH"])
@jwt_required
def edit_post(post_id):
    """
    投稿を編集するAPI

    Parameters
    ----------
    menus : List[int]
        メニューidのリスト
    message : str
        投稿コメント

    Returns
    -------
    """
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@posts.route("/posts/<int:post_id>", methods=["DELETE"])
@jwt_required
def delete_post(post_id):
    """
    投稿を削除するAPI

    Parameters
    ----------

    Returns
    -------
    """
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@posts.route("/posts/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
