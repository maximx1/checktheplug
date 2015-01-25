from bottle import run
from controllers import *
from utilities.SettingsUtil import SettingsUtil
from models.AppCommonContainer import AppCommonContainer
from utilities.DatabaseSchemaBootstrap import DatabaseSchemaBootstrap

if __name__ == "__main__":
    settingsUtil = SettingsUtil()
    appSettings = settingsUtil.loadConfig()
    app = AppCommonContainer()
    app.settings = appSettings
    DatabaseSchemaBootstrap().bootstrap(app)
    run(host=appSettings.hostname, port=appSettings.port)