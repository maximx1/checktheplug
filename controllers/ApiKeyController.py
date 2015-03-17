import random
from bottle import get, post, auth_basic, request
from models.AppCommonContainer import AppCommonContainer
from models.Server import Server
from data.UserDao import UserDao
from data.AppDao import AppDao
from data.ServerDao import ServerDao
from models.BasicResponse import BasicResponse

"""
    Authentication validator
"""
def authenticateBasicAuth(appshortkey, authKey):
    return AppDao(AppCommonContainer().settings).verifyUserAccess(appshortkey, authKey)

"""
    Authenticate Application server
"""
def authenticateServer(id, key):
    return True

"""
    The main get endpoint for getting the key to validate system up.
"""
@get('/api/test/<inKey>')
def getIsLiveKey(inKey):
    randKey = random.randint(100000, 999999)
    return BasicResponse(randKey, "hash" + str(randKey) + ":" + inKey)

@post('/api/app/lookup')
@auth_basic(authenticateBasicAuth)
def getAppDetails():
    appshortkey, _ = request.auth or (None, None)
    if request.json:
        id = request.json.get('id', None)
        if id:
            result = AppDao(AppCommonContainer().settings).getAppDetailsById(id)
            retrievedAppShortKey = result.get('appshortkey', None)
            if retrievedAppShortKey and appshortkey != retrievedAppShortKey:
                return {"status": "appshortkey doesn't belong to id"}
            return result
    return AppDao(AppCommonContainer().settings).getAppDetails(appshortkey)

@get('/settings')
def showSettings():
    app = AppCommonContainer()
    shownSettings = {"database": app.settings.database, "schema": app.settings.schema, "host": app.settings.hostname, "port": app.settings.port, }
    return shownSettings

@post('/api/app/env/vars')
@auth_basic(authenticateBasicAuth)
def getEnvVariables():
    appshortkey, _ = request.auth or (None, None)
    return AppDao(AppCommonContainer().settings).getEnvVariables(appshortkey)

@post('/api/app/search')
def getAppsByName():
    searchTerm = request.json['searchTerm']
    apps = AppDao(AppCommonContainer().settings).searchAppsByName(searchTerm)
    if apps:
        return {"status": "ok", "apps": list(map(lambda x: x.toDict(), apps))}
    return BasicResponse("none", "Search term not found")

@get('/api/app/files/docker')
@auth_basic(authenticateBasicAuth)
def getAppDockerfile():
    appshortkey, _ = request.auth or (None, None)
    dockerfile = AppDao(AppCommonContainer().settings).getAppDockerfile(appshortkey)
    return {"dockerfile": dockerfile}

@post('/api/server/new')
@auth_basic(authenticateServer)
def add_new_server():
    if not request.json:
        return {"status": "error", "message": "No json data found"}
    server = Server.from_dict(request.json)
    if server:
        ServerDao(AppCommonContainer().settings).add(server)
        return BasicResponse("ok").toDict()
    return BasicResponse("error", "Sent data incorrect").toDict()