from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")

@views.route("/pets")
def pets():
    return render_template("pets.html")

@views.route("/shop")
def shop():
    return render_template("shop.html")
