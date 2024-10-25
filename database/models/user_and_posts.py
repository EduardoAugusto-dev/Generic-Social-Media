from peewee import Model, CharField, DateTimeField, ForeignKeyField, TextField, IntegerField
from database.database import db_users, db_posts, db_like
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from flask_login import UserMixin
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError, Email, DataRequired
import datetime


class PostForm(FlaskForm):
    title = StringField('Title of post', validators=[DataRequired(), Length(max=100)], render_kw={"placeholder": "Title"})
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"placeholder": "Content"})
    image = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Just images are permitted.')])
    submit = SubmitField('Create Post')

class User(Model, UserMixin):
    id = IntegerField(primary_key=True)
    username = CharField(max_length=30, unique= True)
    password = CharField(max_length=40)
    register_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_users  

# Posts model
class Posts(Model):
    user = ForeignKeyField(User, backref='posts')
    post_title = TextField()
    content = TextField()
    date_of_post = DateTimeField(default=datetime.datetime.now)
    image_path = CharField(null=True)
    class Meta:
        database = db_posts
        order_by = ('-date_of_post',)
# Like system model
class Like(Model):
    user = ForeignKeyField(User, backref='likes')
    post = ForeignKeyField(Posts, backref='likes')
    indexes = (
        (('user','post'), True), 
    )

    class Meta:
        database = db_like

# Registration model

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired(), Length(
    min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField('Password',validators=[InputRequired(), Length(
    min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField ("Register")

    def validate_username(self, username):
        existing_user_username = User.get_or_none(User.username == username.data)
        if existing_user_username:
            raise ValidationError("That username already exists. Please choose a different one.")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
    min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
    min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField ("Login")