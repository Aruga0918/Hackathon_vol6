import click
from flask.cli import with_appcontext
from models import User, Template, Community, Post, Menu, Category, \
    Shop, CommunityUser, PostMenu, ShopCategory
from database import db
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt()


@click.command("seed")
@click.argument("arg")
@with_appcontext
def seed(arg):
    if arg == "all":
        seed_user()
        seed_template()
        seed_community()
        seed_category()
        seed_shop()
        seed_menu()
        seed_post()
        seed_shop_category()
        seed_community_user()
        seed_post_menu()

    if arg == "user":
        seed_user()
    if arg == "template":
        seed_template()
    if arg == "community":
        seed_community()
    if arg == "category":
        seed_category()
    if arg == "menu":
        seed_menu()
    if arg == "shop":
        seed_shop()
    if arg == "post":
        seed_post()
    if arg == "shop_category":
        seed_shop_category()
    if arg == "community_user":
        seed_community_user()
    if arg == "post_menu":
        seed_post_menu()


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


def seed_category():
    categories = [
        Category(
            name=f"sample category {i}",
        )
        for i in range(1, 11)
    ]
    commit_all(categories)


def seed_menu():
    menus = [
        Menu(
            name=f"sample menu {i}",
            shop_id=i,
            price=i*100
        )
        for i in range(1, 11)
    ]
    commit_all(menus)


def seed_shop():
    shops = [
        Shop(
            name=f"sample shop {i}",
            lattitude=i * 10.1,
            longitude=i * 10.1,
            description="hoge" * i,
            address="address" * i
        )
        for i in range(1, 11)
    ]
    commit_all(shops)


def seed_post():
    posts = [
        Post(user_id=i, shop_id=i)
        for i in range(1, 11)
    ]
    commit_all(posts)


def seed_community_user():
    communities_users = []
    for i in range(1, 11):
        user = User.query.filter(User.id == i).first()
        for j in range(1, 4):
            community = Community.query.filter(Community.id == j).first()
            community_user = CommunityUser(community.id, user.id, is_join=j % 2 == 0)
            community_user.user = user
            community.community_user.append(community_user)
            communities_users.append(community_user)
    commit_all(communities_users)


def seed_post_menu():
    posts_menus = []
    for i in range(1, 11):
        post = Post.query.filter(Post.id == i).first()
        shop_id = post.shop_id
        menus = Menu.query.filter(Menu.shop_id == shop_id).all()

        for menu in menus:
            post_menu = PostMenu(post.id, menu.id)
            post_menu.menu = menu
            post.post_menu.append(post_menu)
            posts_menus.append(post_menu)
    commit_all(posts_menus)


def seed_shop_category():
    shop_categories = []
    for i in range(1, 11):
        shop = Shop.query.filter(Shop.id == i).first()
        for j in range(1, 4):
            category = Category.query.filter(Category.id == j).first()
            shop_category = ShopCategory(category.id, shop.id)
            shop_category.shop = shop
            category.shop_category.append(shop_category)
            shop_categories.append(shop_category)
    commit_all(shop_categories)


def seed_template():
    template = [
        Template(
            user_id=i % 10 + 1,
            description=f"{i}"
        )
        for i in range(20)
    ]
    commit_all(template)


def register_command(app):
    app.cli.add_command(seed)
