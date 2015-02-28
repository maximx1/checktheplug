import random
from bottle import route, get, auth_basic, request
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
@route('/api/test/<inKey>')
def getIsLiveKey(inKey):
    randKey = random.randint(100000, 999999)
    return {"key": randKey, "hash": str(randKey) + ":" + inKey}

@get('/api/app/key/<appshortkey>')
@auth_basic(authenticateBasicAuth)
def getAppDetails(appshortkey):
    return AppDao(AppCommonContainer().settings).getAppDetails(appshortkey)

@get('/api/app/id/<id>')
@auth_basic(authenticateBasicAuth)
def getAppDetailsById(id):
    return AppDao(AppCommonContainer().settings).getAppDetailsById(id)

@route('/settings')
def showSettings():
    app = AppCommonContainer()
    shownSettings = {"database": app.settings.database, "schema": app.settings.schema, "host": app.settings.hostname, "port": app.settings.port, }
    return shownSettings

@route('/api/app/env/vars/<appshortkey>')
@auth_basic(authenticateBasicAuth)
def getEnvVariables(appshortkey):
    return AppDao(AppCommonContainer().settings).getEnvVariables(appshortkey)

@route('/api/app/search/', method='POST')
def getAppsByName():
    searchTerm = request.json['searchTerm']
    apps = AppDao(AppCommonContainer().settings).searchAppsByName(searchTerm)
    if apps:
        return {"status": "ok", "apps": list(map(lambda x: x.toDict(), apps))}
    return {"status": "none"}