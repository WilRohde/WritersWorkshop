from operator import is_
from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.Author import Author
from flask_app.models.Genre import Genre
from flask_app.models.Creator import Creator
from flask_app.models.Dateformat import DateFormat

dbName = "workshop_schema"
class Group:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.short_description = data['short_description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        founding_date = data['founding_date']
        self.founding_date = DateFormat.format_date(founding_date)
        self.creator_id = data['Creator_id']
        self.genre_id = data['Genre_id']
        self.genre = data['GenreName']
        self.member_count = 0
        self.creator = None
        self.members = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO WritingGroups (name, description, short_description, founding_date, "\
            "creator_id, genre_id) VALUES (%(name)s, %(description)s, %(short_description)s, %(founding_date)s, "\
            "%(creator_id)s, %(genre_id)s);"
        group_id = MySQLConnection(dbName).query_db( query, data )
        print(f"group insertion returned {group_id}")
        # group_id should have come back from the query
        author_id = data['creator_id']
        data = {
            'group_id': group_id,
            'author_id': author_id
        }
        # creator of the group is the first member
        query = "INSERT INTO GroupMembers(group_id, author_id) VALUES (%(group_id)s, %(author_id)s);"
        return MySQLConnection(dbName).query_db( query, data )

    @classmethod
    def join(cls,data):
        query = "INSERT INTO GroupMembers(group_id, author_id) VALUES (%(group_id)s, %(author_id)s);"
        return MySQLConnection(dbName).query_db( query, data )

    @classmethod
    def is_member(cls,data):
        query = "SELECT * FROM GroupMembers where group_id = %(group_id)s AND author_id=%(author_id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        if len(results) > 0:
            return True
        else:
            return False

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT WritingGroups.*, Genres.name as GenreName FROM WritingGroups LEFT JOIN Genres "\
                " ON WritingGroups.genre_id = Genres.id WHERE WritingGroups.id = %(id)s;"
        result = MySQLConnection(dbName).query_db( query, data )
        if len(result) < 1:
            return False
        group = cls(result[0])
        data = {
            'Creator_id': group.creator_id
        }
        group.creator = Creator.get(data)
        #group.creator = Author.get_Author_by_id(data)
        data = {
            'id': group.id
        }
        group.members = Author.get_group_members(data)
        group.member_count = len(group.members)
        return group

    @classmethod
    def get_all(cls):
        query = "SELECT WritingGroups.*, Genres.name as GenreName FROM WritingGroups "\
                "LEFT JOIN Genres ON WritingGroups.genre_id = Genres.id;"
        results = MySQLConnection(dbName).query_db( query )
        Groups = []
        if results == False:
            return Groups

        for result in results:
            this_group = cls(result)
            data = {
                'Creator_id': this_group.creator_id
            }
            #this_group.creator = Author.get_Author_by_id(data)
            this_group.creator = Creator.get(data)
            data = {
                'id': this_group.id
            }
            this_group.members = Author.get_group_members(data)
            this_group.member_count = len(this_group.members)
            Groups.append(this_group)
        return Groups

    @classmethod
    def delete(cls,data):
        # delete the members first
        query = "DELETE FROM GroupMembers WHERE group_id = %(id)s;"
        deleted = MySQLConnection(dbName).query_db( query, data )

        # now delete the group
        query = "DELETE FROM WritingGroups WHERE id = %(id)s;"
        return MySQLConnection(dbName).query_db( query, data )
    
    @classmethod
    def update(cls, data):
        # NOTE: you cannot change/update the group's creator
        query = "UPDATE WritingGroups SET name = %(name)s, description = %(description)s, "\
                "short_description = %(short_description)s, founding_date = %(founding_date)s, "\
                "WHERE id = %(id)s;"
        return MySQLConnection(dbName).query_db( query, data )

    @staticmethod
    def validate(data):
        is_Valid = True
        if data['groupname'] == "":
            flash("Group Name is Required","Group")
            is_Valid = False
        if data['genre'] == "":
            flash("Group Genre is Required","Group")
            is_Valid = False
        if data['description'] == "":
            flash("Group Description is Required","Group")
            is_Valid = False
        if data['short_description'] == "":
            flash("Group Short Description is Required","Group")
            is_Valid = False
        if data['founding_date'] == "":
            flash("Group Founding Date is Required","Group")
            is_Valid = False
        return is_Valid
