from flask import render_template
from flask_user import login_required, confirm_email_required, roles_required, current_user
from ..admin import admin
from . import data_visualize_admin

# Root - route
@data_visualize_admin.route('/')
@login_required
@confirm_email_required
@roles_required('admin')
def channels_page():
    return render_template('admin/channels_visualize_page.html', blueprint_title="Admin", title="Data Visualize")

@data_visualize_admin.route('/<channel>')
@login_required
@confirm_email_required
@roles_required('admin')
def channel_options_page(channel):
    return render_template('admin/channel_options_page.html', blueprint_title="Admin", title="Data Visualize", subtitle=channel , channel=channel)
