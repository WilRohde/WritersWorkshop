from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import json
from flask_app import app
from flask_app.models.Author import Author

dbName = "workshop_schema"
class Reviewer:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.first_name = data['firstname']
        self.last_name = data['lastname']

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def get_reviewer(cls, id):
        data = {
            'id': id
        }
        query = "SELECT id, email, firstname, lastname FROM Authors WHERE id=%(id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        return cls(results[0])
