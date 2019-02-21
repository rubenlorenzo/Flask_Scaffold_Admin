# Flask Scaffold Admin
A Flask scaffold project with interface admin, using Flask-User.

## Install

```bash
git clone https://github.com/rubenlorenzo/Flask_Scaffold_Admin.git
cd Flask_Scaffold_Admin

#You must have install virtualenv
virtualenv venv
. venv/bin/activate

pip install -r requirements.txt

#Modify archive
mv app/config_example.py  app/config.py 

FLASK_APP=app/__init__.py flask run
```

## Demo
Small demo video:

[![demo - video](https://i.vimeocdn.com/video/760818806_640x564.jpg)](https://vimeo.com/318413412)