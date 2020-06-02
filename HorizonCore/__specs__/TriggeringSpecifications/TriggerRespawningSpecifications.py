import unittest

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Triggering.TriggerRespawning import TriggerRespawning


class TriggerRespawningSpecifications(unittest.TestCase):
    def test_SpecifyThatTriggerRespawningCanBeConstructed(self):
        triggerRespawning = self.CreateTriggerRespawning()

        self.assertEqual(10, triggerRespawning._numberOfUpdatesBetweenRespawns, "_numberOfUpdatesBetweenRespawns")
        self.assertEqual(0, triggerRespawning._numberOfUpdatesRemainingUntilRespawn, "_numberOfUpdatesRemainingUntilRespawn")
        self.assertEqual(True, triggerRespawning.IsActive())

    def test_SpecifyThatTryRaisesNotImplemented(self):
        triggerRespawning = self.CreateTriggerRespawning()

        self.assertRaises(NotImplementedError, triggerRespawning.Try, None)

    def test_SpecifyThatHandleTelegramRaisesNotImplemented(self):
        triggerRespawning = self.CreateTriggerRespawning()

        self.assertRaises(NotImplementedError, triggerRespawning.HandleTelegram, None)

    def test_SpecifyThatAfterTheTriggerIsDeactivatedItRespawnAfterASpecifiedTime(self):
        triggerRespawning = self.CreateTriggerRespawning()

        self.assertEqual(10, triggerRespawning._numberOfUpdatesBetweenRespawns, "_numberOfUpdatesBetweenRespawns 1")
        self.assertEqual(0, triggerRespawning._numberOfUpdatesRemainingUntilRespawn, "_numberOfUpdatesRemainingUntilRespawn 1")
        self.assertEqual(True, triggerRespawning.IsActive(), "IsActive 1")

        triggerRespawning.Deactivate()

        self.assertEqual(10, triggerRespawning._numberOfUpdatesBetweenRespawns, "_numberOfUpdatesBetweenRespawns 2")
        self.assertEqual(10, triggerRespawning._numberOfUpdatesRemainingUntilRespawn, "_numberOfUpdatesRemainingUntilRespawn 2")
        self.assertEqual(False, triggerRespawning.IsActive(), "IsActive 2")

        triggerRespawning.Update()

        self.assertEqual(10, triggerRespawning._numberOfUpdatesBetweenRespawns, "_numberOfUpdatesBetweenRespawns 3")
        self.assertEqual(9, triggerRespawning._numberOfUpdatesRemainingUntilRespawn, "_numberOfUpdatesRemainingUntilRespawn 3")
        self.assertEqual(False, triggerRespawning.IsActive(), "IsActive 3")

        for counter in range(0, 9):
            triggerRespawning.Update()

        self.assertEqual(10, triggerRespawning._numberOfUpdatesBetweenRespawns, "_numberOfUpdatesBetweenRespawns 4")
        self.assertEqual(0, triggerRespawning._numberOfUpdatesRemainingUntilRespawn, "_numberOfUpdatesRemainingUntilRespawn 4")
        self.assertEqual(True, triggerRespawning.IsActive(), "IsActive 4")

    @staticmethod
    def CreateTriggerRespawning():
        BaseEntity.ResetNextValidId()
        triggerRespawning = TriggerRespawning(1)
        triggerRespawning.SetRespawnDelay(10)
        return triggerRespawning


if __name__ == '__main__':
    unittest.main()
