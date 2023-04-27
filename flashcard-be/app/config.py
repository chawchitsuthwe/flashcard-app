import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "default_secret_key")
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    mysql_username = os.getenv("FLASK_DB_USERNAME")
    mysql_password = os.getenv("FLASK_DB_PASSWORD")
    mysql_host = os.getenv("FLASK_DB_HOST")
    mysql_port = os.getenv("FLASK_DB_PORT")
    mysql_db = os.getenv("FLASK_DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}"

config_by_name = dict(
    dev= DevelopmentConfig
)

key = Config.SECRET_KEY
