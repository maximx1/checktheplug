class Server:
    def __init__(self, id=-1, host="", ipv4=""):
        self.id = id
        self.host = host
        self.ipv4 = ipv4
    
    def toDict(self):
        return self.__dict__
    
    @staticmethod
    def fromDict(serverDict):
        if serverDict and "id" in serverDict and "host" in serverDict and "ipv4" in serverDict:
            return Server(serverDict["id"], serverDict["host"], serverDict["ipv4"])
        return None