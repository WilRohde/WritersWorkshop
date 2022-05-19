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
from flask_app.models.Member import Member

dbName = "workshop_schema"
class Group:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.short_description = data['short_description']
        self.created_at = str(data['created_at'])
        self.updated_at = str(data['updated_at'])
        # founding_date = data['founding_date']
        # self.founding_date = str(DateFormat.format_date(founding_date))
        self.founding_date = str(data['founding_date'])
        self.creator_id = data['Creator_id']
        self.genre_id = data['Genre_id']
        self.genre = data['name'] #NOTE: this CANNOT be right 05/18/2022
        self.member_count = 0
        self.creator = None
        self.members = []

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def save(cls,data):
        _data = [
            data['name'],
            data['description'],
            data['short_description'],
            data['creator_id'],
            data['genre_id']
        ]
        results = MySQLConnection(dbName).call_proc('create_group',_data)
        print(f"value returned results = {results}")
        if (results == False):
            print(f"value {results} fell into False")
            return False
        else:
            # it worked. Now go back and get the member from the db
            _Group = Group(results[0])

        # creator of the group is the first member
        _data = [
            _Group.id,
            data['creator_id']
        ]
        results = MySQLConnection(dbName).call_proc('join_group',_data)
        print(f"value returned results = {results}")
        if (results == False):
            print(f"value {results} fell into False")
            return False
        else:
            # it worked. Now go back and get the member from the db
            # NOTE: not sure if this is right, just return the row we just made in the GroupMembership table
            return results[0]

    @classmethod
    def join(cls,data):
        _data = [
            data['group_id'],
            data['author_id']
        ]
        results = MySQLConnection(dbName).call_proc('join_group',_data)
        print(f"value returned results = {results}")
        if (results == False):
            print(f"value {results} fell into False")
            return False
        else:
            # it worked. Now go back and get the member from the db
            # NOTE: not sure if this is right, just return the row we just made in the GroupMembership table
            return results[0]

    @classmethod
    def is_member(cls,data):
        _data = [
            data['group_id'],
            data['author_id']
        ]
        results = MySQLConnection(dbName).call_proc('author_is_member',_data)
        # NOTE: have to test this don't trust it
        if len(results) > 0:
            return True
        else:
            return False

    @classmethod
    def get_by_id(cls,data):
        _data = [
            data['group_id']
        ]
        results = MySQLConnection(dbName).call_proc('get_group_by_id',_data)
        if (results == False) or len(results) < 1:
            return False
        group = cls(results[0])
        data = {
            'Creator_id': group.creator_id
        }
        group.creator = Creator.get(data)
        #group.creator = Author.get_Author_by_id(data)
        data = {
            'id': group.id
        }
        group.members = Group.get_group_members(data)
        group.member_count = len(group.members)
        return group

    @classmethod
    def is_group(cls,data):
        _data = [
            data['name']
        ]
        results = MySQLConnection(dbName).call_proc('get_group_by_name',_data)
        # NOTE: have to test this don't trust it
        if len(results) > 0:
            return True
        else:
            return False

    @classmethod
    def get_all(cls):
        # query = "SELECT WritingGroups.*, Genres.name as GenreName FROM WritingGroups "\
        #         "LEFT JOIN Genres ON WritingGroups.genre_id = Genres.id;"
        # results = MySQLConnection(dbName).query_db( query )
        results = MySQLConnection(dbName).call_proc('get_groups')
        Groups = []
        if results == False:
            return Groups

        for result in results:
            this_group = cls(result)
            print(f"this_group.id = {this_group.id}")
            data = {
                'Creator_id': this_group.creator_id
            }
            print(f"value of data is = {data}")
            #this_group.creator = Author.get_Author_by_id(data)
            this_group.creator = Creator.get(data)
            # NOTE: 05/16/2022 - don't load members here but need to do later
            data = {
                'id': this_group.id
            }
            # print(f"value of data = {data}")
            # this_group.members = Group.get_group_members(data)
            this_group.member_count = Group.get_member_count(data)
            Groups.append(this_group)
        return Groups

    @classmethod
    def get_member_count(cls,data):
        _data = [
            data['id']
        ]
        results = MySQLConnection(dbName).call_proc('get_group_member_count',_data)
        if (results == False) or (len(results)==0):
            print(f"value {results} fell into False")
            return 0
        else:
            print(f"get_member_count returned {results}")
            result = results[0]
            return result['member_count']

    @classmethod
    def update(cls, data):
        # NOTE: you cannot change/update the group's creator
        # NOTE: 05/15/2022 need to test this!
        _data = [
            data['id'],
            data['name'],
            data['description'],
            data['short_description'],
            data['founding_date']
        ]
        return MySQLConnection(dbName).call_proc('update_group',_data)

    @classmethod
    def get_group_members(cls,data):
        members = []
        _data = [
            data['id']
        ]
        results = MySQLConnection(dbName).call_proc('get_group_members',_data)
        # query = "SELECT Authors.firstname, Authors.lastname FROM Authors LEFT JOIN GroupMembers " \
        #         "ON authors.id = GroupMembers.author_id LEFT JOIN WritingGroups " \
        #         "ON GroupMembers.Group_id = WritingGroups.id WHERE WritingGroups.id = %(id)s;"
        #results = MySQLConnection(dbName).query_db( query, data )
        if (results == False) or (len(results)==0):
            print(f"value {results} fell into False")
            return False
        else:
            for result in results:
                members.append(Member(result))
            return members

    @classmethod
    def get_all_for_author(cls,data):
        groups = []
        _data = [
            data['id']
        ]
        results = MySQLConnection(dbName).call_proc('get_author_groups',_data)
        if (results == False) or (len(results)==0):
            print(f"value {results} fell into False")
            return False
        else:
            for result in results:
                groups.append(Group(result))
            return groups

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
