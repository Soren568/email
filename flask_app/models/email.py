from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DB = "email_validation_schema"

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails(email) VALUES (%(email)s);"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        result = connectToMySQL(DB).query_db(query)
        emails = []
        for email in result:
            emails.append(cls(email))
        return emails

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)


#  WITHOUT DUPE CHECK
    # @staticmethod
    # def validate_email(user):
    #     is_valid = True
    #     if not EMAIL_REGEX.match(user['email']):
    #         flash("Invalid email address!", 'email')
    #         is_valid = False
    #     elif user['email'] == :
    #     return is_valid

# WITH DUPE CHECK
    @staticmethod
    def validate_email(email_one): #request form
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL(DB).query_db(query,email_one)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email_one['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid