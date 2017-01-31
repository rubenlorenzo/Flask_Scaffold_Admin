

from flask import Flask
import os
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager, SQLAlchemyAdapter

app = Flask(__name__)

#Setup config
from app.settings import ConfigClass
app.config.from_object(__name__+'.ConfigClass')

from app.settings import CreateAdminUser
app.config.from_object(__name__+'.CreateAdminUser')

# Initialize Flask extensions
db = SQLAlchemy(app)                 # Initialize Flask-SQLAlchemy
mail = Mail(app)                                # Initialize Flask-Mail

# Load and create Models Database
from app.models import User, Role
db.create_all()

#Add User to Flask-User
db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)

# Create user admin default
if not User.query.filter(User.username==os.getenv('ADMIN_USER')).first():
        user1 = User(username=os.getenv('ADMIN_USER'), email=os.getenv('ADMIN_EMAIL'), active=True,
                password=user_manager.hash_password(os.getenv('ADMIN_PASSWORD')))
        user1.roles.append(Role(name='admin'))
        db.session.add(user1)
        db.session.commit()

# Load views
from app import views

# Start server
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
