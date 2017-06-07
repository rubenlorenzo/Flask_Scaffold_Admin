from flask import render_template, redirect, request
from flask_user import login_required, confirm_email_required, roles_required, current_user
from ..admin import admin
from . import data_task
from .libs import credentials_generate, credentials_form_generate, template_options, get_credentials
from ..admin import db

# Root - route
@data_task.route('/')
@login_required
@confirm_email_required
@roles_required('admin')
def sources_page():
    return render_template('sources_page.html', blueprint_title="Admin", title="Data Task")

@data_task.route('/options/<source>', methods=['GET','POST'])
@login_required
@confirm_email_required
@roles_required('admin')
def source_options_page(source):

    credentials = get_credentials(source, current_user.id)
    form_credentials = credentials_form_generate(source)

    # Process valid POST - form_credentials_twitter
    if request.method == 'POST' and form_credentials.validate():
        form_credentials.populate_obj(credentials)
        credentials.set_user_id(current_user.id)

        # Save credentials_twitter
        db.session.add(credentials)
        db.session.commit()

    return render_template(source+'_options_page.html', blueprint_title="Admin", title="Data Task", subtitle=source , source=source, credentials=credentials, form_credentials=form_credentials)
