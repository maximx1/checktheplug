import random

class ApiKeyController:
    """
        The main get endpoint for getting the key to validate system up.
    """
    def getIsLiveKey(self, inKey):
        randKey = random.randint(100000, 999999)
        key = {"key": randKey, "hash": str(randKey) + inKey}
        return key
