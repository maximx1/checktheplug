from bottle import run, app
from src.models import AppCommonContainer
from src.utilities import DatabaseSchemaBootstrap, SettingsUtil
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
