from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    current_app,
    send_from_directory,
)
from flask_login import current_user, login_required

original = Blueprint(
    "original", __name__, template_folder="templates", static_folder="static"
)


@original.route("/design")
def design():
    return render_template("original/design.html")


@original.route("/fashion")
@login_required
def fashion():
    return render_template("original/fashionevent.html")


@original.route("/weather")
def weather():
    return render_template("original/APItest.html")


@original.route("/styling")
def styling():
    return render_template("original/styling.html")


@original.route("/fashontest")
def fashontest():
    return render_template("original/fashiontest.html")
