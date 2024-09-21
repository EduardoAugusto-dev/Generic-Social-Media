from flask import Blueprint, render_template, redirect, url_for
from database.models.user_and_posts import Posts

home_route = Blueprint('home_page', __name__)

@home_route.route("/")
def initial_screen():
    return redirect (url_for('login.register'))

@home_route.route("/home")
def home():
    """This function list every posts"""
    posts = Posts.select()
    return render_template('index.html', posts=posts)
