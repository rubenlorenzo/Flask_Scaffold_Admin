from ..base_models import Credentials
from . import db

class CredentialsTwitter(Credentials, db.Model):
    __tablename__='credentials_twitter'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(100), nullable=False, unique=True)
    token_secret =db.Column(db.String(100), nullable=False, unique=True)
    consumer_key = db.Column(db.String(100), nullable=False, unique=True)
    consumer_secret = db.Column(db.String(100), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self):
        self.provider="twitter"
        Credentials.__init__(self, self.provider)

    def add_credentials(self, token, token_secret,consumer_key,consumer_secret):
        self.token=token
        self.token_secret=token_secret
        self.consumer_key=consumer_key
        self.consumer_secret=consumer_secret
