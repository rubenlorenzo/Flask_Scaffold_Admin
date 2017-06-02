from flask import render_template, redirect, request
from flask_user import login_required, confirm_email_required, roles_required, current_user
from ..admin import admin
from . import data_task
from .libs import credentials_generate, credentials_form_generate, template_options

# Root - route
@data_task.route('/')
@login_required
@confirm_email_required
@roles_required('admin')
def sources_page():
    return render_template('sources_page.html', blueprint_title="Admin", title="Data Task")

@data_task.route('/options/<source>')
@login_required
@confirm_email_required
@roles_required('admin')
def source_options_page(source):
    credentials = credentials_generate(source)
    form_credentials = credentials_form_generate(source)

    # Process valid POST - form_credentials_twitter
    if request.method == 'POST' and form_credentials.validate():
        form_credentials.populate_obj(credentials)

        # Save credentials_twitter
        db.session.commit()

    return render_template(template_options(source), blueprint_title="Admin", title="Data Task", subtitle=source , source=source, description=str(credentials), form_credentials=form_credentials)
