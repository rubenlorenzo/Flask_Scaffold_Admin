from flask import render_template,url_for , redirect, request, flash
from flask_user import current_user
from . import home

#Root - route
@home.route('/')
def home_page():
    return redirect(url_for('home.content_page'))

#Explore - route
@home.route('/content')
def content_page():
    return render_template('content_page.html', blueprint_title="Home", title="Content")

#About - route
@home.route('/about')
def about_page():
    return render_template('about_home_page.html', blueprint_title="Home", title="About")
