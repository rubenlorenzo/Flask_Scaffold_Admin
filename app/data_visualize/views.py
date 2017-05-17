from flask import render_template
from flask_user import login_required, confirm_email_required, roles_required, current_user
from ..admin import admin
from . import data_visualize

# Root - route
@admin.route('/data_visualize')
@login_required
@confirm_email_required
@roles_required('admin')
def data_visualize_admin():
    return render_template('data_visualize_admin.html', blueprint_title="Admin", title="Data Visualize")
