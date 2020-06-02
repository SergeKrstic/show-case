import unittest

from HorizonCore.Framework.Box2D import Box2D
from HorizonCore.Framework.Vector2D import Vector2D


class Box2DSpecifications(unittest.TestCase):

    def test_SpecifyThatABox2DCanBeConstructed(self):
        box = Box2D(Vector2D(1, 2), Vector2D(8, 9))

        self.assertEqual(1, box.TopLeft.X, "TopLeft.X")
        self.assertEqual(2, box.TopLeft.Y, "TopLeft.Y")
        self.assertEqual(8, box.BottomRight.X, "BottomRight.X")
        self.assertEqual(9, box.BottomRight.Y, "BottomRight.Y")
        self.assertEqual(4.5, box.Center.X, "Center.X")
        self.assertEqual(5.5, box.Center.Y, "Center.Y")
        self.assertEqual(2, box.Top, "Top")
        self.assertEqual(1, box.Left, "Left")
        self.assertEqual(9, box.Bottom, "Bottom")
        self.assertEqual(8, box.Right, "Right")

    def test_SpecifyThatBoxCanDetermineIfAnotherBoxOverlapsWithItself(self):
        box = Box2D(Vector2D(1, 2), Vector2D(8, 9))
        otherOverlapping = Box2D(Vector2D(0, 0), Vector2D(3, 3))
        otherNotOverlapping = Box2D(Vector2D(-1, -1), Vector2D(1, 1))

        self.assertTrue(box.IsOverlappedWith(otherOverlapping), "overlapping")
        self.assertFalse(box.IsOverlappedWith(otherNotOverlapping), "not overlapping")
