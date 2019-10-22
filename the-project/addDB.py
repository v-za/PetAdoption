#for adding into DATABASE
from application import db
from application.models import Pet
from application.models import Product

'''
simply adding into Pet DATABASE

'''

# Create Pet Objects

pet_1 = Pet(petName = "goodBoy", petType = "Dog", petAge = 13)
pet_2 = Pet(petName = "Tom", petType = "Cat", petAge= 12)


# adding Pets to DATABASE

db.session.add(pet_1)
db.session.add(pet_2)

# Create Product Objects

product_1 = Product(productName = "Ruggs' Rubber Bones", productType = "Toy", productDesc = "A nice rubber bone for your beloved pooch.", productPrice = 2, productInStock = 18)
product_2 = Product(productName = "Kitty Kingdom Sandbox", productType = "Maintenance", productDesc = "A comfy place for your kitty to relieve himself.", productPrice = 18,  productInStock = 6)


# adding Producs to DATABASE

db.session.add(product_1)
db.session.add(product_2)

# finally commit

db.session.commit()
