from flask import Blueprint, render_template, request
from database.models.user_and_posts import Posts

posts_route = Blueprint ('posts', __name__)

@posts_route.route("/posts")
def post_list():
    """This function list every users"""
    posts = Posts.select()
    return render_template('post_list.html', posts = posts)

@posts_route.route("/post")
def create_post():
    """This function create a post"""
    
    title = request.form.get('title')
    content = request.form.get('content')

    new_post = Posts.create(
        username = data['username'],
        content = data['content'],
        date_of_post = data['date_of_post'],
        
     )
     
    return render_template('post_creation', posts = new_post)
    

