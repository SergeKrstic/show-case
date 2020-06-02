import unittest

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.Vector2D import Vector2D
from HorizonCore.Triggering.Trigger import Trigger
from HorizonCore.Triggering.TriggerRegion import TriggerRegionCircle, TriggerRegionRectangle


class TriggerSpecifications(unittest.TestCase):
    def test_SpecifyThatATriggerCanBeConstructed(self):
        trigger = self.CreateTestTrigger()

        self.assertEqual(None, trigger._regionOfInfluence, "regionOfInfluence")
        self.assertEqual(False, trigger._removeFromWorld, "removeFromWorld")
        self.assertEqual(True, trigger._active, "active")

    def test_SpecifyThatTryRaisesNotImplemented(self):
        trigger = self.CreateTestTrigger()

        self.assertRaises(NotImplementedError, trigger.Try, None)

    def test_SpecifyThatUpdateRaisesNotImplemented(self):
        trigger = self.CreateTestTrigger()

        self.assertRaises(NotImplementedError, trigger.Update)

    def test_SpecifyThatHandleTelegramRaisesNotImplemented(self):
        trigger = self.CreateTestTrigger()

        self.assertRaises(NotImplementedError, trigger.HandleTelegram, None)

    def test_SpecifyThatTriggerAFlagWhetherItNeedsToBeRemovedFromTheWorld(self):
        trigger = self.CreateTestTrigger()
        self.assertEqual(False, trigger.IsToBeRemoved())

        trigger.SetToBeRemovedFromWorld()
        self.assertEqual(True, trigger.IsToBeRemoved())

    def test_SpecifyThatTriggerCanBeActivated(self):
        trigger = self.CreateTestTrigger()
        self.assertEqual(True, trigger.IsActive())

        trigger.SetInactive()
        self.assertEqual(False, trigger.IsActive())

        trigger.SetActive()
        self.assertEqual(True, trigger.IsActive())

    def test_SpecifyThatACircularRegionCanBeAdded(self):
        trigger = self.CreateTestTrigger()
        trigger.AddCircularTriggerRegion(center=Vector2D(1, 3), radius=3)

        self.assertEqual(type(trigger._regionOfInfluence), TriggerRegionCircle)

    def test_SpecifyThatARectangularRegionCanBeAdded(self):
        trigger = self.CreateTestTrigger()
        trigger.AddRectangularTriggerRegion(topLeft=Vector2D(1, 3), bottomRight=Vector2D(5, 6))

        self.assertEqual(type(trigger._regionOfInfluence), TriggerRegionRectangle)

    def test_SpecifyThatATriggerCanDetermineIfAnEntityIsTouchingTheTrigger(self):
        trigger = self.CreateTestTrigger()
        trigger.AddRectangularTriggerRegion(topLeft=Vector2D(1, 3), bottomRight=Vector2D(5, 6))

        self.assertEqual(True, trigger.IsTouchingTrigger(entityGpsPosition=Vector2D(3, 4), entityRadius=3))

    def test_SpecifyThatWhenNoRegionOfInfluenceIsAssignedTheTriggerIsTouchingReturnsFalseByDefault(self):
        trigger = self.CreateTestTrigger()

        self.assertEqual(False, trigger.IsTouchingTrigger(entityGpsPosition=Vector2D(3, 4), entityRadius=3))

    @staticmethod
    def CreateTestTrigger():
        BaseEntity.ResetNextValidId()
        return Trigger(1)


if __name__ == '__main__':
    unittest.main()
