from flask import Flask, render_template, request, make_response, session, flash, redirect, url_for
from flask_login import LoginManager
from flask_admin import Admin
# SQLAlchemyなどのインポート
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from apps.crud.models import User

# Flask-Adminのインポート
from flask_admin import Admin
from flask_admin.contrib.sqla  import  ModelView 


# CSRF対策モジュール
from flask_wtf.csrf import CSRFProtect

# configファイルのインポート
from apps.config import config

# SQLAlchemyのインスタンス化
db = SQLAlchemy()
csrf = CSRFProtect()

login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = ""

def create_app(config_key):
    app = Flask(__name__)
    
    app.config.from_object(config[config_key])
    
    # app.config.from_envvar("APPLICATION_SETTINGS")
    
    # アプリのconfigを設定
    # app.config.from_mapping(
    #     SECRET_KEY = "secret_key",
    #     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:wu65vnV5YLNwPYL9bSJY@localhost:3306/flask?charset=utf8",
    #     SQLALCHEMY_TRACK_MODIFICATIONS = False,
    #     SQLALCHEMY_ECHO = True,
    #     WTF_CSRF_SECRET_KEY = "Adhjhdasdbskjdbas"
    # )
        
    csrf.init_app(app)
    
    db.init_app(app)
    
    Migrate(app, db)

    login_manager.init_app(app)
    
# Admin設定
#######################################################################
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# Adminルーティング
#######################################################################
    admin = Admin(app, name='ClothCharm', template_mode='bootstrap3')
    from apps.crud.models import User
    admin.add_view(ModelView(User, db.session))

    from apps.detector.models import UserImage, Follow, CategoryName, Condition, Color, Sex, Size, Favorite
    admin.add_view(ModelView(UserImage, db.session))
    admin.add_view(ModelView(Follow, db.session))
    admin.add_view(ModelView(CategoryName, db.session))
    admin.add_view(ModelView(Condition, db.session))
    admin.add_view(ModelView(Color, db.session))
    admin.add_view(ModelView(Sex, db.session))
    admin.add_view(ModelView(Size, db.session))
    admin.add_view(ModelView(Favorite, db.session))
    
# 
#######################################################################
    from apps.crud import views as crud_views
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

# auth   
#####################################################################
    
    from apps.auth import views as auth_views
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

# detector  
#######################################################################    

    # これを主軸にする
    from apps.detector import views as dt_views
    app.register_blueprint(dt_views.dt)
    
# Mypage  
#######################################################################    
    
    from apps.original import views as mypage_views
    app.register_blueprint(mypage_views.original, url_prefix="/original")
    
# Market
#######################################################################

    from apps.market import views as market_views
    app.register_blueprint(market_views.market, url_prefix="/market")
    
# Deal
#######################################################################

    # from apps.deal import views as deal_views
    # app.register_blueprint(deal_views.deal, url_prefix="/deal")
    
    
    return app