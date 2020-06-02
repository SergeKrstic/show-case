import datetime
import mock as Mock
import unittest

import HorizonCore.Configuration as Config
from HorizonCore.Framework.Regulator import Regulator


class RegulatorSpecifications(unittest.TestCase):

    def setUp(self):
        self.testUser = Config.Users[0]
        self.time = datetime.datetime(2016, 11, 8, 14, 00, 12, 18299)

        class fakeDateTime(datetime.datetime):
            @classmethod
            def utcnow(cls):
                return self.time

        patcher = Mock.patch('datetime.datetime', fakeDateTime)
        self.addCleanup(patcher.stop)
        patcher.start()

    def test_SpecifyThatThatRegulatorCanBeConstructed(self):
        # act
        regulator = self.CreateRegulator(numberOfSecondsBetweenUpdates=10)

        # assert
        self.assertEqual(regulator._updatePeriodInSeconds, 10, '_updatePeriod')
        self.assertEqual(regulator._nextUpdateTime,
                         datetime.datetime(2016, 11, 8, 14, 00, 12, 18299), '_nextUpdateTime')

    def test_SpecifyThatWhenRegulatorCanConstructedWithANegativeUpdateRate(self):
        # act
        regulator = self.CreateRegulator(numberOfSecondsBetweenUpdates=-5)

        # assert
        self.assertEqual(regulator._updatePeriodInSeconds, -1, '_updatePeriod')
        self.assertEqual(regulator._nextUpdateTime,
                         datetime.datetime(2016, 11, 8, 14, 00, 12, 18299), '_nextUpdateTime')

    def test_SpecifyThatIsReadyAlwaysReturnsTrueWhenUpdatePeriodIsSetToZero(self):
        # arrange
        regulator = self.CreateRegulator(numberOfSecondsBetweenUpdates=0)

        # assert
        self.assertEqual(regulator.IsReady(), True)

    def test_SpecifyThatIsReadyAlwaysReturnFalseWhenUpdatePeriodIsNegative(self):
        # arrange
        regulator = self.CreateRegulator(numberOfSecondsBetweenUpdates=-3)

        # assert
        self.assertEqual(regulator.IsReady(), False)

    def test_SpecifyThatIsReadyReturnsFalseWhenCurrentTimeLessThanNextUpdateTime(self):
        # arrange
        regulator = self.CreateRegulator(numberOfSecondsBetweenUpdates=10)
        regulator.IsReady()
        self.time = self.time + datetime.timedelta(seconds=2)

        # assert
        self.assertEqual(regulator.IsReady(), False)

    def test_SpecifyThatIsReadyReturnsTrueWhenCurrentTimeExceedsNextUpdateTime(self):
        # arrange
        regulator = self.CreateRegulator(numberOfSecondsBetweenUpdates=10)
        regulator.IsReady()
        self.time = self.time + datetime.timedelta(seconds=12)

        # assert
        self.assertEqual(regulator.IsReady(), True)

    @staticmethod
    def CreateRegulator(numberOfSecondsBetweenUpdates):
        return Regulator(numberOfSecondsBetweenUpdates, updatePeriodVariatorInSeconds=0)
