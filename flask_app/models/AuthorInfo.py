from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import json, flash
from flask_app import app
import re
from flask_app.models import Author, Group

class AuthorInfo:
    def __init__(self,data):
        self.username = data['username']
        self.email = data['email']
        self.first_name = data['firstname']
        self.last_name = data['lastname']

@classmethod
def get_memberships(self,data):
    pass

@classmethod
def get_submissions(self,data):
    pass

@classmethod
def get_reviews(self.data):
    pass
