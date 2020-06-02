import unittest
import mock

from HorizonCore.Framework.BaseEngine import BaseEngine
from HorizonCore.ToolBox.Utils import Utils


class AgileEngineSpecifications(unittest.TestCase):

    def setUp(self):
        self._originalSleepForFunction = Utils.SleepFor
        Utils.SleepFor = mock.Mock()

    def tearDown(self):
        Utils.SleepFor = self._originalSleepForFunction

    def test_SpecifyThatBaseEngineCanBeConstructed(self):
        baseEngine = BaseEngine()

        self.assertEqual('BaseEngine', baseEngine.GetEngineName(), 'GetEngineName')
        self.assertEqual(1, baseEngine.EngineCylinderDelayInSeconds, 'EngineCylinderDelayInSeconds')
        self.assertEqual(5, baseEngine.EngineRestartDelayInSeconds, 'EngineRestartDelayInSeconds')

    def test_SpecifyThatTestEngineCanBeConstructed(self):
        testEngine = self.CreateTestEngine()

        self.assertEqual('TestEngine', testEngine.GetEngineName())

    def test_SpecifyThatFireEngineCylindersRaisesNotImplementedError(self):
        # arrange
        engine = BaseEngine()

        # assert
        self.assertRaises(NotImplementedError, engine.FireEngineCylinders)

    def test_SpecifyThatEngineIsAlwaysRunning(self):
        # arrange
        engine = BaseEngine()

        # assert
        self.assertEqual(True, engine.EngineIsRunning())

    def test_SpecifyThatEngineFailuresCanBeHandled(self):
        # arrange
        Utils.NotifyAdminOfSystemEvent = mock.Mock()
        Utils.SleepFor = mock.Mock()

        engine = self.CreateTestEngine()

        # act
        engine.HandleEngineFailure(Exception())

        # assert
        self.assertEqual(
            "[call('Error message: TestEngine has crashed...'), call('Error details: ()')]",
            str(Utils.NotifyAdminOfSystemEvent.call_args_list)
        )

        self.assertEqual(
            "[call(5, 'seconds')]",
            str(Utils.SleepFor.call_args_list)
        )

    def test_SpecifyThatEngineCanRun(self):
        # arrange
        engine = self.CreateTestEngine()
        engine.FireEngineCylinders = mock.Mock()

        # act
        engine.Run()

        # assert
        self.assertEqual(True, engine.FireEngineCylinders.called)
        self.assertEqual(1, engine.FireEngineCylinders.call_count)
        self.assertEqual("[call(1, 'seconds')]", str(Utils.SleepFor.call_args_list))

    def test_SpecifyThatEngineFailuresCanBeHandledWhileRunning(self):
        # arrange
        engine = self.CreateTestEngine()
        engine.FireEngineCylinders = lambda: 1/0
        engine.HandleEngineFailure = mock.Mock()

        # act
        engine.Run()

        # assert
        self.assertEqual(True, engine.HandleEngineFailure.called)
        self.assertEqual(1, engine.HandleEngineFailure.call_count)

    # Creation methods
    # ==================================================================================================================

    @staticmethod
    def CreateTestEngine():
        class TestEngine(BaseEngine):
            def FireEngineCylinders(self):
                pass

        engine = TestEngine()
        engine.EngineIsRunning = mock.Mock()
        engine.EngineIsRunning.side_effect = [True, False]

        return engine
