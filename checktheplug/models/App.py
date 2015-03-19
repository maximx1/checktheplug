class App:
    def __init__(self, id, appshortkey, name, description, host, dockerfile_template):
        self.id = id
        self.appshortkey = appshortkey
        self.name = name
        self.description = description
        self.host = host
        self.dockerfile_template = dockerfile_template
    
    def to_dict(self):
        return self.__dict__