from app import app
from flask import Blueprint

# Blueprint
data_visualize = Blueprint('data_visualize', __name__, template_folder='./templates', static_folder="./static", static_url_path="/static")

# Views
from . import views
