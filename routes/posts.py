from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.models.user_and_posts import Posts, User, Like
from flask_login import current_user

posts_route = Blueprint ('posts', __name__)

@posts_route.route('/add_post', methods = ['POST'])
def create_post():
    """Function to create a new post"""

    new_post = Posts.create(
        username= current_user,
        post_title=request.form['post_title'],
        content=request.form['content'],
    )
    
    return redirect(url_for('home_page.home'))

@posts_route.route('/delete_post/<int:post_id>', methods = ['POST'])
def delete_post(post_id):
    """Function to delete a post"""
    post = Posts.get_or_none(Posts.id == post_id)
    if post:
        Like.delete().where(Like.post == post).execute()
        post.delete_instance()
        flash("Post deleted with successfully", "success") #message of success
    else:
        flash("You can't delete this post!", "error") # message of error
    return redirect(url_for('home_page.home'))

@posts_route.route('/edit_post/<int:post_id>', methods = ['GET'])
def edit_post(post_id):
    """Function to renderize the form for edit a post"""
    post = Posts.get_or_none (Posts.id == post_id)

    if posts is None:
        flash("Post not found", "error")
        return redirect (url_for('home_page.home'))

    return render_template ('form_edit.html', post=post)


@posts_route.route('/update_post/<int:post_id>', methods = ['POST'])
def update_post(post_id):
    """Function to update a post, here the code actualize the info of the post"""
    print(f"Atualizando o post {post_id}")
    post = Posts.get_by_id(post_id)
    if request.method == 'POST':
        post.post_title = request.form ['post_title']
        post.content = request.form ['content']
        post.save()
        flash("Post updated with succesfully", "success")
        return redirect(url_for('home_page.home'))

@posts_route.route('/like_post/<int:post_id>', methods = ['POST'])
def like_system(post_id):
    user = current_user

    post = Posts.get_or_none(Posts.id == post_id)
    if not post:
        flash("Post not found", "error")
        return redirect(url_for('home_page.home'))

    like_exists = Like.select().where((Like.user == user.id) & (Like.post == post.id)).exists()

    if like_exists:
        Like.delete().where((Like.user == user.id) & (Like.post == post.id)).execute()
        post.likes -=1
    else:
        Like.create(user = user, post = post)
        post.likes += 1

    post.save()

    return redirect(url_for('home_page.home'))


