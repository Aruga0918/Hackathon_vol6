import os


class DevelopmentConfig:

    user = os.environ["APP_DATABASE_USER"]
    password = os.environ["APP_DATABASE_PASSWORD"]
    host = os.environ["APP_DATABASE_HOST"]
    db_name = os.environ["APP_DATABASE_NAME"]
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


Config = DevelopmentConfig