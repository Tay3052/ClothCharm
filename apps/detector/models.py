from datetime import datetime

from apps.app import db

class UserImage(db.Model):
    __tablename__ = "user_images"
    __table_args__=({"mysql_charset": "utf8mb4"})

    # 画像ID
    id = db.Column(db.Integer, primary_key=True)
    # ユーザーID
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # 買った人のID
    # buyer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # 画像の名前
    image_name = db.Column(db.String(255))
    # 画像のパス
    image_path = db.Column(db.String(255))
    # 画像が売れたかどうか
    sold = db.Column(db.Boolean, default=False)
    # レンタル状況
    rental = db.Column(db.Boolean, default=False)
    # 説明
    explain = db.Column(db.Text)
    # カテゴリ
    category = db.Column(db.Integer, db.ForeignKey("categorynames.id"))
    # サイズ
    size = db.Column(db.Integer, db.ForeignKey("sizes.id"))
    # 状態
    condition = db.Column(db.Integer, db.ForeignKey("conditions.id"))
    # 価格
    price = db.Column(db.Integer)
    # 色情報
    color = db.Column(db.Integer, db.ForeignKey("colors.id"))
    # 性別
    sexual = db.Column(db.Integer, db.ForeignKey("sexuals.id"))
    # 発送予定日
    send = db.Column(db.Integer)
    # 作成日
    created_at = db.Column(db.DateTime, default=datetime.now)
    # 更新日
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

####################################################################
class SellInfo(db.Model):
    __tablename__ = "sellinfos"
    __table_args__=({"mysql_charset": "utf8mb4"})
    
    # ID
    id = db.Column(db.Integer, primary_key=True)
    # 売人ID
    
    seller_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # 顧客ID
    buyer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    # 取引状況ID
    # 1: 送金待ち
    # 2: 送金済み
    # 3: 発送済み
    # 4: 到着済み
    # 5: 取引完了
    deal_id = db.Column(db.Integer)
    
    # 商品ID
    product_id = db.Column(db.Integer, db.ForeignKey("user_images.id"))
    

####################################################################
class Color(db.Model):
    __tablename__ = "colors"
    __table_args__=({"mysql_charset": "utf8mb4"})

    # 出品ID
    id = db.Column(db.Integer, primary_key=True)
    # 種類名
    color = db.Column(db.String(255))
    
    # backrefを使用する、外部キー設定
    col = db.relationship("UserImage", backref="colors")

####################################################################
class CategoryName(db.Model):
    __tablename__ = "categorynames"
    __table_args__=({"mysql_charset": "utf8mb4"})

    # 出品ID
    id = db.Column(db.Integer, primary_key=True)
    # 種類名
    categoryname = db.Column(db.String(255))
    
    # backrefを使用する
    cat = db.relationship("UserImage", backref="categorynames")

####################################################################    
class Condition(db.Model):
    __tablename__ = "conditions"
    __table_args__=({"mysql_charset": "utf8mb4"})

    # 出品ID
    id = db.Column(db.Integer, primary_key=True)
    # 種類名
    condition = db.Column(db.String(255))
    
    # backrefを使用する
    con = db.relationship("UserImage", backref="conditions")
    
####################################################################    
class Size(db.Model):
    __tablename__ = "sizes"
    __table_args__=({"mysql_charset": "utf8mb4"})

    # 出品ID
    id = db.Column(db.Integer, primary_key=True)
    # 種類名
    size = db.Column(db.String(255))
    
    # backrefを使用する
    siz = db.relationship("UserImage", backref="sizes")

####################################################################
class Sex(db.Model):
    __tablename__ = "sexuals"
    __table_args__=({"mysql_charset": "utf8mb4"})
    
    id = db.Column(db.Integer, primary_key=True)
    
    sex = db.Column(db.String(255))
    
    image = db.relationship("UserImage", backref="sexuals")

####################################################################    
class SendProduct(db.Model):
    __tablename__ = "sendproducts"
    __table_args__ = ({"mysql_charset": "utf8mb4"})
    
    id = db.Column(db.Integer, primary_key=True)
    send = db.Column(db.String(255))
    
####################################################################
class Follow(db.Model):
    __tablename__ = "follows" 
    
    id = db.Column(db.Integer, primary_key=True)
    follow = db.Column(db.Integer, db.ForeignKey("users.id"))
    follower = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

# お気に入り機能
####################################################################
class Favorite(db.Model):
    __tablename__ = "favorites"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("user_images.id"))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)