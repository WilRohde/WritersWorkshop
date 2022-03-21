from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
import tkinter as tk
from tkinter import filedialog
from flask_app.models.Author import Author
from flask_app.models.Group import Group
from flask_app.models.Review import Review

dbName = "workshop_schema"
class Submission:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.data = data['data']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.group_id = data['Group_id']
        self.author_id = data['Author_id']
        self.review_count = 0
        self.group = None
        self.author = None
        self.reviews = None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO Submissions (title, description, data, "\
                "Group_id, Author_id) VALUES (%(title)s, %(description)s, "\
                "%(submission_text)s, %(group_id)s, %(Author_id)s);"
        return MySQLConnection(dbName).query_db( query, data )

    @classmethod
    def update(cls, data):
        query = "UPDATE Submissions SET title=%(title)s, description=%(description)s, data=%(submission_text)s, "\
                "Group_id=%(group_id)s, Author_id=%(Author_id)s WHERE Submissions.id = %(id)s;"
        return MySQLConnection(dbName).query_db( query, data )

    @classmethod
    def get(cls,data):
        query = "SELECT * FROM Submissions WHERE id = %(id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        this_submission = cls(results[0])
        # NOTE need to get the group and the author
        data = {
            'Author_id': this_submission.author_id
        }
        this_submission.author = Author.get_Author_by_id(data)
        data = {
            'id': this_submission.group_id
        }
        this_submission.group = Group.get_by_id(data)
        this_submission.reviews = Review.get_by_submission(this_submission.id)
        this_submission.review_count = len(this_submission.reviews)
        return this_submission

    @classmethod
    def get_all(cls,data):
        query = "SELECT * FROM Submissions WHERE author_id = %(id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        submissions = []
        for result in results:
            # NOTE need to get the group and the author
            this_submission = cls(result)
            #this_submission.author = Author.get_Author_by_id(this_submission.author_id)
            #this_submission.group = Group.get_by_id(this_submission.group_id)
            this_submission.reviews = Review.get_by_submission(this_submission.id)
            this_submission.review_count = len(this_submission.reviews)
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
            data = {
                'Author_id': this_submission.author_id
            }
            print(f"Looking for submissions from Author_id = {this_submission.author_id}")
            this_submission.author = Author.get_Author_by_id(data)
            data = {
                'id': this_submission.group_id
            }
            this_submission.group = Group.get_by_id(data)
            this_submission.reviews = Review.get_by_submission(this_submission.id)
            this_submission.review_count = len(this_submission.reviews)
            submissions.append(this_submission)
        return submissions

    @classmethod
    def delete(cls,data):
        pass

