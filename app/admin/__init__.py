from app import app
import os
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, SQLAlchemyAdapter
from flask import Blueprint


# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Load and create Models Database
from .models import User, Role
db.create_all()

# Add User to Flask-User
db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)

# Create user admin default
if not User.query.filter(User.username==os.getenv('ADMIN_USER')).first():
        user1 = User(username=os.getenv('ADMIN_USER'), email=os.getenv('ADMIN_EMAIL'), active=True,
                password=user_manager.hash_password(os.getenv('ADMIN_PASSWORD')))
        user1.roles.append(Role(name='admin'))
        db.session.add(user1)
        db.session.commit()

# Blueprint
admin = Blueprint('admin', __name__, template_folder='./templates')

# Views
from . import views
