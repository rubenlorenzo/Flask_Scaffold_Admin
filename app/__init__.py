from flask import Flask
import os
from flask_mail import Mail


app = Flask(__name__)



#Setup config
from app.settings import ConfigClass
app.config.from_object(__name__+'.ConfigClass')

from app.settings import CreateAdminUser
app.config.from_object(__name__+'.CreateAdminUser')

mail = Mail(app)                                # Initialize Flask-Mail

# Load Blueprints
from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint, url_prefix='/admin')

# Start server
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
