import json
import sys
from models.Settings import Settings
"""
    Utilities to load settings.
"""
class SettingsUtil:
    """
        Loads settings file from the fs.
    """
    def loadSettings(self):
        settingsStream = open('config/settings.json')
        self.settingsData = json.load(settingsStream)
        settingsStream.close()

    """
        Loads config into a settings object.
    """
    def loadConfig(self):
        if len(sys.argv) == 1:
            return self.generateConfigItem(self.settingsData["default"])
        else:
            options = {}
            for x in range(1, len(sys.argv)):
                flag = sys.argv[x].split("=")
                options[flag[0]] = flag[1]
            return self.parseFlags(options)

    """
        Generates a settings object from the selected profile.
    """
    def generateConfigItem(self, profile):
        return Settings(profile["database"], profile["schema"], profile["hostname"], profile["port"])

    """
        Parse flags to selectively flesh out config items.
    """
    def parseFlags(self, options):
        settings = self.generateConfigItem(self.settingsData["default"])
        if "-Cconf.profile" in options:
            settings = self.generateConfigItem(self.settingsData[options["-Cconf.profile"]])
        if "-Cconf.database" in options:
            settings.database = options["-Cconf.database"]
        if "-Cconf.schema" in options:
            settings.schema = options["-Cconf.schema"]
        if "-Cconf.hostname" in options:
            settings.hostname = options["-Cconf.hostname"]
        if "-Cconf.port" in options:
            settings.port = options["-Cconf.port"]
        return settings