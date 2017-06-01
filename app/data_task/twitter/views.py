from flask import render_template
from flask_user import login_required, confirm_email_required, roles_required, current_user
from . import twitter
from .models import CredentialsTwitter


@twitter.route('/')
@login_required
@confirm_email_required
@roles_required('admin')
def source_options_page():
    credentialsTwitter=CredentialsTwitter()
    return render_template('twitter_options_page.html', blueprint_title="Admin", title="Data Task", subtitle="twitter" , source="twitter", description=str(credentialsTwitter))
