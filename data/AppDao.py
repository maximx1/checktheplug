import sqlite3
from models.App import App
from utilities.StringOps import randomAlphaNumeric

"""
    Actions surrounding the apps from the database.
"""
class AppDao:
    """
        Sets up the object with the sql connection.
    """
    def __init__(self, settings):
        self.conn = sqlite3.connect(settings.database)

    """
        Gets the app's details from its shortkey
    """
    def getAppDetails(self, appshortkey):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, appshortkey, name, description, host, owner_id from applications where appshortkey=?", (appshortkey,))
            appRow = cur.fetchone()
            if appRow:
                return {"id": appRow[0], "appshortkey": appRow[1], "name": appRow[2], "description": appRow[3], "host" : appRow[4], "owner": appRow[5]}
            return {"status": "Application short key not found"}

    """
        Gets the app's details from its id
    """
    def getAppDetailsById(self, id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, appshortkey, name, description, host, owner_id from applications where id=?", (id,))
            appRow = cur.fetchone()
            if appRow:
                return {"id": appRow[0], "appshortkey": appRow[1], "name": appRow[2], "description": appRow[3], "host" : appRow[4], "owner": appRow[5]}
            return {"status": "id not found"}
    
    """
        Verifies that if the app not the owner, that they are at least allowed to access it.
    """
    def verifyUserAccessToApp(self, userId, appId, userOwnerChecked=False):
        with self.conn:
            cur = self.conn.cursor()
            if not userOwnerChecked:
                cur.execute("SELECT * from applications where id=? and owner_id=?", (appId, userId))
                appRow = cur.fetchone()
                if appRow:
                    return True
            else:
                cur.execute("SELECT * from applications a inner join applicationAdmins aa on a.id = aa.app_id where a.id=? and aa.user_id=?", (appId, userId))
                appRow = cur.fetchone()
                if appRow:
                    return True
            return False

    """
        Gets the env variables from the appshortkey.
    """
    def getEnvVariables(self, appshortkey):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id from applications where appshortkey=?", (appshortkey,))
            appRow = cur.fetchone()
            if appRow:
                cur.execute("select envVariable, envValue from envVariables where app_id = ?", (appRow[0],))
                envVarRows = cur.fetchall()
                if len(envVarRows) > 0:
                    return {"envVars": list(map(lambda x: {"key": x[0], "value": x[1]}, envVarRows))}
                return {"status": "No Environment Variable found for application id"}
            return {"status": "Application short key not found"}

    """
        Verifies that the authKey is registered to the appshortkey.
    """
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

    """
        Searches up an app by it's name.
    """
    def searchAppByName(self, searchTerm):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, appshortkey, name, description, host from applications where name like ?", ("%" + searchTerm + "%",))
            appRows = cur.fetchall()
            if appRows:
                return list(map(lambda x: App(x[0], x[1], x[2], x[3], x[4]), appRows))

    """
        Creates a new app. Will return -1 and a message if there is any issues with the database.
    """
    def createNewApp(self, user, appname, description, host):
        with self.conn:
            try:
                cur = self.conn.cursor()
                newAppShortKey = randomAlphaNumeric()
                print(newAppShortKey)
                cur.execute("INSERT INTO applications(appshortkey, name, description, host, owner_id) values(?, ?, ?, ?, ?)", (newAppShortKey, appname, description, host, user.id))
                return (cur.lastrowid, newAppShortKey, None)
            except Exception as er:
                return (-1, None, "There was a db issue: " + str(er))