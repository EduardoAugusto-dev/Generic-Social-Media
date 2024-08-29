from peewee import Model, CharField, DateTimeField, ForeignKeyField, TextField
from database.database import db_users, db_posts
import datetime

# User model
class User(Model):
    username = CharField(max_length=30)
    email = CharField(max_length=40)
    password = CharField(max_length=40)
    register_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db_users  

# Posts model
class Posts(Model):
    username = ForeignKeyField(User)
    content = TextField()
    date_of_post = DateTimeField(default=datetime.datetime.now)
    image_url = CharField(null=True)

    class Meta:
        database = db_posts  
        order_by = ('-date_of_post',)
