class Server:
    def __init__(self, id=-1, host="", ipv4=""):
        self.id = id
        self.host = host
        self.ipv4 = ipv4
    
    def toDict(self):
        return {"id": self.id, "host": self.host, "ipv4": self.ipv4}