import random
from bottle import get, post, auth_basic, request
from checktheplug.models.AppCommonContainer import AppCommonContainer
from checktheplug.models.Server import Server
from checktheplug.data.AppDao import AppDao
from checktheplug.data.ServerDao import ServerDao
from checktheplug.models.BasicResponse import BasicResponse

"""
    Authentication validator
"""
def authenticate_basic_auth(key_part_one, key_part_two):
    print(key_part_one+key_part_two)
    return AppDao(AppCommonContainer().settings).verify_user_access(key_part_one + key_part_two)

"""
    Authenticate Application server
"""
def authenticate_server(id, key):
    return True

"""
    The main get endpoint for getting the key to validate system up.
"""
@get('/api/test/<inKey>')
def get_is_live_key(inKey):
    randKey = random.randint(100000, 999999)
    return BasicResponse(randKey, "hash" + str(randKey) + ":" + inKey)

@post('/api/app/lookup')
@auth_basic(authenticate_basic_auth)
def get_app_details():
    appshortkey, _ = request.auth or (None, None)
    if request.json:
        id = request.json.get('id', None)
        if id:
            return AppDao(AppCommonContainer().settings).get_app_details_by_id(id)
    return AppDao(AppCommonContainer().settings).get_app_details(appshortkey)

@get('/settings')
def show_settings():
    app = AppCommonContainer()
    shownSettings = {"database": app.settings.database, "schema": app.settings.schema, "host": app.settings.hostname, "port": app.settings.port, }
    return shownSettings

@post('/api/app/env/vars')
@auth_basic(authenticate_basic_auth)
def get_env_variables():
    appshortkey, _ = request.auth or (None, None)
    return AppDao(AppCommonContainer().settings).get_env_variables(appshortkey)

@post('/api/app/search')
def get_apps_by_name():
    search_term = request.json['searchTerm']
    apps = AppDao(AppCommonContainer().settings).search_apps_by_name(search_term)
    if apps:
        return {"status": "ok", "apps": list(map(lambda x: x.to_dict(), apps))}
    return BasicResponse("none", "Search term not found")

@get('/api/app/files/docker')
@auth_basic(authenticate_basic_auth)
def get_app_dockerfile():
    appshortkey, _ = request.auth or (None, None)
    dockerfile = AppDao(AppCommonContainer().settings).get_app_dockerfile(appshortkey)
    return {"dockerfile": dockerfile}

@post('/api/server/new')
@auth_basic(authenticate_server)
def add_new_server():
    if not request.json:
        return {"status": "error", "message": "No json data found"}
    server = Server.from_dict(request.json)
    if server:
        ServerDao(AppCommonContainer().settings).add(server)
        return BasicResponse("ok").to_dict()
    return BasicResponse("error", "Sent data incorrect").to_dict()