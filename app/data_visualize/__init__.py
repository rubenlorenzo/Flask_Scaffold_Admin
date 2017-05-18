from app import app
from flask import Blueprint

# Blueprint
data_visualize_admin = Blueprint('data_visualize_admin', __name__, template_folder='./templates', static_folder="./static", static_url_path="/static")

# Views
from . import views
