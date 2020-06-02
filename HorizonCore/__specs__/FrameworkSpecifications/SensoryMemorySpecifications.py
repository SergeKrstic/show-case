import datetime
import unittest

from mock import mock

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.SensoryMemory import MemoryRecord, SensoryMemory


class SensoryMemorySpecifications(unittest.TestCase):

    def setUp(self):
        self.time = datetime.datetime(2016, 11, 8, 14, 00, 12, 18299)

        class fakeDateTime(datetime.datetime):
            @classmethod
            def utcnow(cls):
                return self.time

        patcher = mock.patch('datetime.datetime', fakeDateTime)
        self.addCleanup(patcher.stop)
        patcher.start()

    def test_SpecifyThatMemoryRecordCanBeConstructed(self):
        # arrange
        expectedTimeLastSensed = datetime.datetime(2018, 3, 19, 11, 30)
        expectedTimeBecameVisible = datetime.datetime(2018, 3, 19, 11, 31)
        expectedTimeLastVisible = datetime.datetime(2018, 3, 19, 11, 32)
        expectedLastSensedPosition = datetime.datetime(2018, 3, 19, 11, 33)

        # act
        memoryRecord = MemoryRecord()

        # assert
        self.assertEqual(None, memoryRecord.TimeLastSensed)
        self.assertEqual(None, memoryRecord.TimeBecameVisible)
        self.assertEqual(None, memoryRecord.TimeLastVisible)
        self.assertEqual(None, memoryRecord.LastSensedPosition)

        # act
        memoryRecord.TimeLastSensed = expectedTimeLastSensed
        memoryRecord.TimeBecameVisible = expectedTimeBecameVisible
        memoryRecord.TimeLastVisible = expectedTimeLastVisible
        memoryRecord.LastSensedPosition = expectedLastSensedPosition

        self.assertEqual(expectedTimeLastSensed, memoryRecord.TimeLastSensed)
        self.assertEqual(expectedTimeBecameVisible, memoryRecord.TimeBecameVisible)
        self.assertEqual(expectedTimeLastVisible, memoryRecord.TimeLastVisible)
        self.assertEqual(expectedLastSensedPosition, memoryRecord.LastSensedPosition)

    def test_SpecifyThatSensoryMemoryCanBeConstructed(self):
        # act
        testBot = self.CreateTestBot()
        memorySpan = datetime.timedelta(minutes=30)
        sensoryMemory = SensoryMemory(testBot, memorySpan)

        # assert
        self.assertEqual(testBot, sensoryMemory.Owner)
        self.assertEqual(memorySpan, sensoryMemory.MemorySpan)
        self.assertEqual(0, len(sensoryMemory._memoryMap))

    def test_SpecifyThatSensoryMemoryCanBeUpdatedWithANewEvent(self):
        # arrange
        sensoryMemory = self.CreateTestSensoryMemory()

        # act
        sensoryMemory.Update("firstEvent")

        # assert
        memoryRecord = sensoryMemory._getMemoryRecord("firstEvent")
        self.assertEqual(self.time, memoryRecord.TimeLastSensed, "TimeLastSensed")
        self.assertEqual(self.time, memoryRecord.TimeBecameVisible, "TimeBecameVisible")
        self.assertEqual(self.time, memoryRecord.TimeLastVisible, "TimeLastVisible")
        self.assertEqual(None, memoryRecord.LastSensedPosition, "LastSensedPosition")

    def test_SpecifyThatAnEventCanBeRemovedFromSensoryMemory(self):
        # arrange
        sensoryMemory = self.CreateTestSensoryMemory()

        # act
        sensoryMemory.Update("firstEvent")

        # assert
        self.assertEqual(1, len(sensoryMemory._memoryMap))

        # act
        sensoryMemory.RemoveEventFromMemory("firstEvent")

        # assert
        self.assertEqual(0, len(sensoryMemory._memoryMap))

    def test_SpecifyThatEventLocationWithinRangeRaiseNotImplementedError(self):
        # arrange
        sensoryMemory = self.CreateTestSensoryMemory()

        # assert
        self.assertRaises(NotImplementedError, sensoryMemory.IsEventLocationWithinRange, "firstEvent")

    def test_SpecifyThatAMemoryRecordCanBeRetrieved(self):
        # arrange
        sensoryMemory = self.CreateTestSensoryMemory()
        sensoryMemory.Update("firstEvent")

        # act
        memoryRecord = sensoryMemory._getMemoryRecord("firstEvent")

        # assert
        self.assertIsNotNone(memoryRecord)
        self.assertEqual(self.time, memoryRecord.TimeLastSensed, "TimeLastSensed")

    def test_SpecifyThatAnExceptionIsRaisedWhenTryingToRetrieveAnNonExistRecord(self):
        # arrange
        sensoryMemory = self.CreateTestSensoryMemory()
        sensoryMemory.Update("firstEvent")

        # assert
        self.assertRaises(Exception, sensoryMemory._getMemoryRecord, "non-existing-event")

    def test_SpecifyThatLastRecordedPositionOfEventLocationCanBeRetrieved(self):
        # arrange
        sensoryMemory = self.CreateTestSensoryMemory()
        sensoryMemory.Update("firstEvent")

        # assert
        self.assertEqual(None, sensoryMemory.GetLastRecordedPositionOfEventLocation("firstEvent"))

    def test_SpecifyThatTimeEventLocationHasBeenVisibleCanBeRetrieved(self):
        # arrange
        sensoryMemory = self.CreateTestSensoryMemory()
        sensoryMemory.Update("firstEvent")

        # assert
        self.assertEqual(self.time, sensoryMemory.GetTimeEventLocationHasBeenVisible("firstEvent"))

    def test_SpecifyThatTimeSinceEventWasLastSensedCanBeRetrieved(self):
        # arrange
        sensoryMemory = self.CreateTestSensoryMemory()
        sensoryMemory.Update("firstEvent")

        # assert
        self.assertEqual(self.time, sensoryMemory.GetTimeSinceEventWasLastSensed("firstEvent"))

    def test_SpecifyThatTimeEventLocationHasBeenOutOfViewCanBeRetrieved(self):
        # arrange
        sensoryMemory = self.CreateTestSensoryMemory()
        sensoryMemory.Update("firstEvent")
        self.time = datetime.datetime(2016, 11, 8, 14, 15, 12, 18299)

        # assert
        self.assertEqual(datetime.timedelta(minutes=15), sensoryMemory.GetTimeEventLocationHasBeenOutOfView("firstEvent"))

    def test_SpecifyThatAListOfRecentlySensedEventsCanBeRetrieved(self):
        # arrange
        sensoryMemory = self.CreateTestSensoryMemory()
        self.time = datetime.datetime(2016, 11, 8, 14, 00, 12, 18299)
        sensoryMemory.Update("event1")
        self.time = datetime.datetime(2016, 11, 8, 14, 15, 12, 18299)
        sensoryMemory.Update("event2")
        self.time = datetime.datetime(2016, 11, 8, 14, 30, 12, 18299)
        sensoryMemory.Update("event3")

        # act
        self.time = datetime.datetime(2016, 11, 8, 14, 40, 12, 18299)
        recentMemory = sensoryMemory.GetListOfRecentlySensedEvents()

        # assert
        self.assertEqual(2, len(recentMemory))

    # Creation methods
    # ==================================================================================================================

    @staticmethod
    def CreateTestBot():
        BaseEntity.ResetNextValidId()
        return TestBot(1)

    @staticmethod
    def CreateTestSensoryMemory():
        testBot = SensoryMemorySpecifications.CreateTestBot()
        memorySpan = datetime.timedelta(minutes=30)
        return SensoryMemory(testBot, memorySpan)


# Helper classes
# ======================================================================================================================

class TestBot(BaseEntity):

    def Update(self):
        pass

    def HandleTelegram(self, telegram):
        pass
