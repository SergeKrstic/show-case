import datetime
import mock
import time
import unittest

from HorizonCore.ToolBox.Timer import Timer


class TimerSpecifications(unittest.TestCase):

    def setUp(self):
        self.mockTime = mock.Mock()
        self.mockTime.return_value = time.mktime(datetime.datetime(2011, 6, 21).timetuple())

        patcher = mock.patch('time.time', self.mockTime)
        self.addCleanup(patcher.stop)
        patcher.start()

    def test_SpecifyThatTimerCanBeConstructed(self):
        # act
        timer = Timer()

        # assert
        self.assertEqual(timer.StartTime, 0)

    def test_SpecifyThatTimerCanBeStarted(self):
        timer = Timer()

        # act
        timer.Start()

        # assert
        self.assertEqual(timer.StartTime, 1308614400.0)

    def test_SpecifyThatTimerCanBeStopped(self):
        timer = Timer()
        timer.Start()
        self.mockTime.return_value = self.mockTime.return_value + 2

        # act
        elapsedTime = timer.Stop()

        # assert
        self.assertEqual(elapsedTime, 2.0)


if __name__ == '__main__':
    unittest.main()
