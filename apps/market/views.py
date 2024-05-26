from flask import Blueprint, render_template, request, redirect, url_for, current_app, send_from_directory, jsonify
from flask_login import current_user, login_required
from apps.detector.models import UserImage, Color, CategoryName, Condition, Size, Favorite
from apps.app import db
from flask_paginate import Pagination, get_page_args
from flask_login import current_user, login_required
from datetime import datetime

market = Blueprint("market", __name__, template_folder="templates")

# ページネーション関数
def image_paginate(lengs):
    if lengs == None:
        lengs = UserImage.query.order_by(UserImage.id.desc()).all()
    page = request.args.get(get_page_args(), type=int, default=1)
    products = lengs[(page-1)*9:page*9]
    pagination = Pagination(page=page, per_page=9, rows=products, total=len(lengs),  css_framework="bootstrap5", search=False)
    
    return pagination

@market.route("/shop/", methods=["GET"])
def shop():
    products = UserImage.query.order_by(UserImage.id.desc()).all()
    return render_template("market/shop-sidebar.html", products=products)

@market.route("/shop/price/<int:price>", methods=["GET"])
def shopprice(price):    
    if price == 1:
        products = UserImage.query.filter(UserImage.price <= 2000 , UserImage.price >= 1000).order_by(UserImage.id.desc()).all()

    if price == 2:
        products = UserImage.query.filter(UserImage.price <= 3000 , UserImage.price >= 2000).order_by(UserImage.id.desc()).all()

    if price == 3:
        products = UserImage.query.filter(UserImage.price <= 4000 , UserImage.price >= 3000).order_by(UserImage.id.desc()).all()
    
    if price == 4:
        products = UserImage.query.filter(UserImage.price <= 5000 , UserImage.price >= 4000).order_by(UserImage.id.desc()).all()

    # pagination = image_paginate(products)

    return render_template("market/shop-sidebar.html", price=price)

# 性別
@market.route("shop/category/<int:key>")
def shopcategory(key):
    products = UserImage.query.filter(UserImage.sexual==key).order_by(UserImage.id.desc()).all()
    
    # pagination = image_paginate()
    
    return render_template("market/shop-sidebar.html", products=products)

# サイズ
@market.route("shop/size/<int:key>")
def shopsize(key):
    
    products = UserImage.query.filter(UserImage.size==key).order_by(UserImage.id.desc()).all()
    
    # pagination = image_paginate(products)
    return render_template("market/shop-sidebar.html", products=products)

@market.route("detail/<int:id>")
def detail(id):
    product = UserImage.query.filter_by(id=id).first()
    color = Color.query.filter_by(id=product.color).first()
    categories = CategoryName.query.filter_by(id=product.category).first()
    condition = Condition.query.filter_by(id=product.condition).first()
    size = Size.query.filter_by(id=product.size).first()
    allproducts = UserImage.query.order_by(UserImage.id.desc()).all()
    
    return render_template("market/single-product.html", product=product, color=color, categories=categories, condition=condition, size=size, allproducts=allproducts)
    
@market.route("/payment/<int:id>", methods=["GET", "POST"])
@login_required
def payment(id):
    product = UserImage.query.filter_by(id=id).first()
    
    return render_template("market/accountant.html", product=product)

@market.route("/paymentComplete/<int:id>", methods=["GET", "POST"])
@login_required
def paymentComplete(id):
    product = UserImage.query.filter_by(id=id).first()
    if product.sold == False:
        product.sold = True
        db.session.commit()
    return render_template("market/purchase.html", product=product)

@market.route("/rental/<int:id>", methods=["GET", "POST"])
def rental(id):
    product = UserImage.query.filter_by(id=id).first()

    return render_template("market/rental.html", product=product)

@market.route("/rentalComplete/<int:id>", methods=["GET", "POST"])
def rentalComplete(id):
    product = UserImage.query.filter_by(id=id).first()
    if product.rental == False:
        product.rental = True
        db.session.commit()
    return render_template("market/rentalok.html", product=product)

@market.route("/favorite/<int:id>", methods=["GET", "POST"])
@login_required
def favorite(id):
    product = UserImage.query.filter_by(id=id).first()
    
    favorite = Favorite(user_id=current_user.id, product_id=product.id)
    db.session.add(favorite)
    db.session.commit()
    
    return redirect(url_for("market.shop"))

@market.route("/wishList", methods=["GET", "POST"])
@login_required
def wishList():
    # お気に入りを取得
    user_id = current_user.id
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    products = []
    for favorite in favorites:
        product = UserImage.query.filter_by(id=favorite.product_id).first()
        if product not in products:
            products.append(product)
        else:
            pass
    return render_template("market/wishlist.html", products=products)

@market.route("/wishList/delete/<int:id>", methods=["GET", "POST"])
def deleteWishList(id):
    favorite = Favorite.query.filter_by(user_id = current_user.id, product_id=id).first()
    db.session.delete(favorite)
    db.session.commit()
    return redirect(url_for("market.wishList"))


@market.route("/search/<string:search>", methods=["GET"])
def search(search):
    search = request.args.get(search)
    
    products = UserImage.query.filter(UserImage.image_name.like("%" + str(search) + "%")).order_by(UserImage.id.desc()).all()
    # categories = UserImage.query.filter(UserImage.category.like("%" + search + "%")).order_by(UserImage.id.desc()).all()
    
    return render_template("market/history.html", products=products)
