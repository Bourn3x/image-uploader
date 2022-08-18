from flask import Flask
from routes import configure_routes

UPLOAD_FOLDER = 'static/images'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
configure_routes(app)
