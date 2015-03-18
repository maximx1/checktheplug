class BasicResponse:
    def __init__(self, status="", message=""):
        self.status = status
        self.message = message

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(basicResponseDict):
        if basicResponseDict and "id" in basicResponseDict and "host" in basicResponseDict and "ipv4" in basicResponseDict:
            return BasicResponse(basicResponseDict["id"], basicResponseDict["host"], basicResponseDict["ipv4"])
        return None