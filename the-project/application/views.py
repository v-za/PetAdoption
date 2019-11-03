#views.py
import os
import secrets
from flask import render_template,url_for, flash, redirect, request, abort
from application import app,db

from application.forms import UserRegistrationForm, UserLoginForm, AdoptionAddForm, UpdateUserDetailsForm,UpdateUserPasswordForm
from application.models import Pet, User, Product
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import login_user, current_user, logout_user, login_required





admin = Admin(app)
## ADMIN VIEWS ####

class adminModelView(ModelView):
    pass

admin.add_view(adminModelView(Pet,db.session))
admin.add_view(adminModelView(User,db.session))
admin.add_view(adminModelView(Product,db.session))

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404


@app.route('/')
@app.route('/home')

def home():
    #return render_template('home.html',posts=post)
    return render_template('home.html',title="Home")

@app.route('/about')

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


@app.route('/adopt', methods=['GET','POST'])
def adopt():
    pets = Pet.query.all()
    return render_template('petTable.html',title='pet', pets=pets)


@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form = UpdateUserDetailsForm()
    #form2 = UpdateUserPasswordForm()
    if form.validate_on_submit():
        current_user.firstName = form.firstName.data

        current_user.secondName = form.secondName.data

        current_user.email = form.email.data

        db.session.commit()
        return redirect(url_for('account'))
    elif request.method == 'GET':
        current_user.firstName = current_user.firstName

        current_user.secondName = current_user.secondName

        current_user.email = current_user.email

    return render_template("account.html",title=current_user.firstName + "'s Account", form=form)

@app.route('/productAdd', methods=['GET','POST'])

def productAdd():
    products = Product.query.all()
    return render_template('productTable.html',title='product', products=products)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/animal_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn

@app.route("/adoptionAdd", methods=['GET','POST'])
def adoptionAdd():
    form = AdoptionAddForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            pet = Pet(petName=form.name.data,petType=form.type.data, petGender = form.gender.data, petBreed=form.breed.data, petAge=form.age.data, petWeight=form.weight.data, petImage=picture_file)
        else:
            pet = Pet(petName=form.name.data,petType=form.type.data, petGender = form.gender.data, petBreed=form.breed.data, petAge=form.age.data, petWeight=form.weight.data)
        db.session.add(pet)
        db.session.commit()
        flash(f'Application Has Been Sent for {form.name.data}!','success')
        return redirect(url_for('adoptionAdd'))
    return render_template('adoptionAdd.html',title='Add Pet', form=form)


@app.route("/petAdd/<petID>")
def adoptInfo(petID):
    if bool(Pet.query.filter_by(id=petID).first()):
        pet = Pet.query.filter_by(id=petID).first()
        return render_template('adoptInfo.html',title='Pet Info', pet=pet)
    else:
        abort(404)
