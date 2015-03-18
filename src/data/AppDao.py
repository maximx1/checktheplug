import sqlite3

from src.models.App import App
from utilities.StringOps import random_alpha_numeric


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
    def get_app_details(self, appshortkey):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, appshortkey, name, description, host, owner_id from applications where appshortkey=?", (appshortkey,))
            app_row = cur.fetchone()
            if app_row:
                return {"id": app_row[0], "appshortkey": app_row[1], "name": app_row[2], "description": app_row[3], "host" : app_row[4], "owner": app_row[5]}
            return {"status": "Application short key not found"}

    """
        Gets the app's details from its id
    """
    def get_app_details_by_id(self, id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, appshortkey, name, description, host, owner_id from applications where id=?", (id,))
            app_row = cur.fetchone()
            if app_row:
                return {"id": app_row[0], "appshortkey": app_row[1], "name": app_row[2], "description": app_row[3], "host" : app_row[4], "owner": app_row[5]}
            return {"status": "id not found"}
    
    """
        Verifies that if the app not the owner, that they are at least allowed to access it.
    """
    def verify_user_access_to_app(self, user_id, app_id, user_owner_checked=False):
        with self.conn:
            cur = self.conn.cursor()
            if not user_owner_checked:
                cur.execute("SELECT * from applications where id=? and owner_id=?", (app_id, user_id))
                app_row = cur.fetchone()
                if app_row:
                    return True
            else:
                cur.execute("SELECT * from applications a inner join applicationAdmins aa on a.id = aa.app_id where a.id=? and aa.user_id=?", (app_id, user_id))
                app_row = cur.fetchone()
                if app_row:
                    return True
            return False

    """
        Gets the env variables from the appshortkey.
    """
    def get_env_variables(self, appshortkey):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id from applications where appshortkey=?", (appshortkey,))
            app_row = cur.fetchone()
            if app_row:
                cur.execute("select envVariable, envValue from envVariables where app_id = ?", (app_row[0],))
                env_var_rows = cur.fetchall()
                if len(env_var_rows) > 0:
                    return {"envVars": list(map(lambda x: {"key": x[0], "value": x[1]}, env_var_rows))}
                return {"status": "No Environment Variable found for application id"}
            return {"status": "Application short key not found"}

    """
        Verifies that the authKey is registered to the appshortkey.
    """
    def verify_user_access(self, auth_key):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("select authKey from authKeys where authKey = ?", (auth_key,))
            app_row = cur.fetchone()
            return True if app_row else False

    """
        Determines which ports are left available out of the range allotted
        * range is set to 9700 - 9799 inclusive. Likely each server isn't going to be hosting 100 apps
    """
    def calculate_next_port(self, used_ports):
        port_range = set(range(9700, 9800))
        ports_left = port_range - set(used_ports)
        return ports_left.pop() if ports_left else None

    """
        Searches up an app by it's name.
    """
    def search_apps_by_name(self, search_term):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, appshortkey, name, description, host from applications where name like ?", ("%" + search_term + "%",))
            app_row = cur.fetchall()
            if app_row:
                return list(map(lambda x: App(x[0], x[1], x[2], x[3], x[4], None), app_row))

    """
        Creates a new app. Will return -1 and a message if there is any issues with the database.
    """
    def create_new_app(self, user, appname, description, host, dockerfile):
        with self.conn:
            try:
                cur = self.conn.cursor()
                new_app_short_key = random_alpha_numeric()
                cur.execute("INSERT INTO applications(appshortkey, name, description, host, owner_id, dockerfile) values(?, ?, ?, ?, ?, ?)", (new_app_short_key, appname, description, host, user.id, dockerfile))
                return (cur.lastrowid, new_app_short_key, None)
            except Exception as er:
                return (-1, None, "There was a db issue: " + str(er))
            
    """
        Grabs just the dockerfile base64 code from the database.
    """
    def get_app_dockerfile(self, appshortkey):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT dockerfile from applications where appshortkey = ?", (appshortkey,))
            dockerfile_row = cur.fetchone()
            return dockerfile_row[0] if dockerfile_row else ""