from peewee import Model, CharField, DateTimeField, ForeignKeyField, TextField, IntegerField
from database.database import db_users, db_posts, db_like
import datetime

# User model
class User(Model):
    user = CharField(max_length=30)
    email = CharField(max_length=40)
    password = CharField(max_length=40)
    register_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_users  

# Posts model
class Posts(Model):
    username = ForeignKeyField(User)
    post_title = TextField()
    content = TextField()
    date_of_post = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_posts  
        order_by = ('-date_of_post',)


class Like(Model):
    user = ForeignKeyField(User, backref='likes')
    post = ForeignKeyField(Posts, backref='likes')
    indexes = (
        (('user','post'), True), 
    )

    class Meta:
        database = db_like

