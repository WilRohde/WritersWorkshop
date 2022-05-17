from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import json, flash
from flask_app import app
from flask_bcrypt import Bcrypt
import re
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]{3,}$')
PASSWORD_REGEX = re.compile(r'^[a-zA-Z0-9#%&!@]{8,}$')
dbName = "workshop_schema"

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.first_name = data['firstname']
        self.last_name = data['lastname']
        self.password = data['password']
        self.created_at = str(data['created_at'])
        self.update_at = str(data['updated_at'])

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def save(cls,data):
        data['@id']=0
        _data = [
            data['username'],
            data['email'],
            data['firstname'],
            data['lastname'],
            data['password']
        ]
        results = MySQLConnection(dbName).call_proc('create_author',_data)
        print(f"value returned results = {results}")
        if (results == False):
            print(f"value {results} fell into False")
            return False
        else:
            # it worked. Now go back and get the member from the db
            print(f"fell into success with value result = {results}")
            # _data = [data['username']]
            # results = MySQLConnection(dbName).call_proc('get_author_by_username',_data)
            _author = Author(results[0])
            return _author

    @classmethod
    def login(cls,data):
        query = "SELECT * FROM Authors WHERE email = %(email)s;"
        return MySQLConnection(dbName).query_db( query, data )

    @classmethod
    def get_Author_by_credential(cls,data):
        if EMAIL_REGEX.match(data['credential']):
            # signing in with e-mail
            _data = [data['credential']]
            results = MySQLConnection(dbName).call_proc('get_author_by_email',_data)
            print(f"value returned results = {results}")
            if (results == False) or (results == ()):
                return False
            else:
                _author = Author(results[0])
                return _author
        else:
            _data = [data["credential"]]
            results = MySQLConnection(dbName).call_proc('get_author_by_username',_data)
            print(f"value returned results = {results}")
            if (results == False) or (results == ()):
                return False
            else:
                _author = Author(results[0])
                return _author

    @classmethod
    def get_Author_by_email(cls,data):
        _data = [
            data['email']
        ]
        results = MySQLConnection(dbName).call_proc('get_author_by_email',_data)
        print(f"value returned results = {results}")
        if (results == False) or (results == ()):
            return False
        else:
            _author = Author(results[0])
            return _author

    @classmethod
    def get_Author_by_id(cls,data):
            _data = [data['id']]
            results = MySQLConnection(dbName).call_proc('get_author_by_id',_data)
            print(f"value returned results = {results}")
            if (results == False) or (results == ()):
                return False
            else:
                _author = Author(results[0])
                return _author

    @classmethod
    def get_Author_by_username(cls,data):
            _data = [data['username']]
            results = MySQLConnection(dbName).call_proc('get_author_by_username',_data)
            print(f"value returned results = {results}")
            if (results == False) or (results == ()):
                return False
            else:
                _author = Author(results[0])
                return _author

    @staticmethod
    def validate(data):
        is_valid = True
        print(f"validate data = {data}")
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!","register")
            is_valid = False
        if not NAME_REGEX.match(data['firstname']):
            flash("First Name is invalid!","register")
            is_valid = False
        if not NAME_REGEX.match(data['lastname']):
            flash("Last Name is invalid!","register")
            is_valid = False
        if not PASSWORD_REGEX.match(data['password']):
            flash("Password must be 8 valid characters!","register")
            is_valid = False
        if (data['password']!=data['confirm-password']):
            flash("Password entries do not match!","register")
            is_valid = False
        results = Author.get_Author_by_email(data)
        if results != False:
            flash(f"Author email {data['email']} already exists in database!","register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        print(f"login data {data}")
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!","login")
            is_valid = False
        if not PASSWORD_REGEX.match(data['password']):
            flash("Password must be 8 valid characters!","login")
        return is_valid