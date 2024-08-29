from flask import Flask
from config import general_config

#init flask
app = Flask(__name__, static_url_path='/static')

general_config(app)

app.run(debug=True, port = 5001)

