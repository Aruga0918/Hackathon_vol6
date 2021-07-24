import logging

from flask import jsonify, Blueprint, request

from http import HTTPStatus

from models import Shop, Menu, Post, PostMenu, CommunityUser

rankings = Blueprint("rankings", __name__)
logger = logging.getLogger("app")


@rankings.route("/rankings/shops/<int:shop_id>", methods=["GET"])
def get_rankings(shop_id):
    """
    ランキング取得API

    Parameters
    ----------
    n_cnt : int, default 3
        returnの数
    community_id : int. default None
        コミュニティid.　指定がない時は全投稿を用いたランキングを作成

    Returns
    -------
    [
        {
            "menu_id" : メニューid
            "name" : メニュー名
            "price" : 価格
            "posted_cnt" : 食べた人の数
        }
        ...
    ]

    """
    payload = request.json
    n_cnt = payload.get("n_cnt")
    if n_cnt is None:
        n_cnt = 3
    community_id = payload.get("community_id")

    try:
        shop_data = Shop.query.filter(Shop.id == shop_id).first()
        if shop_data is None:
            return jsonify({"message": "Shop data not found"}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    try:
        if community_id is None:
            post_data_list = Post.query.filter(Post.shop_id == shop_id).all()
        else:
            community_user_data_list = CommunityUser.query.filter(CommunityUser.community_id == community_id).all()
            user_id_list = [community_user_data.user_id for community_user_data in community_user_data_list]
            post_data_list = Post.query.filter(Post.shop_id == shop_id, Post.user_id.in_(user_id_list)).all()
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    post_id_list = [post_data.id for post_data in post_data_list]

    try:
        post_menu_data_list = PostMenu.query.filter(PostMenu.post_id.in_(post_id_list)).all()
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    posted_menu_list = [post_menu_data.menu_id for post_menu_data in post_menu_data_list]
    top_n_menu_id, posted_cnt_dict = get_top_n_id(n_cnt, posted_menu_list)

    try:
        menu_data_list = [Menu.query.filter(Menu.id == menu_id).first() for menu_id in top_n_menu_id]
    except Exception as e:
        logger.error(e)
        return jsonify({"message": f"Internal server error\n{e}"}), HTTPStatus.INTERNAL_SERVER_ERROR

    return_data = [
        {
            "menu_id": menu_data.id,
            "name": menu_data.name,
            "price":menu_data.price,
            "posted_cnt": posted_cnt_dict.get(menu_data.id)
        }
        for menu_data in menu_data_list
    ]

    return jsonify(return_data), HTTPStatus.OK


def get_top_n_id(n_cnt, posted_menu_list):
    """
    n位までのメニューidのリストと投稿数を返す関数

    Parameters
    ----------
    n_cnt : int
        順位
    posted_menu_list : list[int]
        メニューidのリスト

    Returns
    -------
    top_n_menu_id : list[int]
        n位までのメニューidのリスト
    menu_cnt_dict : {メニューid : 投稿数}
        各メニューの投稿数
    """
    menu_cnt_dict = {}
    for menu in posted_menu_list:
        if menu in menu_cnt_dict:
            menu_cnt_dict[menu] += 1
        else:
            menu_cnt_dict[menu] = 0

    sorted_menu = sorted(menu_cnt_dict.items(), key = lambda x : x[1], reverse=True)

    rank = 0
    top_n_menu_id = []
    previous_menu_cnt = -1

    for menu in sorted_menu:
        menu_id = menu[0]
        menu_cnt = menu[1]

        if menu_cnt == 0:
            break

        if menu_cnt != previous_menu_cnt:
            rank += 1

        if rank > n_cnt:
            break

        top_n_menu_id.append(menu_id)
        previous_menu_cnt = menu_cnt

    return top_n_menu_id, menu_cnt_dict


@rankings.route("/rankings/test")
def index():
    logger.warn("warn")
    logger.error("error")
    logger.critical("critical")
    return jsonify({"message": "api_test"}), HTTPStatus.OK
