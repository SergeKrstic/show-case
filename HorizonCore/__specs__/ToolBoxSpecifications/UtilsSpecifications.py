import datetime
from mock import *
import time
import unittest

from HorizonCore.ToolBox.Utils import Utils


mockTime = Mock()
mockTime.return_value = time.mktime(datetime.datetime(2011, 6, 21, 10, 15, 30).timetuple())


class UtilsSpecifications(unittest.TestCase):

    def test_SpecifyThatLengthOfTimeCanBeConvertedIntoSeconds(self):
        self.assertEqual(Utils.ConvertTimeLengthToSeconds(1, 'second'), 1)
        self.assertEqual(Utils.ConvertTimeLengthToSeconds(3, 'seconds'), 3)

        self.assertEqual(Utils.ConvertTimeLengthToSeconds(1, 'minute'), 60)
        self.assertEqual(Utils.ConvertTimeLengthToSeconds(3, 'minutes'), 180)
        self.assertEqual(Utils.ConvertTimeLengthToSeconds(3.5, 'minutes'), 210)

        self.assertEqual(Utils.ConvertTimeLengthToSeconds(1, 'hour'), 3600)
        self.assertEqual(Utils.ConvertTimeLengthToSeconds(3, 'hours'), 10800)
        self.assertEqual(Utils.ConvertTimeLengthToSeconds(3.5, 'hours'), 12600)

        self.assertEqual(Utils.ConvertTimeLengthToSeconds(1, 'day'), 86400)
        self.assertEqual(Utils.ConvertTimeLengthToSeconds(3, 'days'), 259200)
        self.assertEqual(Utils.ConvertTimeLengthToSeconds(3.5, 'days'), 302400)

    def test_SpecifyThatAnExceptionIsRaisedWhenConvertingTimeLengthStringUsingAnInvalidUnit(self):
        self.assertRaises(Exception, Utils.ConvertTimeLengthToSeconds, 5.5, 'invalid unit')

    @patch('HorizonCore.ToolBox.Utils.time.sleep', return_value=None)
    def test_SpecifyThatUtilsCanSleepForGivenLengthOfTime(self, patched_time_sleep):

        # execute
        Utils.SleepFor(3, 'seconds')

        # verify
        self.assertEqual(1, patched_time_sleep.call_count)
        patched_time_sleep.assert_called_with(3)

    def test_SpecifyThatAListOfIndicesCanBeShuffled(self):
        import random

        # setup
        random.seed(101)
        numberOfIndices = 8

        # execute
        shuffledIndices = Utils.GetShuffledIndices(numberOfIndices)

        # verify
        self.assertEqual(len(shuffledIndices), numberOfIndices, "numberOfIndices")
        self.assertEqual([1, 6, 5, 0, 7, 2, 4, 3], shuffledIndices, 'shuffledIndices')

    def test_SpecifyThatTimeCanBeRangedChecked(self):
        # arrange
        onTimeDay = datetime.time(8, 30)  # 8:30 am
        offTimeDay = datetime.time(22, 45)  # 10:45 pm

        onTimeNight = datetime.time(22, 45)  # 10:45 pm
        offTimeNight = datetime.time(8, 30)  # 8:30 am

        # assert
        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(8, 29), onTimeDay, offTimeDay), False)
        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(8, 30), onTimeDay, offTimeDay), True)
        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(10, 00), onTimeDay, offTimeDay), True)
        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(22, 44), onTimeDay, offTimeDay), True)
        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(22, 45), onTimeDay, offTimeDay), False)

        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(22, 44), onTimeNight, offTimeNight), False)
        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(22, 45), onTimeNight, offTimeNight), True)
        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(23, 30), onTimeNight, offTimeNight), True)
        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(8, 29), onTimeNight, offTimeNight), True)
        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(8, 30), onTimeNight, offTimeNight), False)

        self.assertEqual(Utils.IsTimeWithinSchedule(datetime.time(8, 31), onTimeNight, onTimeNight), False)

    @patch('time.time', mockTime)
    def test_SpecifyThatLocalTimeCanBeRetrieved(self):
        self.assertEqual('Tue Jun 21 10:15:30 2011', Utils.GetLocalTime())

    def test_SpecifyThatTimeCanBeCreatedFromString(self):
        timeString = "06:15"
        self.assertEqual(type(Utils.TimeFromString(timeString)), datetime.time)
        self.assertEqual(Utils.TimeFromString(timeString), datetime.time(6, 15))

    def test_SpecifyThatTimeCanBeConvertedToString(self):
        timeObject = datetime.time(6, 15)
        self.assertEqual(type(Utils.TimeToString(timeObject)), type('string'))
        self.assertEqual(Utils.TimeToString(timeObject), "06:15")

    def test_SpecifyThatTimeCanBeAdjusted(self):
        timeObject = datetime.time(6, 15)
        self.assertEqual(str(Utils.AdjustTime(timeObject, 3, 4, 5)), "09:19:05")

    def test_SpecifyThatDecimalValuesCanBeCompared(self):
        value = 1.23456789
        self.assertEqual(Utils.IsEqual(value, value + Utils.EPSILON / 2), True)
        self.assertEqual(Utils.IsEqual(value, value + Utils.EPSILON * 2), False)

    def test_SpecifyThatDateTimeCanBeCreatedFromString(self):
        dateTimeString = "2018-07-12 03:07:11"
        self.assertEqual(type(Utils.DateTimeFromString(dateTimeString)), datetime.datetime)
        self.assertEqual(Utils.DateTimeFromString(dateTimeString), datetime.datetime(2018, 7, 12, 3, 7, 11))

    def test_SpecifyThatDateTimeCanBeConvertedToString(self):
        dateTimeObject = datetime.datetime(2018, 7, 12, 3, 7, 11)
        self.assertEqual(type(Utils.DateTimeToString(dateTimeObject)), type('string'))
        self.assertEqual(Utils.DateTimeToString(dateTimeObject), "2018-07-12 03:07:11")

    def test_SpecifyThatDateCanBeCreatedFromString(self):
        dateString = "2018-07-11"
        self.assertEqual(type(Utils.DateFromString(dateString)), datetime.date)
        self.assertEqual(Utils.DateFromString(dateString), datetime.date(2018, 7, 11))

    def test_SpecifyThatDateCanBeConvertedToString(self):
        dateObject = datetime.datetime(2018, 7, 11).date()
        self.assertEqual(type(Utils.DateToString(dateObject)), type('string'))
        self.assertEqual(Utils.DateToString(dateObject), "2018-07-11")

    @patch('HorizonCore.ToolBox.Utils.pprint', create=True)
    def test_SpecifyThatDebugPrintCanWriteADictionaryToConsole(self, print_):
        Utils.DEBUG_PRINT_ENABLED = True
        Utils.DebugPrint({"Message": "Sample debug message"})
        print_.assert_called_with({'Message': 'Sample debug message'})

    @patch('HorizonCore.ToolBox.Utils.print', create=True)
    def test_SpecifyThatDebugPrintCanWriteAMessageToConsole(self, print_):
        Utils.DEBUG_PRINT_ENABLED = True
        Utils.DebugPrint("Sample debug message")
        print_.assert_called_with("Sample debug message")
