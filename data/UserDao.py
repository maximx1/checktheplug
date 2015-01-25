import sqlite3

class UserDao:
    def __init__(self, settings):
        self.conn = sqlite3.connect(settings.database)

    def login(self, username, password):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, username, gravatar, admin from users where username=? and password=?", (username, password))
            row = cur.fetchone()
            if row:
                return {"id": row[0], "username": row[1], "gravatar": row[2], "admin" : True if row[3] == 1 else False}
            return {"status": "login failed"}