from bottle import run, app
from controllers import *
from utilities.SettingsUtil import SettingsUtil
from models.AppCommonContainer import AppCommonContainer
from utilities.DatabaseSchemaBootstrap import DatabaseSchemaBootstrap
from beaker.middleware import SessionMiddleware

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
