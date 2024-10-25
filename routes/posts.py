from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.models.user_and_posts import Posts, User, Like, PostForm
from flask_login import current_user
from werkzeug.utils import secure_filename
import os

posts_route = Blueprint ('posts', __name__)

from main import app 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@posts_route.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.post_title.data
        content = form.content.data
        image = form.image.data
        image_path = None
        if image:
            filename = secure_filename(image.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(filepath)
            image_path = 'uploads/' + filename  # Garantir que o caminho seja `uploads/nome_do_arquivo`
        print(f'Creating post: Title={title}, Content={content}, ImagePath={image_path}')
        new_post = Posts.create(user=current_user, post_title=title, content=content, image_path=image_path)
        flash('Post created successfully', 'success')
        return redirect(url_for('home'))
    if form.errors:
        flash(f'Error: {form.errors}', 'error')
    posts = Posts.select()
    return render_template('index.html', posts=posts, form=form)

@posts_route.route('/delete_post/<int:post_id>', methods = ['POST'])
def delete_post(post_id):
    """Function to delete a post"""

    post = Posts.get_or_none(Posts.id == post_id)

    if post.user.id != current_user.id:
        flash ("You can't exclude a post who are not yours!", "danger")
    else:
        Like.delete().where(Like.post == post).execute()
        post.delete_instance()
        flash("Post deleted with successfully", "success") #message of success
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

    if post.user.id != current_user.id:
        flash ("You can't edit a post who are not yours!", "danger")

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


