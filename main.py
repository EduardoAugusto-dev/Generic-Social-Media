from flask import Flask
import os
from config import general_config

#init flask
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

general_config(app)

app.run(debug=True, port = 5001)

