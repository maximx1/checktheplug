import unittest
import sys
from utilities.SettingsUtil import SettingsUtil

class TestSettingsUtil(unittest.TestCase):
    def setUp(self):
        self.settingsUtil = SettingsUtil()
        self.settingsUtil.settingsData = {"default": { "database": "config/checktheplug.db", "schema": "config/default.sql", "hostname": "localhost", "port": 8080}}

    def test_canParseAllFlagsExceptProfile(self):
        flags = ['-Cconf.database', '-Cconf.schema', '-Cconf.hostname', '-Cconf.port']
        values = ['dbname.db', 'schema.sql', 'localhost', 1234]
        options = dict(zip(flags, values))
        settings = self.settingsUtil.parseFlags(options)
        self.assertEquals('dbname.db', settings.database)
        self.assertEquals('schema.sql', settings.schema)
        self.assertEquals('localhost', settings.hostname)
        self.assertEquals(1234, settings.port)

    def test_canParseProfileFlag(self):
        options = {"-Cconf.profile": "testProfile"}
        self.settingsUtil.settingsData["testProfile"] = { "database": "config/checktheplug-test.db", "schema": "config/test.sql", "hostname": "localhost", "port": 8089}
        settings = self.settingsUtil.parseFlags(options)
        self.assertEquals('config/checktheplug-test.db', settings.database)
        self.assertEquals('config/test.sql', settings.schema)
        self.assertEquals('localhost', settings.hostname)
        self.assertEquals(8089, settings.port)

    def test_canGenerateConfigItem(self):
        settings = self.settingsUtil.generateConfigItem(self.settingsUtil.settingsData["default"])
        self.assertEquals('config/checktheplug.db', settings.database)
        self.assertEquals('config/default.sql', settings.schema)
        self.assertEquals('localhost', settings.hostname)
        self.assertEquals(8080, settings.port)

    def test_canBuildDefaultSettingsWithNoCommandLineArgs(self):
        sys.argv = ["checktheplug.py"]
        settings = self.settingsUtil.loadConfig()
        self.assertEquals('config/checktheplug.db', settings.database)
        self.assertEquals('config/default.sql', settings.schema)
        self.assertEquals('localhost', settings.hostname)
        self.assertEquals(8080, settings.port)

    def test_canBuildDefaultSettingsWithOneCommandLineArg(self):
        sys.argv = ["checktheplug.py", "-Cconf.database=config/checktheplug-test.db"]
        settings = self.settingsUtil.loadConfig()
        self.assertEquals('config/checktheplug-test.db', settings.database)
        self.assertEquals('config/default.sql', settings.schema)
        self.assertEquals('localhost', settings.hostname)
        self.assertEquals(8080, settings.port)

    def test_canBuildDefaultSettingsWithMultipleCommandLineArgs(self):
        sys.argv = ["checktheplug.py", "-Cconf.database=config/checktheplug-test.db", "-Cconf.schema=config/test.sql"]
        settings = self.settingsUtil.loadConfig()
        self.assertEquals('config/checktheplug-test.db', settings.database)
        self.assertEquals('config/test.sql', settings.schema)
        self.assertEquals('localhost', settings.hostname)
        self.assertEquals(8080, settings.port)

if __name__ == '__main__':
    unittest.main()