import unittest
import os
from data.AppDao import AppDao
from models.Settings import Settings
from utilities.DatabaseSchemaBootstrap import DatabaseSchemaBootstrap

class TestAppDao(unittest.TestCase):
    def setUp(self):
        self.settings = Settings("checktheplug-test.db", "test.sql", "localhost", 8080)
        # self.deleteTestDb()
        # DatabaseSchemaBootstrap().bootstrap(self.settings)
        self.appDao = AppDao(self.settings)

    #def tearDown(self):
        # self.deleteTestDb()

    def deleteTestDb(self):
        if os.path.isfile(self.settings.database):
            os.remove(self.settings.database)

    def test_canFindLeftoverPortWhenMultipleAreAvailable(self):
        usedPorts = list(range(9700,9790))
        leftoverPort = self.appDao.calculateNextPort(usedPorts)
        self.assertTrue(leftoverPort in list(range(9790, 9800)))

    def test_canFindLeftoverPortWhenOnlyOneIsAvailable(self):
        usedPorts = list(range(9700,9799))
        leftoverPort = self.appDao.calculateNextPort(usedPorts)
        self.assertEquals(leftoverPort, 9799)

    def test_canReturnNoneWhenThereAreNoPortsAvailable(self):
        usedPorts = list(range(9700,9800))
        leftoverPort = self.appDao.calculateNextPort(usedPorts)
        self.assertIsNone(leftoverPort)

if __name__ == '__main__':
    unittest.main()