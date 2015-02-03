import random
from bottle import route, get, auth_basic
from models.AppCommonContainer import AppCommonContainer
from data.UserDao import UserDao
from data.AppDao import AppDao

"""
    Authentication validator
"""
def authenticateBasicAuth(appshortkey, authKey):
    return AppDao(AppCommonContainer().settings).verifyUserAccess(appshortkey, authKey)

"""
    The main get endpoint for getting the key to validate system up.
"""
@route('/isLiveKey/<inKey>')
def getIsLiveKey(inKey):
    randKey = random.randint(100000, 999999)
    return {"key": randKey, "hash": str(randKey) + ":" + inKey}

@get('/getAppDetails/<appshortkey>')
@auth_basic(authenticateBasicAuth)
def getAppDetails(appshortkey):
    return AppDao(AppCommonContainer().settings).getAppDetails(appshortkey)

@route('/settings')
def showSettings():
    app = AppCommonContainer()
    shownSettings = {"database": app.settings.database, "schema": app.settings.schema, "host": app.settings.hostname, "port": app.settings.port, }
    return shownSettings

@route('/getEnvVariables/<appshortkey>')
@auth_basic(authenticateBasicAuth)
def getEnvVariables(appshortkey):
    return AppDao(AppCommonContainer().settings).getEnvVariables(appshortkey)