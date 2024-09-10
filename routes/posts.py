from flask import Blueprint, render_template, request, redirect, url_for
from database.models.user_and_posts import Posts, User

posts_route = Blueprint ('posts', __name__)

@posts_route.route('/add', methods = ['POST'])
def create_post():
    """Function to create a new post"""

    user, created = User.get_or_create(
        user = 'default_user',
        defaults = {'email': 'default@example.com', 'password': '12345'}
    )

    new_post = Posts.create(
        username=user,
        post_title=request.form['post_title'],
        content=request.form['content'],
    )
    
    return redirect(url_for('home_page.home'))
