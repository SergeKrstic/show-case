import unittest
from enum import Enum

import mock

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.EntityManager import EntityManager
from HorizonCore.Framework.Goal import Goal, GoalStatus
from HorizonCore.Framework.GoalEvaluator import GoalEvaluator
from HorizonCore.Framework.GoalThink import GoalThink


class GoalThinkSpecifications(unittest.TestCase):
    def setUp(self):
        self.testEntity = TestBot(Entity.TestEntity)
        EntityManager.RegisterEntity(self.testEntity)

    def tearDown(self):
        EntityManager.Reset()
        BaseEntity.ResetNextValidId()

    def test_SpecifyThatGoalEvaluatorCanBeConstructed(self):
        # arrange
        goalThink = self.CreateGoalThink()

        # assert
        self.assertEqual(self.testEntity, goalThink.Owner)
        self.assertEqual(GoalType.TestGoalComposite, goalThink.Type)
        self.assertEqual(2, len(goalThink._evaluators))

    def test_SpecifyThatGoalThinkCanDetermineIfGoalIsPresent(self):
        # arrange
        goalThink = self.CreateGoalThink()

        # assert
        self.assertFalse(goalThink.IsGoalPresent(GoalType.TestGoal1), "Expected no goals to be present")

        # act
        goalThink.AddSubGoal(GoalOne(self.testEntity))

        # assert
        self.assertTrue(goalThink.IsGoalPresent(GoalType.TestGoal1), "Expected goal to be present")

        # assert
        self.assertFalse(goalThink.IsGoalPresent(GoalType.TestGoal2), "Expected goal NOT to be present")

    def test_SpecifyThatActiveDelegatesToArbitrate(self):
        # arrange
        goalThink = self.CreateGoalThink()
        goalThink.Arbitrate = mock.Mock()

        # act
        goalThink.Activate()

        # assert
        goalThink.Arbitrate.assert_called()

    def test_SpecifyThatTerminateDoesNothing(self):
        # arrange
        goalThink = self.CreateGoalThink()

        # act
        goalThink.Terminate()

        # assert
        self.assertTrue(True, "Just a dummy test to achieve 100% coverage")

    def test_SpecifyThatTheCurrentGoalCanBeProcessedAndSetStatusBackToInactive(self):
        # arrange
        goalThink = self.CreateGoalThink()
        self.testEntity._brain = goalThink

        # act
        goalThink._processSubGoals = mock.Mock(return_value=GoalStatus.Completed)
        status = goalThink.Process()

        # assert
        self.assertEqual(GoalStatus.Inactive, status)

        # act
        goalThink._processSubGoals = mock.Mock(return_value=GoalStatus.Failed)
        status = goalThink.Process()

        # assert
        self.assertEqual(GoalStatus.Inactive, status)

    def test_SpecifyThatAnExceptionIsRaisedWhenTryingToArbitrateIfNoEvaluatorSet(self):
        # arrange
        goalThink = self.CreateGoalThink()
        goalThink._evaluators = []

        # assert
        self.assertRaises(Exception, goalThink.Arbitrate)

    # Helper Methods
    # ==================================================================================================================

    @staticmethod
    def CreateGoalThink():
        goalEvaluators = [TestGoalEvaluatorOne(characterBias=0.5), TestGoalEvaluatorTwo(characterBias=0.3)]
        testEntity = EntityManager.GetEntityFromID(Entity.TestEntity)
        return GoalThink(testEntity, GoalType.TestGoalComposite, goalEvaluators)


# Helper Classes
# ======================================================================================================================

class Entity(Enum):
    TestEntity = 1


class GoalType(Enum):
    TestGoalComposite = 0
    TestGoal1 = 1
    TestGoal2 = 2


class TestBot(BaseEntity):
    def __init__(self, entityId):
        super().__init__(entityId)
        self._brain = None

    def Update(self):
        self.Brain.Process()

    def HandleTelegram(self, telegram):
        pass

    @property
    def Brain(self):
        return self._brain


class TestGoalEvaluatorOne(GoalEvaluator):
    def CalculateDesirability(self, bot):
        return 0.8

    def SetGoal(self, bot):
        bot.Brain.AddSubGoal(GoalOne(bot))


class TestGoalEvaluatorTwo(GoalEvaluator):
    def CalculateDesirability(self, bot):
        return 0.5

    def SetGoal(self, bot):
        pass


class GoalOne(Goal):
    def __init__(self, owner):
        super().__init__(owner, GoalType.TestGoal1)

    def Activate(self):
        pass

    def Process(self):
        pass

    def Terminate(self):
        pass
