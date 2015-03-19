import sqlite3

from checktheplug.models.User import User


class UserDao:
    def __init__(self, settings):
        self.conn = sqlite3.connect(settings.database)

    def login(self, username, password):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, username, gravatar, admin from users where username=? and password=?", (username, password))
            row = cur.fetchone()
            return User(row[0], row[1], row[2], True if row[3] == 1 else False) if row else None
