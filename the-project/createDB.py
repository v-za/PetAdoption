#Creating Database

'''
simple program to create DATABASE

'''

from application import db
<<<<<<< HEAD
from application.models import Pet,User   #import Pet model for DATABASE
=======
from application.models import Pet   #import Pet model for DATABASE
from application.models import Product   #import Product model for DATABASE
>>>>>>> 3b46ec838ffd4eaebd8b6b855bc6b9c0214f2cef

#creating the DATABASE

db.create_all()
