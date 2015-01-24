from bottle import run
from controllers import *
from utilities.SettingsUtil import SettingsUtil
from models.AppCommonContainer import AppCommonContainer

if __name__ == "__main__":
    settingsUtil = SettingsUtil()
    appSettings = settingsUtil.buildConfig()
    app = AppCommonContainer()
    app.settings = appSettings
    run(host=appSettings.hostname, port=appSettings.port)