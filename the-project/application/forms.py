from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
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


class AdoptionAddForm(FlaskForm):
    name = StringField('What is the name of the pet you are rehoming? (required)',validators=[DataRequired()])          #other arguments are constraints
    type = StringField('What species of animal is your pet? (required)',validators=[DataRequired()])
    breed = StringField('Do you know the breed of your pet? If so, put it here.')
    gender = StringField('Is your pet male or female?')
    age = IntegerField('How old is your pet? (Please put an integer. If you are unsure, you can guess)')
    description = StringField('Tell us anything else you want to tell us about your pet (personality, special needs, etc)')
    contact = StringField('Please leave a phone number or email address (or both) for us to contact you (required):', validators=[DataRequired()])
    picture = FileField('Upload a pic of your pet', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Send Request')
