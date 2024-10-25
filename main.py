from flask import Flask
import os
from extensions import bcrypt, login_manager


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login.login"
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')


if __name__ == '__main__':
    from config import general_config
    general_config(app)
    app.run(debug=True, port=5001)
