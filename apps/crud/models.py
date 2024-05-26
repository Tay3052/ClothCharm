from datetime import datetime
from apps.app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

# db.Modelを継承したUserクラスを作成する
class User(db.Model, UserMixin):
    # テーブル名を指定する
    __tablename__ = "users"
    # カラムを定義する
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    sex = db.Column(db.Integer)
    password_hash = db.Column(db.String(255))
    profile = db.Column(db.Text)
    icon_path = db.Column(db.String(255))
    zipcode = db.Column(db.String(255))
    address = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    fullname = db.Column(db.String(255))
    furigana = db.Column(db.String(255))
    noticeid = db.Column(db.String(255))
    points = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # backrefを利用しrelation情報を設定する
    user_images = db.relationship("UserImage", backref="users")

    # パスワードをセットするためのプロパティ
    @property
    def password(self):
        raise AttributeError("読み取り不可")

    # パスワードをセットするためのセッター関数でハッシュ化したパスワードをセットする
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # パスワードチェックをする
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # メールアドレス重複チェックをする
    def is_duplicate_email(self):
        return User.query.filter_by(email=self.email).first() is not None


# ログインしているユーザー情報を取得する関数を作成する
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Flask-Admin用のモデル
class AdminUser(db.Model):
    __tablename__ = "admin_users"
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(250))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __unicode__(self):
        return self.username

"""class Follow(db.Model):
    __tablename__ = "follows" 
    
    id = db.Column(db.Integer, primary_key=True)
    follow = db.Column(db.Integer, db.ForeignKey("users.id"))
    follower = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)"""