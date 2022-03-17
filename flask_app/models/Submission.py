from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
import tkinter as tk
from tkinter import filedialog
from flask_app.models.Author import Author
from flask_app.models.Group import Group

dbName = "workshop_schema"
class Submission:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.filename = data['filename']
        self.filesize = data['filesize']
        self.filetype = data['filetype']
        self.data = data['data']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.group_id = data['group_id']
        self.author_id = data['author_id']
        self.group = None
        self.author = None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO Submissions (title, description, filename, filesize, filetype, data, "\
                "Group_id, Author_id) VALUES (%(title)s, %(description)s, %(filename)s, "\
                "%(filesize)s, %(filetype)s, %(data)s);"
        return MySQLConnection(dbName).query_db( query, data )

    @classmethod
    def get(cls,data):
        query = "SELECT * FROM Submissions WHERE id = %(id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        this_submission = cls(results[0])
        # NOTE need to get the group and the author
        this_submission.author = Author.get_Author_by_id(this_submission.author_id)
        this_submission.group = Group.get_by_id(this_submission.group_id)

    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM Submissions WHERE author_id = %(id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        submissions = []
        for result in results:
            # NOTE need to get the group and the author
            this_submission = cls(result)
            this_submission.author = Author.get_Author_by_id(this_submission.author_id)
            this_submission.group = Group.get_by_id(this_submission.group_id)
            submissions.append(this_submission)
        return submissions

    @classmethod
    def get_all_by_group(cls,data):
        query = "SELECT * FROM Submissions WHERE Group_id = %(id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        submissions = []
        for result in results:
            # NOTE need to get the group and the author
            this_submission = cls(result)
            this_submission.author = Author.get_Author_by_id(this_submission.author_id)
            this_submission.group = Group.get_by_id(this_submission.group_id)
            submissions.append(this_submission)
        return submissions

    @classmethod
    def delete(cls,data):
        pass

