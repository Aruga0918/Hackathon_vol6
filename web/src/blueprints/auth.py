from http import HTTPStatus
from flask_bcrypt import Bcrypt
from database import db
from models import User
from flask import jsonify, Blueprint, request
import logging
from flask_jwt_extended import (
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    create_access_token,
    create_refresh_token
)


bcrypt = Bcrypt()

auth = Blueprint("auth", __name__)
logger = logging.getLogger("app")


@auth.route("/auth/signin", methods=["POST"])
def signin():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), HTTPStatus.BAD_REQUEST
    data = request.get_json()
    uid = data["uid"]
    password = data["password"]

    try:
        user = db.session.query(User).filter_by(uid=uid).first()
        if not user:
            return jsonify({"message": f"not user {uid}"}), HTTPStatus.UNAUTHORIZED

        username = user.name
        icon_url = user.icon_url
        _id = user.id

        if not bcrypt.check_password_hash(user.password, password):
            return jsonify({"message": "Bad username or password"}), HTTPStatus.UNAUTHORIZED
    except Exception as e:
        return jsonify({"message": f"An error occurred\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return (
        jsonify(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "username": username,
                "icon_url": icon_url,
                "id": _id,
                "uid": uid
            }
        ),
        HTTPStatus.OK
    )

    return (jsonify({"access_token": access_token}), HTTPStatus.OK)


@auth.route("/auth/signup", methods=["POST"])
def signup():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), HTTPStatus.BAD_REQUEST

    try:
        data = request.get_json()
        uid = data["uid"]
        name = data["username"]
        password = data["password"]

        user = db.session.query(User).filter_by(uid=uid).first()
    except Exception as e:
        logger.warn(e)
        db.session.rollback()
        return jsonify({"message": "Internal server error can't get params"}), HTTPStatus.INTERNAL_SERVER_ERROR

    # 新規登録
    if not user:
        hashed_pass = bcrypt.generate_password_hash(password).decode('utf-8')
        try:
            user = User(uid=uid, name=name, password=hashed_pass)
            db.session.add(user)
            db.session.commit()
            icon_url = user.icon_url
            _id = user.id
        except Exception as e:
            logger.warn(e)
            db.session.rollback()
            return jsonify({"message": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        db.session.rollback()
        return jsonify({"message": "this user id is already used"}), HTTPStatus.INTERNAL_SERVER_ERROR

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return (
        jsonify(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "username": name,
                "icon_url": icon_url,
                "id": _id,
                "uid": uid
            }
        ),
        HTTPStatus.OK
    )


@auth.route("/auth/refresh", methods=["GET"])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {"access_token": create_access_token(identity=current_user)}
    return jsonify(ret), HTTPStatus.OK


@auth.route("/auth/protected")
@jwt_required
def protected():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    userid = get_jwt_identity()
    return jsonify({"message": f"auth_protected {userid}"})


@auth.route("/auth/test")
def test():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"})
