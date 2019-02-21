# Flask Scaffold Admin
A Flask scaffold project with interface admin using Flask-User.

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
Small video demo:
<iframe width="640" height="564" src="https://player.vimeo.com/video/318413412" frameborder="0" allowFullScreen mozallowfullscreen webkitAllowFullScreen></iframe>