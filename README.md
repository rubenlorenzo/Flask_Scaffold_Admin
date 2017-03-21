Next steps
----------

-	git clone
-	virtualenv -p /usr/bin/python2.7 venv
-	. venv/bin/activate
-	pip2.7 install -r requirements.txt
-	rename *app/config_example.py* to *config.py* and add values
-	export FLASK_APP=app/\__init\__.py
-	export FLASK_DEBUG=1
-	flask run
