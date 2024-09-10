from flask import Blueprint, render_template
from database.models.user_and_posts import Posts

home_route = Blueprint('home_page', __name__)

@home_route.route("/")
def home():
    """This function list every users"""
    posts = Posts.select()
    print(f"Number of posts: {posts.count()}") 
    return render_template('index.html', posts=posts)
