from msilib.schema import Class
from operator import is_
from tokenize import group
from flask import json, flash, session
from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask_app import app
from flask_app.models.Author import Author
from flask_app.models.Genre import Genre
from flask_app.models.Creator import Creator
from flask_app.models.Dateformat import DateFormat

dbName = "workshop_schema"
class SQLClass:
    def __init__(self):
        self.id = 2

    @classmethod
    def get_group_members(cls,data):
        #results = MySQLConnection(dbName).call_proc('get_group_members',data)
        query = "SELECT Authors.firstname, Authors.lastname FROM Authors LEFT JOIN GroupMembers " \
                "ON authors.id = GroupMembers.author_id LEFT JOIN WritingGroups " \
                "ON GroupMembers.Group_id = WritingGroups.id WHERE WritingGroups.id = %(id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        members = []
        if (results == False) or (len(results)==0):
            print(f"value {results} fell into False")
            return False
        else:
            for result in results:
                members.append(Member(result))
                print(result)
            return members

class Member:
    def __init__(self, data):
        self.firstname = data['firstname']
        self.lastname = data['lastname']

k = 1
while (k <= 10):
    _data = {
        'id': k
    }
    my_sqlclass = SQLClass()
    my_sqlclass.get_group_members(_data)
    k = k+1