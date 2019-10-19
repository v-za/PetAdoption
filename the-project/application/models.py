##from application import db
from application import db



class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petName = db.Column(db.String(20))
    petType = db.Column(db.String(20),nullable=False)
    petAge = db.Column(db.Integer,nullable=False)
    #petImage =

#method for how our object is printed when printeed out
    def __repr__(self):
        return f"Pet('{self.petName}','{self.petType}','{self.petAge}')"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    petName = db.Column(db.String(20))
    petType = db.Column(db.String(20),nullable=False)
    petAge = db.Column(db.Integer,nullable=False)
