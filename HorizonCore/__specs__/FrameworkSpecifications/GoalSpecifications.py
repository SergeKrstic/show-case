import unittest

from HorizonCore.Framework.Goal import Goal, GoalStatus


class GoalSpecifications(unittest.TestCase):

    DefaultOwner = 1
    DefaultGoalType = 2

    def test_SpecifyThatThatGoalCanBeConstructed(self):
        # act
        goal = self.CreateGoal()

        # assert
        self.assertEqual(goal.Owner, self.DefaultGoalType, 'Owner')
        self.assertEqual(goal.Type, self.DefaultGoalType, 'Type')
        self.assertEqual(goal.Status, GoalStatus.Inactive, 'Status')

        self.assertEqual(goal.IsComplete(), False, 'IsComplete')
        self.assertEqual(goal.IsActive(), False, 'IsActive')
        self.assertEqual(goal.IsInactive(), True, 'IsInactive')
        self.assertEqual(goal.HasFailed(), False, 'HasFailed')

    def test_SpecifyThatActivateRaisesNotImplementedError(self):
        # arrange
        goal = self.CreateGoal()

        # assert
        self.assertRaises(NotImplementedError, goal.Activate)

    def test_SpecifyThatProcessRaisesNotImplementedError(self):
        # arrange
        goal = self.CreateGoal()

        # assert
        self.assertRaises(NotImplementedError, goal.Process)

    def test_SpecifyThatTerminateRaisesNotImplementedError(self):
        # arrange
        goal = self.CreateGoal()

        # assert
        self.assertRaises(NotImplementedError, goal.Terminate)

    def test_SpecifyThatAddSubGoalRaisesAnException(self):
        # arrange
        goal = self.CreateGoal()

        # assert
        self.assertRaises(Exception, goal.AddSubGoal, None)

    def test_SpecifyThatHandleTelegramReturnsFalse(self):
        # arrange
        goal = self.CreateGoal()

        # assert
        self.assertEqual(goal.HandleTelegram(None), False)

    def test_SpecifyThatActivateIfInactiveFunctionsCorrectly(self):
        # arrange
        goal = self.CreateTestGoal()

        # assert
        self.assertEqual(goal.Status, GoalStatus.Inactive)

        # act
        goal._activateIfInactive()

        # assert
        self.assertEqual(goal.ActiveWasCalled, True)

    def test_SpecifyThatTheGoalCanBeReactivateIfItHasFailed(self):
        # arrange
        goal = self.CreateTestGoal()

        goal._status = GoalStatus.Failed

        # act
        goal._reactivateIfFailed()

        # assert
        self.assertEqual(goal.Status, GoalStatus.Inactive)

    # Helper methods
    # ==================================================================================================================

    def CreateGoal(self):
        return Goal(owner=self.DefaultGoalType, goalType=self.DefaultGoalType)

    @staticmethod
    def CreateTestGoal():
        class TestGoal(Goal):
            ActiveWasCalled = False

            def Process(self):
                pass

            def Activate(self):
                self.ActiveWasCalled = True

            def Terminate(self):
                pass

        return TestGoal(None, None)
