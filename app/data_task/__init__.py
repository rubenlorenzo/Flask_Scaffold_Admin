from app import app
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Blueprint
data_task = Blueprint('data_task', __name__, template_folder='./templates', static_folder="./static", static_url_path="/static")

from .twitter import twitter as twitter_blueprint
def register_sub_blueprint_data_task(app, url_prefix_parent="/admin/data_task"):
    app.register_blueprint(twitter_blueprint, url_prefix=url_prefix_parent+"/twitter")

register_sub_blueprint_data_task(app)

# Views
from . import views
