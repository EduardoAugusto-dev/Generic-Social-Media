from flask import Flask
import os
from config import general_config
from extensions import bcrypt, login_manager

app = Flask(__name__)

bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login.login"

app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

general_config(app)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
