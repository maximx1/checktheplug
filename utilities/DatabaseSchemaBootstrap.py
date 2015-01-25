import os.path
import sqlite3

"""
    Basic utility to create and data load a database.
"""
class DatabaseSchemaBootstrap:
    def bootstrap(self, app):
        if not os.path.isfile(app.settings.database):
            conn = sqlite3.connect(app.settings.database)
            with conn:
                cursor = conn.cursor()
                f = open(app.settings.schema, 'r')
                for line in f:
                    if "" != line and not line.startswith("//"):
                        print("Executing: '" + line + "'")
                        cursor.execute(line)
                f.close()