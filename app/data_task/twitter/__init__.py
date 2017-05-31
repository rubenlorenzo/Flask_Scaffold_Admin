from flask import Blueprint

# Blueprint
twitter = Blueprint('twitter', __name__, template_folder='./templates', static_folder="./static", static_url_path="/static")

from . import views
