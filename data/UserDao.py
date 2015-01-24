import sqlite3

class UserDao:
    def __init__(self, settings):
        self.conn = sqlite3.connect(settings.database)