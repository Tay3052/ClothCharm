from apps.app import db
from apps.auth.forms import LoginForm, SignUpForm
from apps.crud.models import User
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

# Blueprintを使ってauthを生成する
auth = Blueprint("auth", __name__, template_folder="templates", static_folder='./static')


# indexエンドポイントを作成する
@auth.route("/")
def index():
    return render_template("auth/index.html")

# ログインとサインアップのエンドポイントを作成する
@auth.route("/login", methods=["GET", "POST"])
def login():
    loginform = LoginForm()
    signupform = SignUpForm()
    
    if signupform.validate_on_submit():
        user = User(
            username=signupform.username.data,
            email=signupform.email.data,
            password=signupform.password.data,
        )

        # メールアドレス重複チェックをする
        if user.is_duplicate_email():
            flash("指定のメールアドレスは登録済みです")
            return redirect(url_for("auth.signup"))

        # ユーザー情報を登録する
        db.session.add(user)
        db.session.commit()

        # ユーザー情報をセッションに格納する
        login_user(user)

        # GETパラメータにnextキーが存在し、値がない場合はユーザーの一覧ページへリダイレクトする
        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_ = url_for("detector.index")
        return redirect(next_)
    
    if loginform.validate_on_submit():
        # メールアドレスからユーザーを取得する
        user = User.query.filter_by(email=loginform.email.data).first()

        # ユーザーが存在しパスワードが一致する場合はログインを許可する
        if user is not None and user.verify_password(loginform.password.data):
            login_user(user)
            return redirect(url_for("detector.index"))

        # ログイン失敗メッセージを設定する
        flash("メールアドレスかパスワードか不正です")
    return render_template("auth/login.html", loginform=loginform, signupform=signupform)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("detector.index"))

