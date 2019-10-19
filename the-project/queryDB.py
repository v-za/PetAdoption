# for quering the Pet DATABASE
from application import db
from application.models import Pet
print(Pet.query.all())
