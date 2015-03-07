import sqlite3
from models.Server import Server

"""
    Operations to manage accessing the server database.
"""
class ServerDao:
    """
        Sets up the object with the sql connection.
    """
    def __init__(self, settings):
        self.conn = sqlite3.connect(settings.database)
        
    """
        Add Server to the database.
    """
    def add(self, newServer):
        if newServer:
            try:
                with self.conn:
                    cur = self.conn.cursor()
                    cur.execute("INSERT INTO servers(host, ipv4) values(?, ?)", (newServer.host, newServer.ipv4))
                    return(Server(cur.lastrowid, newServer.host, newServer.ipv4), None)
            except Exception as er:
                return (None, "There was a db issue: " + str(er))
        else:
            return (None, "No server passed in")