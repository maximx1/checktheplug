from bottle import run, app
from checktheplug.models.AppCommonContainer import AppCommonContainer
from checktheplug.utilities.DatabaseSchemaBootstrap import DatabaseSchemaBootstrap
from checktheplug.utilities.SettingsUtil import SettingsUtil
from beaker.middleware import SessionMiddleware
import checktheplug.controllers.ApiKeyController
import checktheplug.controllers.PageController

sessionOptions = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': 'config/.session_cache',
    'session.auto ': True
}

if __name__ == "__main__":
    settingsUtil = SettingsUtil()
    settingsUtil.loadSettings()
    appSettings = settingsUtil.loadConfig()
    appContainer = AppCommonContainer()
    appContainer.settings = appSettings
    DatabaseSchemaBootstrap().bootstrap(appContainer.settings)

    app = SessionMiddleware(app(), sessionOptions)

    run(host=appSettings.hostname, port=appSettings.port, app=app)
