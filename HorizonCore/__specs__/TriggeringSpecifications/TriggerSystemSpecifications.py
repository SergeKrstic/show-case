import mock
import unittest

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Triggering.Trigger import Trigger
from HorizonCore.Triggering.TriggerSystem import TriggerSystem


class TriggerSystemSpecifications(unittest.TestCase):
    def test_SpecifyThatTriggerSystemCanBeConstructed(self):
        triggerSystem = TriggerSystem()

        self.assertEqual(0, len(triggerSystem.GetTriggers()))

    def test_SpecifyThatTriggersCanBeRegisteredAndCleared(self):
        BaseEntity.ResetNextValidId()
        triggerSystem = TriggerSystem()

        self.assertEqual(0, len(triggerSystem.GetTriggers()), "len 1")

        triggerSystem.Register(Trigger(1))
        triggerSystem.Register(Trigger(2))

        self.assertEqual(2, len(triggerSystem.GetTriggers()), "len 2")

        triggerSystem.Clear()

        self.assertEqual(0, len(triggerSystem.GetTriggers()), "len 3")

    def test_SpecifyThatUpdateCanBeCalled(self):
        # arrange
        entities = ['e1', 'e2']
        triggerSystem = TriggerSystem()
        triggerSystem.TryTriggers = mock.Mock()
        triggerSystem.UpdateTriggers = mock.Mock()

        # act
        triggerSystem.Update(entities)

        triggerSystem.UpdateTriggers.assert_called()
        triggerSystem.TryTriggers.assert_called_with(entities)

    def test_SpecifyThatTriggersCanBeUpdated(self):
        # arrange
        BaseEntity.ResetNextValidId()
        trigger = Trigger(1)
        trigger.Update = mock.Mock()
        triggerSystem = TriggerSystem()
        triggerSystem.Register(trigger)

        # act
        triggerSystem.UpdateTriggers()

        # assert
        trigger.Update.assert_called()

    def test_SpecifyThatWhenUpdatingTriggersOldTriggersAreRemoved(self):
        # arrange
        trigger = self.CreateTestTrigger()
        trigger.SetToBeRemovedFromWorld()
        triggerSystem = TriggerSystem()
        triggerSystem.Register(trigger)

        self.assertEqual(1, len(triggerSystem.GetTriggers()), "len 1")

        # act
        triggerSystem.UpdateTriggers()

        # assert
        self.assertEqual(0, len(triggerSystem.GetTriggers()), "len 2")

    def test_SpecifyThatTriggersCanBeTestedAgainstEntitiesForTriggering(self):
        # arrange
        e1 = TestEntity()
        entities = [e1]
        trigger = self.CreateTestTrigger()
        trigger.Try = mock.Mock()
        triggerSystem = TriggerSystem()
        triggerSystem.Register(trigger)

        # act
        triggerSystem.TryTriggers(entities)

        # assert
        trigger.Try.assert_called_with(e1)


    @staticmethod
    def CreateTestTrigger():
        BaseEntity.ResetNextValidId()
        return TestTrigger(BaseEntity.GetNextValidId())


class TestEntity:
    def IsReadyForTriggerUpdate(self):
        return True


class TestTrigger(Trigger):
    def Try(self, entityType):
        pass

    def Update(self):
        pass

    def HandleTelegram(self, telegram):
        pass


if __name__ == '__main__':
    unittest.main()
