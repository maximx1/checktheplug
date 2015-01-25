import sqlite3

class AppDao:
    def __init__(self, settings):
        self.conn = sqlite3.connect(settings.database)

    def getAppDetails(self, authKey, appshortkey):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, appshortkey, name, description, host from applications where appshortkey=?", (appshortkey,))
            appRow = cur.fetchone()
            if appRow:
                cur.execute("SELECT * from authKeys where app_id=? and authKey=?", (appRow[0], authKey))
                authRow = cur.fetchone()
                if authRow:
                    return {"appshortkey": appRow[1], "name": appRow[2], "description": appRow[3], "host" : appRow[4]}
                return {"status": "Unauthorized"}
            return {"status": "Application id not found"}