from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField,StringField, BooleanField, FormField, validators

class CredentialsTwitterForm(FlaskForm):
    token = StringField('Token', validators=[
        validators.DataRequired('Token is required')])
    token_secret = StringField('Token Secret', validators=[
        validators.DataRequired('Token Secret is required')])
    consumer_key = StringField('Consumer Key', validators=[
        validators.DataRequired('Consumer Key is required')])
    consumer_secret = StringField('Consumer Secret', validators=[
        validators.DataRequired('Consumer Secret is required')])
    submit = SubmitField('Save')
