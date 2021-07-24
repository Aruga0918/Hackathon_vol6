import logging
from http import HTTPStatus
from flask import jsonify, request, Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from database import db
from models import User, CommunityUser, Menu, PostMenu, Post, Shop

posts = Blueprint("posts", __name__)
logger = logging.getLogger("app")


class DatabaseError(Exception):
    """データベースからの情報取得に失敗したときに投げる例外の基底クラス"""
    pass


class PostNotFoundError(DatabaseError):
    """投稿が存在しなかったときに投げる例外"""

    def __init__(self):
        self.message = jsonify({"message": "Post data not found"})


class UserNotFoundError(DatabaseError):
    """ユーザーが存在しなかったときに投げる例外"""

    def __init__(self):
        self.message = jsonify({"message": "User data not found"})


class ShopNotFoundError(DatabaseError):
    """ショップが存在しなかったときに投げる例外"""

    def __init__(self):
        self.message = jsonify({"message": "Shop data not found"})


class MenuNotFoundError(DatabaseError):
    """メニューが存在しなかったときに投げる例外"""

    def __init__(self):
        self.message = jsonify({"message": "Menu data not found"})


def get_post_detailed_info(post_id):
    """
    投稿の詳細を取得する関数

    Parameters
    ----------
    post_id : int
        投稿id

    Returns
    -------
    {
        "post_id" : 投稿id,
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
    """
    try:
        post_data = Post.query.filter(Post.id == post_id).first()
        if post_data is None:
            raise PostNotFoundError
    except Exception as e:
        raise e

    try:
        post_menu_data = PostMenu.query.filter(PostMenu.post_id == post_id).all()
    except Exception as e:
        raise e

    user_id = post_data.user_id
    shop_id = post_data.shop_id
    menu_ids = [data.menu_id for data in post_menu_data]

    try:
        user_data = User.query.filter(User.id == user_id).first()
        if user_data is None:
            raise UserNotFoundError
    except Exception as e:
        raise e

    try:
        shop_data = Shop.query.filter(Shop.id == shop_id).first()
        if shop_data is None:
            raise ShopNotFoundError
    except Exception as e:
        raise e

    menu_data_list = []
    for menu_id in menu_ids:
        try:
            menu_data = Menu.query.filter(Menu.id == menu_id).first()
            if menu_data is None:
                raise MenuNotFoundError
            menu_data_list.append(menu_data)
        except Exception as e:
            raise e

    menu_list = [
        {
            "menu_id": menu_data.id,
            "name": menu_data.name,
            "price": menu_data.price
        }
        for menu_data in menu_data_list
    ]

    post_detailed_info = {
        "post_id": post_id,
        "user_name": user_data.name,
        "user_id": user_data.id,
        "uid": user_data.uid,
        "user_icon_url": user_data.icon_url,
        "shop_id": shop_data.id,
        "shop_name": shop_data.name,
        "shop_icon_url": shop_data.icon_url,
        "message": post_data.message,
        "menu": menu_list,
        "created_at": post_data.created_at
    }

    return post_detailed_info


@posts.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    """
    投稿取得API

    Parameters
    ----------

    Returns
    -------
    {
        "post_id" : 投稿id,
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
    """
    try:
        return_data = get_post_detailed_info(post_id)
    except DatabaseError as e:
        return e.message, HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify(return_data), HTTPStatus.OK


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
            "post_id" : 投稿id,
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
    try:
        post_data_list = Post.query.filter(Post.user_id == user_id).all()
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        return_data = [get_post_detailed_info(post_data.id)
                       for post_data in post_data_list]
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify(return_data), HTTPStatus.OK


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
            "post_id" : 投稿id,
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
    try:
        post_data_list = Post.query.filter(Post.shop_id == shop_id).all()
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        return_data = [get_post_detailed_info(post_data.id)
                       for post_data in post_data_list]
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify(return_data), HTTPStatus.OK


@posts.route("/posts/communities/<int:community_id>", methods=["GET"])
def get_community_posts(community_id):
    """
    コミュニティ投稿取得API

    Parameters
    ----------

    Returns
    -------
    [
        {
            "post_id" : 投稿id,
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
    if community_id == 0:
        try:
            community_user_data_list = CommunityUser.query.all()
            if not community_user_data_list:
                return jsonify({"message": "Community data not found"}), HTTPStatus.BAD_REQUEST
        except Exception as e:
            logger.error(e)
            return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        try:
            community_user_data_list = CommunityUser.query.filter(
                CommunityUser.community_id == community_id).all()
            if not community_user_data_list:
                return jsonify({"message": "Community data not found"}), HTTPStatus.BAD_REQUEST
        except Exception as e:
            logger.error(e)
            return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    if community_id == 0:
        try:
            community_user_data = CommunityUser.query.first()
            if community_user_data is None:
                return jsonify({"message": "Unauthorized"}), HTTPStatus.UNAUTHORIZED
        except Exception as e:
            logger.error(e)
            return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        user_id = get_jwt_identity()
        try:
            community_user_data = CommunityUser.query.filter(
                CommunityUser.user_id == user_id,
                CommunityUser.community_id == community_id
            ).first()
            if community_user_data is None:
                return jsonify({"message": "Unauthorized"}), HTTPStatus.UNAUTHORIZED
        except Exception as e:
            logger.error(e)
            return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    user_id_list = [
        community_user_data.user_id for community_user_data in community_user_data_list]
    try:
        post_data_list = Post.query.filter(Post.user_id.in_(user_id_list)).all()
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        return_data = [get_post_detailed_info(post_data.id)
                       for post_data in post_data_list]
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify(return_data), HTTPStatus.OK


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
    try:
        payload = request.json
        menus = payload.get("menus")
        message = payload.get("message")
        if not menus:
            raise ValueError("menu is None")
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Bad request error"}), HTTPStatus.BAD_REQUEST

    jwt_user_id = get_jwt_identity()
    if user_id != jwt_user_id:
        return jsonify({"message": "User ID mismatched"}), HTTPStatus.BAD_REQUEST

    try:
        user_data = User.query.filter(User.id == user_id).first()
        if user_data is None:
            return jsonify({"message": "User data not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        shop_data = Shop.query.filter(Shop.id == shop_id).first()
        if shop_data is None:
            return jsonify({"message": "Shop data not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    for menu_id in menus:
        try:
            menu_data = Menu.query.filter(Menu.id == menu_id).first()
            if menu_data is None:
                return jsonify({"message": "Menu data not found"}), HTTPStatus.BAD_REQUEST
        except Exception as e:
            logger.error(e)
            return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        post = Post(user_id=user_id, shop_id=shop_id, message=message)
        db.session.add(post)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    for menu_id in menus:
        try:
            post_menu = PostMenu(post_id=post.id, menu_id=menu_id)
            db.session.add(post_menu)
            db.session.commit()
        except Exception as e:
            logger.error(e)
            db.session.rollback()
            return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify(post.to_dict()), HTTPStatus.OK


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
