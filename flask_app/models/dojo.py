# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja
# model the class after the friend table from our database

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.ninjas = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def create(cls, data:dict):
        #query the string
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        #contact the database
        dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        return dojo_id

    #want to be able to update whichever user we select by id thro the DB since each id is unique to the user
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_one_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        dojo = cls(result[0])
        for row in result:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'dojo_id': row['dojo_id'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
    #edit the user and update the information
    # @classmethod
    # def update(cls, data):
    #     # query = "UPDATE users SET name=%(name)s, email=%(email)s, description=%(description)s, updated_at=NOW() WHERE id = %(id)s;"
    #     # make sure theres no spaces inbetwwen each comma
    #     query = "UPDATE dojos SET name=%(name)s,updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def destroy(cls,data):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL(DATABASE).query_db(query, data)

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # checking to make sure there arent any errors
        if results:
        # Create an empty list to append our instances of friends
            dojos = []
            # Iterate over the db results and create instances of friends with cls.
            for dojo in results:
                dojos.append( cls(dojo) )
            return dojos
        return False