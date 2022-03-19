from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.Author import Author
from flask_app.models.Genre import Genre

dbName = "workshop_schema"
class Group:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.short_description = data['short_description']
        self.founding_date = data['founding_date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator_id = data['Creator_id']
        self.genre_id = data['Genre_id']
        self.member_count = 0
        self.creator = None
        self.members = []
        self.genre = None

    def getCreator(data):
        pass

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
    def get_by_id(cls,data):
        query = "SELECT * FROM WritingGroups WHERE id = %(id)s;"
        result = MySQLConnection(dbName).query_db( query, data )
        if len(result) < 1:
            return False
        group = cls(result[0])
        data = {
            'Author_id': group.creator_id
        }
        group.creator = Author.get_Author_by_id(data)
        data = {
            'id': group.id
        }
        group.members = Author.get_group_members(data)
        group.member_count = len(group.members)
        return group

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM WritingGroups;"
        results = MySQLConnection(dbName).query_db( query )
        Groups = []
        if results == False:
            return Groups

        for result in results:
            this_group = cls(result)
            data = {
                'Author_id': this_group.creator_id
            }
            this_group.creator = Author.get_Author_by_id(data)
            data = {
                'id': this_group.id
            }
            this_group.members = Author.get_group_members(data)
            this_group.member_count = len(this_group.members)
            Groups.append(this_group)
        return Groups

    @classmethod
    def get_genre(cls,data):
        pass
    
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
        query = "UPDATE WritingGroups SET name = %(name)s, description = %(description)s, "\
                "short_description = %(short_description)s, founding_date = %(founding_date)s, "\
                "creator_id = %(creator_id)s WHERE id = %(id)s;"
        return MySQLConnection(dbName).query_db( query, data )

