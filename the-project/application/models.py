##from application import db
from application import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20),nullable=False)
    secondName = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(50),nullable=False)


    def __repr__(self):
        return f"User('{self.firstName}', '{self.secondName}', '{self.email}')"



class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petName = db.Column(db.String(20))
    petType = db.Column(db.String(20),nullable=False)
    petAge = db.Column(db.Integer,nullable=False)
    #petImage =

#method for how our object is printed when printeed out
    def __repr__(self):
        return f"Pet('{self.petName}','{self.petType}','{self.petAge}')"
