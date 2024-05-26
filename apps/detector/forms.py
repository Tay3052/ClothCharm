from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_wtf.form import FlaskForm
from wtforms import SubmitField, StringField, SelectField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, length

class UploadImageForm(FlaskForm):
    title = StringField("タイトル", validators=[
            DataRequired(message="この項目は必須です。"),
        ] )
    explain = TextAreaField("説明", validators=[
            DataRequired(message="この項目は必須です。"),
        ])
    sexual = SelectField("性別", choices=[(1, "メンズ"), (2, "レディース"), (3,"ジェンダーレス"), (4,"オリジナルデザイン")], validators=[
            DataRequired(message="この項目は必須です。"),
        ])
    category = SelectField("カテゴリー", choices=[(1, "トップス"), (2, "シャツ"), (3, "スカート"), (4, "パンツ"), (5, "ワンピース"), (6, "ジャケット/アウター"), (7, "セットアップ"),(8, "スーツ/フォーマル"),(9, "靴下"),(10, "シューズ"),(11, "浴衣"),(12, "水着"),(13, "ファッション雑貨"),(14, "バッグ"),(15, "アクセサリー")], validators=[
            DataRequired(message="この項目は必須です。"),
        ])
    size = SelectField("サイズ", choices=[(1, "XS"), (2, "S"), (3, "M"), (4, "L"),(5, "LL")], validators=[
            DataRequired(message="この項目は必須です。"),
        ])
    condition = SelectField("商品の状態", choices=[(1, "新品"), (2, "ほぼ未使用"), (3, "目立った傷や汚れなし"), (4, "やや傷や汚れあり")], validators=[
            DataRequired(message="この項目は必須です。"),
        ])
    send = SelectField("発送時期", choices=[(1, "1〜2日で発送"), (2, "3〜4日で発送"), (3, "1週間以内に発送"), (4, "1週間以上発送待ち")], validators=[
            DataRequired(message="この項目は必須です。"),
        ])
    price = IntegerField("価格", validators=[
            DataRequired(message="この項目は必須です。"),
        ])
    
    image = FileField(
        validators=[
            FileRequired(message="画像ファイルを指定してください。"),
            FileAllowed(["jpg", "jpeg", "png"], "サポートされてない画像形式です。"),
        ]
    )
    
    submit = SubmitField("アップロード")
    
class DeleteForm(FlaskForm):
    submit = SubmitField("削除")
    