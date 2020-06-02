import unittest
from enum import Enum

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.EntityManager import EntityManager
from HorizonCore.Framework.Goal import Goal, GoalStatus
from HorizonCore.Framework.GoalComposite import GoalComposite
from HorizonCore.Framework.Telegram import Telegram


class GoalCompositeSpecifications(unittest.TestCase):

    def setUp(self):
        self.testEntity = TestEntity(Entity.TestEntity)
        EntityManager.RegisterEntity(self.testEntity)

    def tearDown(self):
        EntityManager.Reset()
        BaseEntity.ResetNextValidId()

    def test_SpecifyThatAGoalCompositeCanBeConstructed(self):
        # act
        goalComposite = self.CreateGoalComposite()

        # assert
        self.assertEqual(len(goalComposite._subGoalList), 0)

    def test_SpecifyThatActivateRaisesNotImplementedError(self):
        # arrange
        goalComposite = self.CreateGoalComposite()

        # assert
        self.assertRaises(NotImplementedError, goalComposite.Activate)

    def test_SpecifyThatProcessRaisesNotImplementedError(self):
        # arrange
        goalComposite = self.CreateGoalComposite()

        # assert
        self.assertRaises(NotImplementedError, goalComposite.Process)

    def test_SpecifyThatTerminateRaisesNotImplementedError(self):
        # arrange
        goalComposite = self.CreateGoalComposite()

        # assert
        self.assertRaises(NotImplementedError, goalComposite.Terminate)

    def test_SpecifyThatSubGoalsCanBeAdded(self):
        # arrange
        goalComposite = self.CreateGoalComposite()
        goalOne = GoalOne(self.testEntity)
        goalTwo = GoalTwo(self.testEntity)

        # act
        goalComposite.AddSubGoal(goalOne)
        goalComposite.AddSubGoal(goalTwo)

        # assert
        self.assertEqual(len(goalComposite._subGoalList), 2)
        self.assertEqual(GoalType.TestGoal2, goalComposite._subGoalList[0]._type)
        self.assertEqual(GoalType.TestGoal1, goalComposite._subGoalList[1]._type)

    def test_SpecifyThatAllSubGoalCanBeRemoved(self):
        # arrange
        goalComposite = self.BuildHierarchicalGoal()

        # assert
        self.assertEqual(len(goalComposite._subGoalList), 2)

        # act
        goalComposite.RemoveAllSubGoals()

        # assert
        self.assertEqual(len(goalComposite._subGoalList), 0)

    def test_SpecifyThatGoalCompositeCanDetermineWhetherSubGoalsArePresent(self):
        # arrange
        goalComposite = self.BuildHierarchicalGoal()

        # assert
        self.assertTrue(goalComposite.HasSubGoals(), "Should contain sub-goals")

        # arrange
        goalComposite.RemoveAllSubGoals()

        # assert
        self.assertFalse(goalComposite.HasSubGoals(), "Should be empty")

    def test_SpecifyThatCurrentSubGoalCanBeRetrieved(self):
        # arrange
        goalComposite = self.BuildHierarchicalGoal()

        # assert
        self.assertEqual(GoalType.TestGoal2, goalComposite.CurrentSubGoal.Type)

    def test_SpecifyThatAnExceptionIsRaisedWhenTryToRetrieveASubGoalFromAnEmptyList(self):
        # arrange
        goalComposite = self.CreateGoalComposite()

        # assert
        self.assertRaises(Exception, lambda: goalComposite.CurrentSubGoal)

    def test_SpecifyThatTelegramCanBeHandled(self):
        # arrange
        goalComposite = self.BuildHierarchicalGoal()
        telegram = Telegram(dispatchTime=0,
                            senderId=Entity.TestEntity,
                            receiverId=Entity.TestEntity,
                            message="Hello",
                            extraInfo=None)

        # act
        goalComposite.HandleTelegram(telegram)

        # assert
        self.assertEqual(goalComposite._subGoalList[0].TelegramWasProcessed, True)

    def test_SpecifyThatFalseIsReturnIfNoGoalsArePresentToHandleATelegram(self):
        # arrange
        goalComposite = self.CreateGoalComposite()
        telegram = Telegram(dispatchTime=0,
                            senderId=Entity.TestEntity,
                            receiverId=Entity.TestEntity,
                            message="Hello",
                            extraInfo=None)

        # act
        result = goalComposite.HandleTelegram(telegram)

        # assert
        self.assertEqual(False, result)

    def test_SpecifyThatSubGoalsCanBeProcessed(self):
        # arrange
        goalComposite = self.BuildHierarchicalGoal()

        # assert
        self.assertEqual(2, len(goalComposite._subGoalList))

        # act
        result = goalComposite._processSubGoals()

        # assert
        self.assertEqual(1, len(goalComposite._subGoalList))
        self.assertEqual(GoalStatus.Completed, result)

    def test_SpecifyThatTheResultOfProcessingAnEmptySubGoalListReturnsCompleted(self):
        # arrange
        goalComposite = self.CreateGoalComposite()

        # assert
        self.assertEqual(0, len(goalComposite._subGoalList))

        # act
        result = goalComposite._processSubGoals()
        self.assertEqual(GoalStatus.Completed, result)

    def test_SpecifyThatIfAfterProcessingASubGoalThereStillRemainSubGoalsThenTheResultReturnedIsActive(self):
        # arrange
        goalComposite = self.BuildHierarchicalGoal()
        goalComposite._subGoalList[0]._status = GoalStatus.Active

        # assert
        self.assertEqual(2, len(goalComposite._subGoalList))

        # act
        result = goalComposite._processSubGoals()

        # assert
        self.assertEqual(2, len(goalComposite._subGoalList))
        self.assertEqual(GoalStatus.Active, result)

    # Helper Methods
    # ==================================================================================================================

    @staticmethod
    def CreateGoalComposite():
        testEntity = EntityManager.GetEntityFromID(Entity.TestEntity)
        return GoalComposite(testEntity, GoalType.TestGoalComposite)

    def BuildHierarchicalGoal(self):
        testEntity = EntityManager.GetEntityFromID(Entity.TestEntity)
        goalComposite = GoalComposite(testEntity, GoalType.TestGoalComposite)

        goalOne = GoalOne(self.testEntity)
        goalTwo = GoalTwo(self.testEntity)

        goalComposite.AddSubGoal(goalOne)
        goalComposite.AddSubGoal(goalTwo)

        return goalComposite


# Helper Classes
# ======================================================================================================================

class Entity(Enum):
    TestEntity = 1


class GoalType(Enum):
    TestGoalComposite = 0
    TestGoal1 = 1
    TestGoal2 = 2


class TestEntity(BaseEntity):
    def Update(self):
        pass

    def HandleTelegram(self, telegram):
        pass


class GoalOne(Goal):
    def __init__(self, owner):
        super().__init__(owner, GoalType.TestGoal1)
        self.GoalWasActivated = False
        self.GoalWasProcessed = False
        self.GoalWasTerminated = False
        self.TelegramWasProcessed = False

    def Activate(self):
        self.GoalWasActivated = True

    def Process(self):
        self.GoalWasProcessed = True
        return GoalStatus.Completed

    def Terminate(self):
        self.GoalWasTerminated = True


class GoalTwo(Goal):
    def __init__(self, owner):
        super().__init__(owner, GoalType.TestGoal2)
        self._status = GoalStatus.Completed
        self.GoalWasActivated = False
        self.GoalWasProcessed = False
        self.GoalWasTerminated = False
        self.TelegramWasProcessed = False

    def Activate(self):
        self.GoalWasActivated = True

    def Process(self):
        self.GoalWasProcessed = True
        return GoalStatus.Completed

    def Terminate(self):
        self.GoalWasTerminated = True

    def HandleTelegram(self, telegram):
        self.TelegramWasProcessed = True
        return True
