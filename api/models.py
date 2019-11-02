##from application import db
from config import productsDB, productsMA, userDB, userMA, adoptDB, adoptMA

class User(userDB.Model):
    __tablename__ = "user"
    userID = userDB.Column(userDB.Integer, primary_key=True)
    userName = userDB.Column(userDB.String(20))
    userFirst = userDB.Column(userDB.String(20))
    userLast = userDB.Column(userDB.String(50))
    userPhone = userDB.Column(userDB.String(50))
    userEmail = userDB.Column(userDB.String(50))
    userAddress = userDB.Column(userDB.String(200))
    userAddress2 = userDB.Column(userDB.String(200))
    userState = userDB.Column(userDB.String(30))
    userZip = userDB.Column(userDB.String(6))

class UserSchema(userMA.ModelSchema):
	class Meta:
		model = User
		sqla_session = userDB.session

class Adopt(adoptDB.Model):
    __tablename__ = "adopt"
    adoptID = adoptDB.Column(adoptDB.Integer, primary_key=True)
    adoptName = adoptDB.Column(adoptDB.String(20))
    adoptType = adoptDB.Column(adoptDB.String(20))
    adoptBreed = adoptDB.Column(adoptDB.String(20))
    adoptDesc = adoptDB.Column(adoptDB.String(500))
    adoptAppearance = adoptDB.Column(adoptDB.String(100))
    adoptGender = adoptDB.Column(adoptDB.String(6))
    adoptSize = adoptDB.Column(adoptDB.String(10))

class AdoptSchema(adoptMA.ModelSchema):
	class Meta:
		model = Adopt
		sqla_session = adoptDB.session

class Product(productsDB.Model):
    __tablename__ = "product"
    productID = productsDB.Column(productsDB.Integer, primary_key=True)
    productName = productsDB.Column(productsDB.String(40))
    productDesc = productsDB.Column(productsDB.String(500))
    productScale = productsDB.Column(productsDB.String(10))
    productCost = productsDB.Column(productsDB.String(10))
    productCurrentSale = productsDB.Column(productsDB.String(10))
    productStock = productsDB.Column(productsDB.String(32))

class ProductSchema(productsMA.ModelSchema):
    class Meta:
        model = Product
        sqla_session = productsDB.session
