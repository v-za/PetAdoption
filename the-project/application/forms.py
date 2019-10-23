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

class petForm(FlaskForm):

    petName = StringField('Name', validators=[Length(min=2, max=20) ])          #other arguments are constraints
    petType = StringField('Type',validators=[Length(min=2, max=20)])
    petAge = IntegerField('Age', validators=[])
    submit = SubmitField('Add')

class productForm(FlaskForm):

    productName = StringField('Name', validators=[Length(min=2, max=40)])          #other arguments are constraints
    productType = StringField('Type',validators=[Length(min=2, max=20)])
    productDesc = StringField('Description',validators=[Length(min=2, max=400)])
    productPrice = IntegerField('Price', validators=[])
    productInStock = IntegerField('Stock', validators=[])
    submit = SubmitField('Add')

class petFormDel(FlaskForm):
    id = IntegerField('ID', validators=[])
    delete = SubmitField('Delete')

class productFormDel(FlaskForm):
    id = IntegerField('ID', validators=[])
    delete = SubmitField('Delete')