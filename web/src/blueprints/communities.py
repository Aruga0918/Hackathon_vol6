import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import User, Community, CommunityUser
from database import db

from http import HTTPStatus

communities = Blueprint("communities", __name__)
logger = logging.getLogger("app")


@communities.route("/communities/<int:community_id>", methods=["GET"])
@jwt_required
def get_community_info(community_id):
    """
    コミュニティ情報取得API

    Parameters
    ----------

    Returns
    -------
    """
    user_id = get_jwt_identity()
    # ユーザーがコミュニティに属しているか検証
    try:
        community_user_data = CommunityUser.query.filter(
            CommunityUser.community_id == community_id,
            CommunityUser.user_id == user_id,
            CommunityUser.is_join
        ).first()
        if community_user_data is None:
            return jsonify({"message": "user doesn't join this community"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    # コミュニティ情報を取得
    try:
        community_data = Community.query.filter(Community.id == community_id).first()
        if community_data is None:
            return jsonify({"message": "Community not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    # コミュニティのメンバー情報を取得
    try:
        community_user_data = CommunityUser.query.filter(
            CommunityUser.community_id == community_id
        ).all()
        if community_user_data is None:
            return jsonify({"message": "members data not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    # レスポンスデータの作成
    try:
        ret = dict()
        ret["id"] = community_data.id
        ret["name"] = community_data.name
        ret["comm_icon_url"] = community_data.icon_url
        ret["description"] = community_data.description or ""
        ret["host_user"] = community_data.host_user
        ret["members"] = []
        for cud in community_user_data:
            member_data = dict()

            user_data = User.query.filter(User.id == cud.user_id).first()
            if user_data is None:
                continue
            member_data["id"] = user_data.id
            member_data["uid"] = user_data.uid
            member_data["name"] = user_data.name
            member_data["icon_url"] = user_data.icon_url
            member_data["is_join"] = cud.is_join
            ret["members"].append(member_data)

    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify(ret), HTTPStatus.OK


@communities.route("/communities/create", methods=["POST"])
@jwt_required
def create_community():
    """
    コミュニティ作成API

    Parameters
    ----------
    community_name : str
        コミュニティの名前
    description : str
        コミュニティの説明
    members : List[int]
        招待するuserのid
    community_icon : str, default None
        アイコンのurl

    Returns
    -------
    community_id : int
        コミュニティのid
    """
    try:
        payload = request.json
        community_name = payload.get("community_name")
        if community_name is None:
            raise ValueError("community_name is None")
    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Bad request error"}), 400

    user_id = get_jwt_identity()
    try:
        user_data = User.query.filter(User.id == user_id).first()
        if user_data is None:
            return jsonify({"message": "User data not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    # 招待したいユーザーのデータの有無を確認する
    members = payload.get("members")
    member_ids = []
    try:
        for member_uid in members:
            member_data = User.query.filter(User.uid == member_uid).first()
            if member_data is None:
                return jsonify({"message": "Member data not found"}), HTTPStatus.BAD_REQUEST
            member_ids.append(member_data.id)
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    # コミュニティ作成
    description = payload.get("description")
    try:
        community = Community(community_name, user_id, description=description)
        db.session.add(community)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    # メンバー登録
    try:
        community_user = CommunityUser(community.id, user_id, is_join=True)
        db.session.add(community_user)
        db.session.commit()
        for member_id in member_ids:
            community_user = CommunityUser(community.id, member_id)
            db.session.add(community_user)
            db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return jsonify(community.to_dict()), HTTPStatus.OK


@communities.route("/communities/<int:community_id>", methods=["DELETE"])
@jwt_required
def delete_community(community_id):
    """
    コミュニティ削除API

    Parameters
    ----------

    Returns
    -------

    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})


@communities.route("/communities/<int:community_id>", methods=["PATCH"])
@jwt_required
def edit_community(community_id):
    """
    コミュニティ編集API

    Parameters
    ----------
    community_name : str
        コミュニティの名前
    description : str
        コミュニティの説明
    community_icon : str, default None
        アイコンのurl    

    Returns
    -------

    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})


@communities.route("/communities/<int:community_id>/join", methods=["POST"])
@jwt_required
def join_community(community_id):
    """
    コミュニティ参加API

    Parameters
    ----------

    Returns
    -------
    community_id : int
        コミュニティのid    

    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})


@communities.route("/communities/<int:community_id>/join", methods=["DELETE"])
@jwt_required
def cancel_community_invitation(community_id):
    """
    コミュニティ参加拒否API

    Parameters
    ----------

    Returns
    -------　
    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})


@communities.route("/communities/<int:community_id>/add", methods=["PATCH"])
@jwt_required
def invite_users(community_id):
    """
    ユーザー招待API

    Parameters
    ----------
    members : List[int]
        招待するuserのid

    Returns
    -------　
    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})


@communities.route("/communities/<int:community_id>/members/<int:user_id>", methods=["DELETE"])
@jwt_required
def withdraw_community(community_id, user_id):
    """
    ユーザー退会API

    Parameters
    ----------

    Returns
    -------　
    """
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})


@communities.route("/communities/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})
