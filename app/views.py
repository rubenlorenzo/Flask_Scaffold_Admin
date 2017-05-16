from app import app
from flask import render_template,url_for , redirect, request, flash
from flask_user import current_user
from app.home import home

#Root - route
@app.route('/')
def home_page():
    return redirect(url_for('home.home_page'))
