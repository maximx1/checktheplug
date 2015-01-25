import random
from bottle import route, template, request, get
from models.AppCommonContainer import AppCommonContainer
from data.UserDao import UserDao
from data.AppDao import AppDao

"""
    The main get endpoint for getting the key to validate system up.
"""
@route('/isLiveKey/<inKey>')
def getIsLiveKey(inKey):
    randKey = random.randint(100000, 999999)
    key = {"key": randKey, "hash": str(randKey) + ":" + inKey}
    return key

@get('/getAppDetails/<appshortkey>')
def getAppDetails(appshortkey):
    authKey = request.get_header("authKey")
    if authKey:
        return AppDao(AppCommonContainer().settings).getAppDetails(authKey, appshortkey)
    return {"status": "Unauthorized"}

@route('/settings')
def showSettings():
    app = AppCommonContainer()
    shownSettings = {"database": app.settings.database, "schema": app.settings.schema, "host": app.settings.hostname, "port": app.settings.port, }
    return shownSettings

@route('/login/<username>/<password>')
def testLogin(username, password):
    return UserDao(AppCommonContainer().settings).login(username, password)