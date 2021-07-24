import click
from flask.cli import with_appcontext
from models import User, Community, Post, Menu, Category, \
    Shop, CommunityUser, PostMenu, ShopCategory
from database import db
from flask_bcrypt import Bcrypt

import json
import itertools
import random

bcrypt = Bcrypt()

shops_json_data = json.load(open("./assets/preprocessed_shops.json"))


@click.command("seed")
@click.argument("arg")
@with_appcontext
def seed(arg):
    if arg == "all":
        seed_user()
        seed_community()
        seed_community_user()
        seed_shop_category_menu()
        seed_post()

    if arg == "user":
        seed_user()
    elif arg == "community":
        seed_community()
    elif arg == "community_user":
        seed_community_user()
    elif arg == "shop_cat_menu":
        seed_shop_category_menu()
    elif arg == "shop":
        seed_shop()
    elif arg == "menu":
        seed_menu()
    elif arg == "category":
        seed_category()
    elif arg == "post":
        seed_post()


def commit_all(objects):
    try:
        db.session.add_all(objects)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()


def seed_user():
    users = [
        User(
            uid=f"uid{i}",
            name=f"sample{i}",
            password=bcrypt.generate_password_hash(f"password{i}").decode('utf-8'),
            profile="hoge" * i
        )
        for i in range(1, 11)
    ]
    commit_all(users)


def seed_community():
    communities = [
        Community(
            name=f"sample community {i}",
            host_user=i,
        )
        for i in range(1, 11)
    ]
    commit_all(communities)


def seed_community_user():
    # communities_users = []
    data = []
    for i in range(1, 11):
        user = User.query.filter(User.id == i).first()
        for j in range(1, 4):
            community = Community.query.filter(Community.id == j).first()
            community_user = CommunityUser(
                user_id=user.id, community_id=community.id, is_join=j % 2 == 0)
            data.append(community_user)
    commit_all(data)


def seed_shop_category_menu():
    # categoryをadd
    seed_category()

    # shopをadd
    seed_shop()

    # menuをadd
    seed_menu()


def seed_category():
    categories = [
        Category(name=cat)
        for cat in set(data["category"] for data in shops_json_data)
    ]
    commit_all(categories)


def seed_shop():
    shops = [
        Shop(
            name=data["name"],
            lattitude=data["lattitude"],
            longitude=data["longitude"],
            description=data["description"],
            address=data["address"],
            icon_url=data["icon_url"]
        )
        for data in shops_json_data
    ]
    commit_all(shops)


def seed_menu():
    menus = list(itertools.chain.from_iterable([
        [
            Menu(
                name=name,
                shop_id=Shop.query.filter(Shop.name == data["name"]).first().id,
                price=price
            )
            for name, price in data["menu"].items()
        ] for data in shops_json_data
    ]))
    commit_all(menus)


def seed_post():
    # data = []
    for user_id in range(1, 11):
        for shop_id in range(1, 11):
            data = []
            post = Post(user_id=user_id, shop_id=shop_id, message="おいしかった"*user_id)
            menus = Menu.query.filter(Menu.shop_id == shop_id).all()
            sampled_menus = random.sample(menus, min(len(menus), 4))

            for menu in sampled_menus:
                post_menu = PostMenu(post_id=post.id, menu_id=menu.id)
                post.menus.append(menu)
                data.append(post)
    commit_all(data)


def register_command(app):
    app.cli.add_command(seed)
