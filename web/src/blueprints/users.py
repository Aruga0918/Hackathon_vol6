import logging
from flask import Blueprint, jsonify, request
from models import User, Community, CommunityUser
from flask_jwt_extended import get_jwt_identity, jwt_required

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
            return jsonify({"message": "User data not found"}), HTTPStatus.BAD_REQUEST

    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return_data = {
        "name": user_data.name,
        "id": user_data.id,
        "uid": user_data.uid,
        "icon_url": user_data.icon_url,
        "profile": user_data.profile
    }

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
    try:
        users_data = User.query.all()
        if not users_data:
            return jsonify({"message": "User data not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return_data = []
    for user_data in users_data:
        return_data.append(
            {
                "name": user_data.name,
                "id": user_data.id,
                "uid": user_data.uid,
                "icon_url": user_data.icon_url,
                "profile": user_data.profile
            }
        )

    return jsonify(return_data), HTTPStatus.OK


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
    user_id = get_jwt_identity()
    try:
        user_data = User.query.filter(User.id == user_id).first()
        if user_data is None:
            return jsonify({"message": "User data not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        community_user_data = CommunityUser.query.filter(
            CommunityUser.user_id == user_id).all()
        if not community_user_data:
            return jsonify({"message": "Community data not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return_data = []
    for data in community_user_data:
        community_id = data.community_id
        community_data = Community.query.filter(Community.id == community_id).first()
        member_cnt = CommunityUser.query.filter(
            CommunityUser.community_id == community_id).count()
        return_data.append(
            {
                "id": community_id,
                "name": community_data.name,
                "icon_url": community_data.icon_url,
                "member_cnt": member_cnt
            }
        )

    return jsonify(return_data), HTTPStatus.OK


@users.route("/users/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
