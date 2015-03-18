import unittest

from src.data import AppDao
from src.models import Settings


class TestAppDao(unittest.TestCase):
    def setUp(self):
        self.settings = Settings(":memory:", "test.sql", "localhost", 8080)
        #DatabaseSchemaBootstrap().bootstrap(self.settings)
        self.appDao = AppDao(self.settings)

    def tearDown(self):
        self.appDao.conn.close()

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