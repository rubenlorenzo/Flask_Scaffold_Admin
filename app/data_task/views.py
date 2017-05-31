from flask import render_template, redirect
from flask_user import login_required, confirm_email_required, roles_required, current_user
from ..admin import admin
from . import data_task
from . import twitter

# Root - route
@data_task.route('/')
@login_required
@confirm_email_required
@roles_required('admin')
def sources_page():
    return render_template('sources_page.html', blueprint_title="Admin", title="Data Task")

@data_task.route('/<source>')
@login_required
@confirm_email_required
@roles_required('admin')
def source_options_page(source):
    if  source == "twitter" :
        redirect(url_for('twitter.source_options_page'))
    return render_template('source_options_page.html', blueprint_title="Admin", title="Data Task", subtitle=source , source=source)
