class Server:
    def __init__(self, id=-1, host="", url="", app_id=None):
        self.id = id
        self.host = host
        self.url = url
        self.app_id=app_id
    
    def to_dict(self):
        return self.__dict__
    
    @staticmethod
    def from_dict(server_dict):
        if server_dict and "id" in server_dict and "host" in server_dict and "url" in server_dict:
            return Server(server_dict["id"], server_dict["host"], server_dict["url"])
        return None