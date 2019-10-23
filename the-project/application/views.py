#views.py

from flask import render_template,url_for, flash, redirect, request
from application import app,db

from application.forms import UserRegistrationForm,UserLoginForm
from application.models import Pet, User, Product
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import login_user, current_user, logout_user,login_required





admin = Admin(app)
## ADMIN VIEWS ####

class adminModelView(ModelView):
    pass

admin.add_view(adminModelView(Pet,db.session))
admin.add_view(adminModelView(User,db.session))
admin.add_view(adminModelView(Product,db.session))


@app.route('/')
@app.route('/home')

def home():
    #return render_template('home.html',posts=post)
    return render_template('home.html',title="Home")

@app.route('/about')
@login_required
def about():
    return render_template('about.html',title="About")

@app.route('/register', methods=['GET','POST'])

def register():
    form  = UserRegistrationForm()
    if form.validate_on_submit():
        user = User(firstName=form.firstName.data,secondName=form.secondName.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash(f'Account created for {form.firstName.data} {form.secondName.data}!','success') #put in layout template that the flash messages show
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',form=form)


@app.route('/login', methods=['GET','POST'])

def login():
    form  = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # show Austin how to debug (form.data.password)
        if user and (user.password == form.password.data):
            login_user(user)
            flash(f'Logged in {user.firstName} {user.secondName}!','success') #put in layout template that the flash messages show
            return redirect(url_for('home'))
    return render_template('login.html', title='Login',form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/petAdd', methods=['GET','POST'])

def petAdd():
    pets = Pet.query.all()
    return render_template('petTable.html',title='pet', pets=pets)



@app.route('/productAdd', methods=['GET','POST'])

def productAdd():
    products = Product.query.all()
    return render_template('productTable.html',title='product', products=products)
