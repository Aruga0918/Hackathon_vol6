import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from models import User, Community, CommunityUser
from database import db

from http import HTTPStatus

communities = Blueprint("communities", __name__)
logger = logging.getLogger("app")


@communities.route("/communities", methods=["POST"])
@jwt_required
def create_community():
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
        return jsonify({"message": f"Internal server error\n{e}"}), 500

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
        return jsonify({"message": f"Internal server error\n{e}"}), 500

    # コミュニティ作成
    description = payload.get("description")
    try:
        community = Community(community_name, user_id, description=description)
        db.session.add(community)
        db.session.commit()
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return jsonify({"message": f"Internal server error\n{e}"}), 500

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
        return jsonify({"message": f"Internal server error\n{e}"}), 500

    return jsonify(community.to_dict()), 200


@communities.route("/communities/<int:community_id>", methods=["GET"])
@jwt_required
def get_community_info(community_id):
    user_id = get_jwt_identity()
    # ユーザーがコミュニティに属しているか検証
    try:
        community_user_data = CommunityUser.query.filter(
            CommunityUser.community_id == community_id and
            CommunityUser.user_id == user_id and
            CommunityUser.is_join is True
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
        ret["comm_icon_url"] = community_data.comm_icon_url
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
            ret["members"].append(member_data)

    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return ret


@communities.route("/communities/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})
