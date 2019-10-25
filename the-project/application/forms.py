from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#inherting FlaskForm class

class UserRegistrationForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired("Too short"),Length(min=2, max=20) ])          #other arguments are constraints
    secondName = StringField('Second Name', validators=[DataRequired(),Length(min=2, max=20) ])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(message="Please Enter a Password")])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')


class UserLoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])          #other arguments are constraints
    password = PasswordField('Password',validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RehomeForm(FlaskForm):

    petName = StringField('What is the name of the pet you are rehoming?', validators=[Length(min=2, max=20) ])          #other arguments are constraints
    petType = StringField('What species of animal is your pet?',validators=[Length(min=2, max=20)])
    petAge = IntegerField('How old is your pet? (Please put an integer. If you are unsure, guess)', validators=[])
    petDesc = StringField('Tell us anything you want to tell us about your pet (personality, special needs, etc), limit 400 characters:',validators=[Length(min=0, max=400)])
    petContact = StringField('Please leave a phone number or email address (or both) for us to contact you:',validators=[Length(min=0, max=80)])
    submit = SubmitField('Add')