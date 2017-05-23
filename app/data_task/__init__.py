from app import app
from flask import Blueprint

# Blueprint
data_task = Blueprint('data_task', __name__, template_folder='./templates', static_folder="./static", static_url_path="/static")

# Views
from . import views
