from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
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
    name = StringField('Pet Name',validators=[DataRequired()])          #other arguments are constraints
    type = StringField('Pet Type',validators=[DataRequired()])
    breed = StringField('Pet Breed',validators=[DataRequired()])
    gender = StringField('Pet Gender',validators=[DataRequired()])
    age = IntegerField('Pet Age',validators=[DataRequired()])
    weight = IntegerField('Pet Weight',validators=[DataRequired()])
    picture = FileField('Profile Picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Send Request')
