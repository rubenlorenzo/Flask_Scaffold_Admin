from flask import Blueprint
from ...admin import db

# Blueprint
twitter = Blueprint('twitter', __name__, template_folder='./templates', static_folder="./static", static_url_path="/static")

from .models import CredentialsTwitter
db.create_all()

from . import views
