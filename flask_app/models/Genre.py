from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import json, flash
from flask_app import app

dbName = "workshop_schema"
class Genre:
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.short_description = data['short_description']
        self.description = data['description']
        self.created_at = str(data['created_at'])
        self.updated_at = str(data['updated_at'])

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def save(cls,data):
        _data = [
            data['name'],
            data['short_description'],
            data['description']
        ]
        results = MySQLConnection(dbName).call_proc('create_genre',_data)
        print(f"value returned results = {results}")
        if (results == False):
            print(f"value {results} fell into False")
            return False
        else:
            return Genre(results[0])

    @classmethod
    def get_by_id(cls, data):
        _data = [
            data['id']
        ]
        results = MySQLConnection(dbName).call_proc('get_genre_by_id',_data)
        print(f"value returned results = {results}")
        if (results == False):
            print(f"value {results} fell into False")
            return False
        else:
            return cls(results[0])

    @classmethod
    def get_by_name(cls,data):
        _data = [
            data['name']
        ]
        results = MySQLConnection(dbName).call_proc('get_genre_by_name',_data)
        print(f"value returned results = {results}")
        if (results == False):
            print(f"value {results} fell into False")
            return False
        else:
            return cls(results[0])

    @classmethod
    def get_all(cls):
        _data=[]
        results = MySQLConnection(dbName).call_proc('get_genres',_data)
        genres = []
        for result in results:
            genres.append(cls(result))
        return genres
        
    # NOTE: you CANNOT delete Genres
    # NOTE: you CANNOT change a genre name
    @classmethod
    def update(cls,data):
        _data = [
            data['id'],
            data['short_description'],
            data['description']
        ]
        results = MySQLConnection(dbName).call_proc('update_genre',_data)
        print(f"value returned results = {results}")
        if (results == False):
            print(f"value {results} fell into False")
            return False
        else:
            return cls(results[0])

        # query = "UPDATE Genres SET name = %(name)s, description = %(description)s, "\
        #         "short_description = %(short_description)s where id = %(id)s;"
        # return MySQLConnection(dbName).query_db( query, data )

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
        