import logging
from flask import Blueprint, jsonify
from models import User, Post


users = Blueprint("users", __name__)
logger = logging.getLogger("app")


@users.route("/users/<int:user_id>", methods=["GET"])
def get_user_info(user_id):
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
            "uid": uid,
            "icon_url": icon_url,
            "profile": profile,
            "post": post_id
        }

    except Exception as e:
        logger.error(e)
        return jsonify({"message": "Internal server error"}), 500

    return jsonify(return_data), 200


@users.route("/users/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})
