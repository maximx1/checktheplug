import os.path
import sqlite3

"""
    Basic utility to create and data load a database.
"""
class DatabaseSchemaBootstrap:
    def bootstrap(self, settings):
        if not os.path.isfile(settings.database):
            conn = sqlite3.connect(settings.database)
            with conn:
                cursor = conn.cursor()
                f = open(settings.schema, 'r')
                for line in f:
                    line = line.rstrip()
                    if "" != line and not line.startswith("//"):
                        print("Executing: '" + line + "'")
                        cursor.execute(line)
                f.close()
