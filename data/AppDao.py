import sqlite3

class AppDao:
    def __init__(self, settings):
        self.conn = sqlite3.connect(settings.database)

    def getAppDetails(self, appshortkey):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, appshortkey, name, description, host from applications where appshortkey=?", (appshortkey,))
            appRow = cur.fetchone()
            if appRow:
                return {"appshortkey": appRow[1], "name": appRow[2], "description": appRow[3], "host" : appRow[4]}
            return {"status": "Application short key not found"}

    def getEnvVariables(self, appshortkey):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id from applications where appshortkey=?", (appshortkey,))
            appRow = cur.fetchone()
            if appRow:
                cur.execute("select envVariable, envValue from envVariables where app_id = ?", (appRow[0]))
                envVarRows = cur.fetchall()
                if len(envVarRows) > 0:
                    return {"envVars": }
                return {"status": "No not found"}
            return {"status": "Application short key not found"}

    def verifyUserAccess(self, appshortkey, authKey):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("select ak.authKey from authKeys ak join applications a on ak.app_id = a.id where a.appshortkey = ? and ak.authKey = ?", (appshortkey, authKey))
            appRow = cur.fetchone()
            return True if appRow else False

    """
        Determines which ports are left available out of the range allotted
        * range is set to 9700 - 9799 inclusive. Likely each server isn't going to be hosting 100 apps
    """
    def calculateNextPort(self, usedPorts):
        portRange = set(range(9700, 9800))
        portsLeft = portRange - set(usedPorts)
        return portsLeft.pop() if portsLeft else None