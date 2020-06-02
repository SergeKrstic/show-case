import unittest

from HorizonCore.Framework.Vector2D import Vector2D
from HorizonCore.Triggering.TriggerRegion import TriggerRegion, TriggerRegionCircle, TriggerRegionRectangle


class TriggerRegionSpecifications(unittest.TestCase):
    def test_SpecifyThatTriggerRegionRaiseANotImplementException(self):
        triggerRegion = TriggerRegion()

        self.assertRaises(Exception, triggerRegion.IsTouching, None, None)

    def test_SpecifyThatACircularRegionCanBeConstructed(self):
        circularRegion = TriggerRegionCircle(position=Vector2D(10, 9), radius=5)

        self.assertEqual(10, circularRegion._position.X, "position.X")
        self.assertEqual(9, circularRegion._position.Y, "position.Y")
        self.assertEqual(5, circularRegion._radius, "radius")

    def test_SpecifyThatACircularRegionCanDetermineIfAnEntityIsTouching(self):
        circularRegion = TriggerRegionCircle(position=Vector2D(10, 10), radius=5)

        self.assertTrue(circularRegion.IsTouching(entityPosition=Vector2D(7, 7), entityRadius=2))
        self.assertFalse(circularRegion.IsTouching(entityPosition=Vector2D(1, 1), entityRadius=2))

    def test_SpecifyThatARectangularRegionCanBeConstructed(self):
        rectangularRegion = TriggerRegionRectangle(topLeft=Vector2D(3, 4), bottomRight=Vector2D(9, 10))

        self.assertEqual(3, rectangularRegion._box.Left, "Left")
        self.assertEqual(4, rectangularRegion._box.Top, "Top")
        self.assertEqual(9, rectangularRegion._box.Right, "Right")
        self.assertEqual(10, rectangularRegion._box.Bottom, "Bottom")

    def test_SpecifyThatARectangularRegionCanDetermineIfAnEntityIsTouching(self):
        rectangularRegion = TriggerRegionRectangle(topLeft=Vector2D(3, 4), bottomRight=Vector2D(9, 10))

        self.assertTrue(rectangularRegion.IsTouching(entityPosition=Vector2D(7, 7), entityRadius=2))
        self.assertFalse(rectangularRegion.IsTouching(entityPosition=Vector2D(1, 1), entityRadius=2))


if __name__ == '__main__':
    unittest.main()
