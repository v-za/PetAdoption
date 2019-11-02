import os
from adoptPets_config import adoptPetsDB
from products_config import productsDB
from userAccount_config import userAccountDB
from models import User, Adopt, Product

# Initializing the database for userAccount.db
USER = [
	{'userID': 101, 'userName': 'tahirtall', 'userFirst': 'Tahir', 'userLast': 'Uzun', 'userPhone': '6307509861', 'userEmail': 'tahirtall46@gmail.com', 'userAddress': '787 N. York Street, Elmhurst, IL', 'userAddress2': 'Apt. 1F', 'userState': 'Illinois', 'userZip': '60126'},
        {'userID': 102, 'userName': 'crownz', 'userFirst': 'Jack', 'userLast': 'Deniel', 'userPhone': '6304254598', 'userEmail': 'jackdeniels@gmail.com', 'userAddress': '235 N. Wisky Street, Chicago, IL', 'userAddress2': 'Apt. 356', 'userState': 'Illinois', 'userZip': '60126'},
        {'userID': 103, 'userName': 'doglover', 'userFirst': 'Melissa', 'userLast': 'DeAmbregio', 'userPhone': '6308573038', 'userEmail': 'dogsareawsome@gmail.com', 'userAddress': '245 S. Tahirisawsome Street, Chicago, IL', 'userAddress2': 'Apt. 46', 'userState': 'Illinois', 'userZip': '60126'},
]

# Initializing the database for adoptPets.db
ADOPT = [
        {'adoptID': 901, 'adoptName': 'Kont', 'adoptType': 'Dog', 'adoptBreed': 'German Sheppard', 'adoptDesc': '2 years old cutie needs a new home!', 'adoptApperance': 'Brown and Black Fur with fully straight ears', 'adoptGender': 'Male', 'adoptSize': '40 lbs'},
        {'adoptID': 902, 'adoptName': 'Riley', 'adoptType': 'Dog', 'adoptBreed': 'Husky', 'adoptDesc': '6 months old beast needs a new home to destroy everything! Someone save me from this dog please!', 'adoptApperance': 'Grey and White fur with Blue Eyes', 'adoptGender': 'Male', 'adoptSize': '10 lbs'},
        {'adoptID': 903, 'adoptName': 'Cutie', 'adoptType': 'Cat', 'adoptBreed': 'Street Cat', 'adoptDesc': 'Rescued off the street, do not have space for this mf', 'adoptApperance': 'Black fur', 'adoptGender': 'Female', 'adoptSize': '5 lbs'},
]

# Initializing the database for products.
PRODUCTS = [
        {'productID': 301, 'productName': 'Whole Hearted', 'productDesc': 'Grain Free All Life Stages Salmon and Pea Recipe Dry Dog', 'productScale': '25lb', 'productCost': '44.99', 'productCurrentSale': '42.74', 'productStock': '12'},
        {'productID': 302, 'productName': 'Just Food for Dogs', 'productDesc': 'Pantry Fresh Beef and Russet Potato Dog Food', 'productScale': '12X12.5 OZ', 'productCost': '54.95', 'productCurrentSale': '49.99', 'productStock': '9'},
        {'productID': 303, 'productName': 'Royal Canin', 'productDesc': 'Feline Health Nutrition Dry Food for Young Kittens', 'productScale': '15lb', 'productCost': '51.29', 'productCurrentSale': '48.73', 'productStock': '21'},
]

if os.path.exists('userAccount.db'):
	os.remove('userAccount.db')

if os.path.exists('adoptPets.db'):
	os.remove('adoptPets.db')

if os.path.exists('products.db'):
	os.remove('products.db')


adoptPetsDB.create_all()
userAccountDB.create_all()
productsDB.create_all()

for user in USER:
	u = User(userID=user.get('userID'), userName=user.get('userName'), userFirst=user.get('userFirst'), userLast=user.get('userLast'),
		userPhone=user.get('userPhone'), userEmail=user.get('userEmail'), userAddress=user.get('userAddress'), userAddress2=user.get('userAddress2'),
        userState=user.get('userState'), userZip=user.get('userZip'))
	userAccountDB.session.add(u)

for adopt in ADOPT:
	a = Adopt(adoptID=adopt.get('adoptID'), adoptName=adopt.get('adoptName'), adoptType=adopt.get('adoptType'), adoptBreed=adopt.get('adoptBreed'),
		adoptDesc=adopt.get('adoptDesc'), adoptApperance=adopt.get('adoptApperance'), adoptGender=adopt.get('adoptGender'), adoptSize=adopt.get('adoptSize'))
	adoptPetsDB.session.add(a)

for product in PRODUCTS:
        p = Product(productID=product.get('productID'), productName=product.get('productName'), productDesc=product.get('productDesc'), productScale=product.get('productScale'), productCost=product.get('productCost'), productCurrentSale=product.get('productCurrentSale'), productStock=product.get('productStock'))
        productsDB.session.add(p)


userAccountDB.session.commit()
adoptPetsDB.session.commit()
productsDB.session.commit()
