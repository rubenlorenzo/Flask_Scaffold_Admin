from ..admin import db
from .base_models import Credentials
from .twitter.models import CredentialsTwitter
from .twitter.forms import CredentialsTwitterForm


def credentials_generate(source):
    credentials = Credentials("none")

    if source == "twitter":
        credentials = CredentialsTwitter()

    return credentials


def get_credentials(source, user_id):
    credentials = credentials_generate(source)

    if source == "twitter":
        credentials = db.session.query(CredentialsTwitter).filter(CredentialsTwitter.user_id == user_id).first()

    if credentials is None:
        credentials = credentials_generate(source)
    return credentials


def credentials_form_generate(source):
    credentials_form = "none"

    if source == "twitter":
        credentials_form = CredentialsTwitterForm()

    return credentials_form
