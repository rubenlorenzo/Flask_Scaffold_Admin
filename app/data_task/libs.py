from .base_models import Credentials
from .twitter.models import CredentialsTwitter
from .twitter.forms import CredentialsTwitterForm

def credentials_generate(source):
    credentials = Credentials("none")

    if source == "twitter":
        credentials = CredentialsTwitter()

    return credentials

def credentials_form_generate(source):
    credentials_form = "none"

    if source == "twitter":
        credentials_form = CredentialsTwitterForm()

    return credentials_form

def template_options(source):
    template = "source_options_page.html"

    if source == "twitter":
        template = 'twitter_options_page.html'

    return template
