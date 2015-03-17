class App:
    def __init__(self, id, appshortkey, name, description, host, dockerfileTemplate):
        self.id = id
        self.appshortkey = appshortkey
        self.name = name
        self.description = description
        self.host = host
        self.dockerfileTemplate = dockerfileTemplate
    
    def toDict(self):
        return {"id": self.id, "appshortkey": self.appshortkey, "name": self.name, "description": self.description, "host": self.host}