from flask import render_template,url_for , redirect, request, flash
from flask_user import current_user
from . import home

#Root - route
@home.route('/')
def home_page():
    return redirect(url_for('home.city_page'))

#Explore - route
@home.route('/city')
def city_page():
    return render_template('city_page.html', blueprint_title="Home", title="City")

#About - route
@home.route('/about')
def about_page():
    return render_template('about_home_page.html', blueprint_title="Home", title="About")
