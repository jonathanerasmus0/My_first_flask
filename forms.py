
from flask import FlaskForm
from forms import StringField, PasswordField, BooleanField, SubmitField
from forms import validate_username, validate_datarequired,length_of_username
from forms import validate_email, validate_password,equal_to

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators={validate_datarequired(),length_of_username(min=2, max=20)})
    email = StringField('Email', validators=[validate_email()])
    password = PasswordField('Password', validators=[validate_password,validate_datarequired()])
    confirm_password = PasswordField('<PASSWORD>', validators=[validate_password,validate_datarequired, equal_to('PASSWORD')])
    submit = SubmitField('log in')
    
    
class loginForm(FlaskForm):
   
    email = StringField('Email', validators=[validate_email()])
    password = PasswordField('Password', validators=[validate_password,validate_datarequired()])
    remember = BooleanField('Remember Me') #why BooleanField? Becuase it is a checkbox which requires true/false values
    submit = SubmitField('log in')
    
