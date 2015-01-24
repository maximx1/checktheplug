import random
from bottle import route, template
from models.AppCommonContainer import AppCommonContainer

"""
    The main get endpoint for getting the key to validate system up.
"""
@route('/isLiveKey/<inKey>')
def getIsLiveKey(inKey):
    randKey = random.randint(100000, 999999)
    key = {"key": randKey, "hash": str(randKey) + ":" + inKey}
    return key

@route('/settings')
def showSettings():
    app = AppCommonContainer()
    shownSettings = {"database": app.settings.database, "schema": app.settings.schema, "host": app.settings.hostname, "port": app.settings.port, }
    return shownSettings