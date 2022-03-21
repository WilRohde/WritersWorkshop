from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.Author import Author

dbName = "workshop_schema"
class Creator:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.first_name = data['firstname']
        self.last_name = data['lastname']
    
    @classmethod
    def get(cls, data):
        query = "SELECT id, email, firstname, lastname FROM Authors WHERE id=%(Creator_id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        return cls(results[0])
