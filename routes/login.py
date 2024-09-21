from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from database.models.user_and_posts import User, LoginForm, RegistrationForm
from extensions import bcrypt, login_manager

login_route = Blueprint('login', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.get_or_none(User.id == int(user_id))

@login_route.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Username: {form.username.data}") 
        print(f"Password: {form.password.data}") 
        user = User.get_or_none(User.username == form.username.data)
        if user:
            print(f"Stored Hash: {user.password}")
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('home_page.home')) 
    return render_template('login.html', form=form)

@login_route.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(username=form.username.data, password=hashed_password)
        new_user.save()
        return redirect(url_for('login.login'))
    return render_template('register.html', form=form)

@login_route.route('/logout', methods =['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.login'))

