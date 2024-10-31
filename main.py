from flask import Flask, send_from_directory
import os
from extensions import bcrypt, login_manager


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
bcrypt.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login.login"
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    from config import general_config
    general_config(app)
    app.run(debug=True, port=5001)
