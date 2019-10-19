#views.py

from flask import render_template,url_for, flash, redirect, request
from application import app,db
from application.forms import UserRegistrationForm,petForm,petFormDel
from application.models import Pet





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
        #flash('Account created!','success') #put in layout template that the flash messages show
        return redirect(url_for('home'))
    return render_template('register.html', title='Register',form=form)


# @app.route('/petTable', methods=['GET','POST'])
#
# def petTable():
#     pets = Pet.query.all()
#     return render_template('petTable.html',title="Pet Database",pets=pets)



@app.route('/petAdd', methods=['GET','POST'])


def petAdd():
    form = petForm()
    formDel= petFormDel()
    pets = Pet.query.all()


    if form.validate_on_submit() and form.submit.data:
        print("HELLO SUBMIT")
        pet = Pet(petName=form.petName.data, petType=form.petType.data, petAge=form.petAge.data)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('petAdd'))

    if formDel.validate_on_submit() and formDel.delete.data:
            print("HELLO DELETE")
            id = int(formDel.id.data)
            db.session.delete(Pet.query.get(id))
            db.session.commit()
            return redirect(url_for('petAdd'))




    return render_template('petAdd.html',title='petAdd',form=form,formDel=formDel, pets=pets)








# @app.route('/login')
#
# def login():
#     form  = UserLoginForm()
#     return render_template('login.html', title='Login',form=form)
