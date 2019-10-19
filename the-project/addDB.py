#for adding into DATABASE
from application import db
from application.models import Pet

'''
simply adding into Pet DATABASE

'''

# creating Pet objects?

pet_1 = Pet(petName = "goodBoy", petType = "Dog", petAge = 13)
pet_2 = Pet(petName = "Tom", petType = "Cat", petAge= 12)


# adding Pets to DATABASE

db.session.add(pet_1)
db.session.add(pet_2)


# finally commit

db.session.commit()
