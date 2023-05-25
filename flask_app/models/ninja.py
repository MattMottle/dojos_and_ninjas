from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    db = "dojos_and_ninjas_schemas"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        results = connectToMySQL(cls.db).query_db(query,data)
        return results

    @classmethod
    def get_one(cls, ninja_id):
            query ="SELECT * FROM ninjas WHERE id = %(id)s;"
            data = {'id':ninja_id}
            results = connectToMySQL(cls.db).query_db(query, data)
            return cls(results[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s,age=%(age)s, dojo_id=%(dojo_id)s WHERE ninjas.id = %(id)s;"
        print(query)
        connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)


