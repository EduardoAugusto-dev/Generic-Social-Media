from routes.home import home_route
from routes.user import user_route
from routes.posts import posts_route
from routes.login import login_route
from database.database import db_users, db_posts
from database.models.user_and_posts import User, Posts


def general_config(app):
    routes_config(app)
    db_config()

def routes_config(app):
    #routes
    app.register_blueprint(home_route)
    app.register_blueprint(user_route, url_prefix = '/user' )
    app.register_blueprint(posts_route, url_prefix = '/posts')
    app.register_blueprint(login_route, url_prefix = '/login')

def db_config():
    db_posts.connect()
    db_users.connect()
    db_users.create_tables([User])
    db_posts.create_tables([Posts])