#Creating Database

'''
simple program to create DATABASE

'''

from application import db
from application.models import Pet   #import Pet model for DATABASE

#creating the DATABASE

db.create_all()
