import random
from bottle import route, template

"""
    The main get endpoint for getting the key to validate system up.
"""
@route('/isLiveKey/<inKey>')
def getIsLiveKey(inKey):
    randKey = random.randint(100000, 999999)
    key = {"key": randKey, "hash": str(randKey) + ":" + inKey}
    return key
