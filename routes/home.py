from flask import Blueprint, render_template

home_route = Blueprint ('home_page', __name__)

@home_route.route("/")
def home():
    return render_template ('index.html')