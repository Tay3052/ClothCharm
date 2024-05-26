from flask_wtf.form import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import PasswordField, StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, length


# ユーザー新規作成とユーザー編集フォームクラス
class UserForm(FlaskForm):
    # ユーザーフォームのusername属性のラベルとバリデータを設定する
    username = StringField(
        "ユーザー名",
        validators=[
            DataRequired(message="ユーザー名は必須です。"),
            length(max=30, message="30文字以内で入力してください。"),
        ],
    )

    # ユーザーフォームemail属性のラベルとバリデータを設定する
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired(message="メールアドレスは必須です。"),
            Email(message="メールアドレスの形式で入力してください。"),
        ],
    )

    # ユーザーフォームpassword属性のラベルとバリデータを設定する
    password = PasswordField("パスワード", validators=[DataRequired(message="パスワードは必須です。"), length(min=5, max=30, message="パスワードは5文字以上必要です。")])

    # ユーザーフォームsubmitの文言を設定する
    submit = SubmitField("新規登録")

class UpdateForm(FlaskForm):
    # ユーザーフォームのusername属性のラベルとバリデータを設定する

    username = StringField(
        "ユーザーネーム",
        validators=[
            DataRequired(message="ユーザー名は必須です。"),
            length(max=30, message="30文字以内で入力してください。"),
        ],
    )

    explain = StringField(
        "プロフィール"
    )

    address = StringField(
        "住所",
        validators=[
            DataRequired(message="ユーザー名は必須です。"),
            length(max=50, message="50文字以内で入力してください。"),
        ],
    )
    
    phone = StringField(
        "電話番号",
        validators=[
            length(max=13, message="13文字以内で入力してください。"),
        ],
    )

    image = FileField(
        validators=[
            FileRequired(message="画像ファイルを指定してください。"),
            FileAllowed(["jpg", "jpeg", "png"], "サポートされてない画像形式です。"),
        ]
    )

    # ユーザーフォームsubmitの文言を設定する
    submit = SubmitField("確定")