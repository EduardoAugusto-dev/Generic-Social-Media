from peewee import SqliteDatabase

db_users = SqliteDatabase('usermanager.db')

db_posts = SqliteDatabase('postsmanager.db')

db_like = SqliteDatabase('likemanager.db')