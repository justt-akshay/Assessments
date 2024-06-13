from database import Database

class User:
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type

    def register(self):
        db = Database()
        query = "INSERT INTO users (username, password, user_type) VALUES (%s, %s, %s)"
        params = (self.username, self.password, self.user_type)
        db.execute_query(query, params)

    def login(self):
        db = Database()
        query = "SELECT * FROM users WHERE username=%s AND password=%s AND user_type=%s"
        params = (self.username, self.password, self.user_type)
        return db.fetch_one(query, params)
