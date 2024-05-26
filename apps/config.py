from pathlib import Path

basedir = Path(__file__).parent.parent


class BaseConfig:
    SECRET_KEY = "secret_key"
    WTF_CSRF_SECRET_KEY = "Adhjhdasdbskjdbas"
    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://hew:password@localhost:3306/flask?charset=utf8"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


config = {
    "local": LocalConfig,
}
