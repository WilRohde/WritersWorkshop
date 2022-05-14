from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
#from flask import flash
#from flask_app import app
#from flask_bcrypt import Bcrypt
import re
#bcrypt = Bcrypt(app)
dbName = "workshop_schema"

def save(data):
    data['@id']=0
    _data = [
        data['username'],
        data['email'],
        data['firstname'],
        data['lastname'],
        data['password'],
        data['@id']
    ]
    result = MySQLConnection(dbName).call_proc('create_author',_data)
    print(f"MySQL returned result={result}")
    _id=result[5]
    if (_id == ()) or (_id == False):
        print(f"value {id} fell into False")
        return False
    else:
        # it worked. Now go back and get the member from the db
        _data = [id]
        print(_data)

data = {
    'username': 'AntonC',
    'email': 'Anton@murder.com',
    'firstname': 'Anton',
    'lastname': 'Chigur',
    'password': 'Antonio90909',
    '@id': 0
}

save(data)

