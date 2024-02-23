
from flask import FlaskForm
from forms import StringField, PasswordField, BooleanField, SubmitField

class RegistrationForm(FlaskForm):
    username = FlaskForm.StringField('Username',
