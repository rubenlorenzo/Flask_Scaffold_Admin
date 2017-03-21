from flask import Flask
import os
from flask_mail import Mail
from flask_uploads import UploadSet, IMAGES, configure_uploads

app = Flask(__name__)

# Setup config
from app.settings import ConfigClass
app.config.from_object(__name__+'.ConfigClass')

from app.settings import CreateAdminUser
app.config.from_object(__name__+'.CreateAdminUser')

# Upload photos config
uploaded_photos = UploadSet('photos', IMAGES)
configure_uploads(app, uploaded_photos)

# Initialize Flask-Mail
mail = Mail(app)

# Load Blueprints
from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')

from .home import home as home_blueprint
app.register_blueprint(home_blueprint, url_prefix='/home')


#Views
from . import views

# Start server
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
