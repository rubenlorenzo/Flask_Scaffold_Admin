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
## home
from .home import home as home_blueprint
app.register_blueprint(home_blueprint, url_prefix='/home')

## admin
from .admin import admin as admin_blueprint, register_sub_blueprint_admin
app.register_blueprint(admin_blueprint, url_prefix='/admin')

register_sub_blueprint_admin(app)

# Views
from . import views

## Celery
from celery import Celery
import time
def make_celery(app):
    celery = Celery(app.import_name,  backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

app.config.update(
    CELERY_BROKER_URL='redis://redis:6379',
    CELERY_RESULT_BACKEND='redis://redis:6379'
)
celery = make_celery(app)

@celery.task(bind=True)
def task_normal(self):
    for i in range(1,10):
        print i
        time.sleep(2)

@app.route('/task')
def task_n():
    task = task_normal.apply_async()
    return "task_normal"

#####

# Start server
if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
