import logging
from flask import Blueprint, jsonify
from models import User, Post
from flask_jwt_extended import jwt_required

from http import HTTPStatus

users = Blueprint("users", __name__)
logger = logging.getLogger("app")


@users.route("/users/<int:user_id>", methods=["GET"])
def get_user_info(user_id):
    """
    ユーザー情報取得API

    Parameters
    ----------

    Returns
    -------
    name : str
        ユーザー名
    id : int
        intの方のユーザid           
    uid : str
        文字列の方のユーザid
    icon_url : str
        アイコンのURL
    profile : str
        ユーザーのプロフィール
    """
    try:
        user_data = User.query.get(user_id)
        if user_data is None:
            return jsonify({"message": "User data not found"}), 401

        name = user_data.name
        uid = user_data.uid
        icon_url = user_data.icon_url
        profile = user_data.profile

        post_data = Post.query.filter(Post.user_id == user_id).all()
        post_id = [post.id for post in post_data]

        return_data = {
            "name": name,
            "id": user_id,
            "uid": uid,
            "icon_url": icon_url,
            "profile": profile,
            "post": post_id
        }

    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    return jsonify(return_data), HTTPStatus.OK


@users.route("/users", methods=["GET"])
def get_users_info():
    """
    ユーザー一覧取得API

    Parameters
    ----------

    Returns
    -------
    [
        name : str
            ユーザー名
        id : int
            intの方のユーザid        
        uid : str
            文字列の方のユーザid
        icon_url : str
            アイコンのURL
        profile : str
            ユーザーのプロフィール
    ]
    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@users.route("/users/withdrawal", methods=["DELETE"])
@jwt_required
def withdraw_user():
    """
    ユーザー削除API

    Parameters
    ----------

    Returns
    -------
    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@users.route("/users/edit", methods=["PATCH"])
@jwt_required
def edit_user():
    """
    ユーザー編集API

    Parameters
    ----------
    user_name : str
        ユーザー名
    user_id : str
        文字列の方のユーザid
    password : str
        パスワード
    user_icon : str, default None
        アイコンのURL   
    profile : str
        ユーザーのプロフィール

    Returns
    -------
    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@users.route("/users/communities", methods=["GET"])
@jwt_required
def get_user_communities():
    """
    所属コミュニティ一覧取得API

    Parameters
    ----------

    Returns
    -------
    id : int
        コミュニティのid
    name : str
        コミュニティの名前
    icon_url : str
        アイコンのURL, default None
    member_cnt : int
        メンバーの数
    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK


@users.route("/users/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
