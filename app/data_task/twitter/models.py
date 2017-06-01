from ..base_models import Credentials
from .. import db

class CredentialsTwitter(Credentials, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(100), nullable=False, unique=True)
    token_secret =db.Column(db.String(100), nullable=False, unique=True)
    consumer_key = db.Column(db.String(100), nullable=False, unique=True)
    consumer_secret = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self):
        self.provider="twitter"
        Credentials.__init__(self, self.provider)
