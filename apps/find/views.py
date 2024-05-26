from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from apps.detector.models import UserImage, Color, CategoryName, Condition, Size, Favorite
from apps.app import db

search = Blueprint("search", __name__, template_folder="templates")

@search("/", methods=["GET"])
def search():
    if request.method == "GET":
        keyword = request.args.get()
        products = UserImage.query.filter(UserImage.name.like("%{}%".format(keyword))).all()
        return render_template("market/shop-sidebar.html", products=products)
    else:
        return redirect(url_for("market.shop"))
