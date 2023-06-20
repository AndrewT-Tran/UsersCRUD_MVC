# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the User table from our database


class User:
    DB = 'mydb'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    # CRUD
    # Create
    @classmethod
    def save(cls, data):
        query = """INSERT INTO `mydb`.`users` (first_name,last_name,email)
        VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    # Read

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        all_users = []
        # this will give us the row
        # we will get a dictionary back from the database
        # Iterate over the db results and create instances of friends with cls.
        for row in results:
            # make object

            all_users.append(cls(row))
        return all_users

    @classmethod
    def get_one(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    # Update

    @classmethod
    def update(cls, data):
        query = """
        UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id=%(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    # Delete

    @classmethod
    def delete(cls, user_id):
        query = "DELETE FROM mydb.users WHERE id = %(id)s;"
        data = {"id": user_id}
        return connectToMySQL(cls.DB).query_db(query, data)
    # @staticmethod
    # def edit(user_id):
    #     query = "SELECT * FROM users WHERE id = %(id)s;"
    #     data = {"id": user_id}
    #     result = connectToMySQL('mydb').query_db(query, data)
    #     return result