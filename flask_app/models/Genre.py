from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app

dbName = "workshop_schema"
class Genre:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.short_description = data['short_description']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get(cls, data):
        query = "SELECT * FROM Genres WHERE id = %(id)s;"
        result = MySQLConnection(dbName).query_db( query, data )
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Genres;"
        results = MySQLConnection(dbName).query_db( query)
        genres = []
        for result in results:
            genres.append(cls(result))
        return genres
        
    @classmethod
    def save(cls,data):
        query = "INSERT INTO Genres (name, description, short_description) "\
                "VALUES (%(name)s, %(description)s, %(short_description)s);"
        return MySQLConnection(dbName).query_db( query, data )

    # NOTE: you CANNOT delete Genres
    @classmethod
    def update(cls,data):
        query = "UPDATE Genres SET name = %(name)s, description = %(description)s, "\
                "short_description = %(short_description)s where id = %(id)s;"
        return MySQLConnection(dbName).query_db( query, data )

    @staticmethod
    def validate(data):
        is_valid = True
        if data['genrename'] == "":
            flash("Genre Name is Required", "Genre")
            is_valid = False
        if data['short_description'] == "":
            flash("Genre Short Description is Required", "Genre")
            is_valid = False
        if data['description'] == "":
            flash("Genre Description is Required", "Genre")
            is_valid = False
        return is_valid
        