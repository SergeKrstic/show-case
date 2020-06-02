import unittest

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Triggering.TriggerLimitedLifeTime import TriggerLimitedLifetime


class TriggerLimitedTimeSpecifications(unittest.TestCase):
    def test_SpecifyThatTriggerLimitedLifetimeCanBeConstructed(self):
        triggerLimitedLifetime = self.CreateTriggerLimitedLifetime()

        self.assertEqual(10, triggerLimitedLifetime._lifetime)
        self.assertEqual(False, triggerLimitedLifetime.IsToBeRemoved())

    def test_SpecifyThatTryRaisesNotImplemented(self):
        triggerLimitedLifetime = self.CreateTriggerLimitedLifetime()

        self.assertRaises(NotImplementedError, triggerLimitedLifetime.Try, None)

    def test_SpecifyThatHandleTelegramRaisesNotImplemented(self):
        triggerLimitedLifetime = self.CreateTriggerLimitedLifetime()

        self.assertRaises(NotImplementedError, triggerLimitedLifetime.HandleTelegram, None)

    def test_SpecifyThatLimitedLifeTriggerCanRemoveItselfWhenItsTimeIsUp(self):
        triggerLimitedLifetime = self.CreateTriggerLimitedLifetime()

        self.assertEqual(10, triggerLimitedLifetime._lifetime)
        self.assertEqual(False, triggerLimitedLifetime.IsToBeRemoved())

        triggerLimitedLifetime.Update()

        self.assertEqual(9, triggerLimitedLifetime._lifetime)
        self.assertEqual(False, triggerLimitedLifetime.IsToBeRemoved())

        for counter in range(0, 9):
            triggerLimitedLifetime.Update()

        self.assertEqual(0, triggerLimitedLifetime._lifetime)
        self.assertEqual(True, triggerLimitedLifetime.IsToBeRemoved())

    @staticmethod
    def CreateTriggerLimitedLifetime():
        BaseEntity.ResetNextValidId()
        return TriggerLimitedLifetime(10)


if __name__ == '__main__':
    unittest.main()
