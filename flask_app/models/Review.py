from flask_app.config.mySQLConnection import MySQLConnection, connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.Reviewer import Reviewer

dbName = "workshop_schema"
class Review:
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.submission_id = data['Submission_id']
        self.reviewer_id = data['Reviewer_id']
        self.reviewer = None
        self.submission = None

    @classmethod
    def get_by_submission(cls,id):
        data = {
            'id': id
        }
        query = "SELECT * FROM Reviews WHERE Submission_id = %(id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        reviews = []
        for result in results:
            review = cls(result)
            review.reviewer = Reviewer.get_reviewer(review.reviewer_id)
            reviews.append(review)
        return reviews

    @classmethod
    def get_by_reviewer_submission(cls,data):
        query = "SELECT * FROM Reviews WHERE Submission_id = %(id)s AND Reviewer_id = %(reviewer_id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        if results == ():
            return None
        else:
            review = cls(results[0])
            review.reviewer = Reviewer.get_reviewer(review.reviewer_id)
            return review
            
    @classmethod
    def get_by_reviewer(cls, data):
        query = "SELECT * FROM Reviews WHERE Reviewer_id = %(id)s;"
        results = MySQLConnection(dbName).query_db( query, data )
        reviews = []
        for result in results:
            review = cls(result)
            review.reviewer = Reviewer.get_reviewer(review.reviewer_id)
            reviews.append(review)
        return reviews

    @classmethod
    def save(cls,data):
        query = "INSERT INTO Reviews (text, Submission_id, Reviewer_id) VALUES "\
                "(%(text)s, %(submission_id)s, %(reviewer_id)s);"
        return MySQLConnection(dbName).query_db( query, data )

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM Reviews WHERE id = %(id)s;"
        return MySQLConnection(dbName).query_db( query, data )

    @classmethod
    def update(cls,data):
        query = "UPDATE Reviews SET text = %(text)s WHERE id = %(id)s;"
        return MySQLConnection(dbName).query_db( query, data )
