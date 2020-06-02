import unittest

from HorizonCore.Framework.Region import Region, RegionModifier
from HorizonCore.Framework.Vector2D import Vector2D


class RegionSpecifications(unittest.TestCase):

    def test_SpecifyThatARegionCanBeConstructed(self):
        # arrange
        region = self.CreateTestRegion()

        # assert
        self.assertEqual(10, region.Left, "Left")
        self.assertEqual(20, region.Top, "Top")
        self.assertEqual(60, region.Right, "Right")
        self.assertEqual(90, region.Bottom, "Bottom")
        self.assertEqual(101, region.ID, "ID")
        self.assertEqual(50, region.Width, "Width")
        self.assertEqual(70, region.Height, "Height")
        self.assertEqual(70, region.Length, "Length")
        self.assertEqual(50, region.Breadth, "Breadth")
        self.assertEqual(35, region.Center.X, "Center.X")
        self.assertEqual(55, region.Center.Y, "Center.Y")

    def test_SpecifyThatTheRegionCanDetermineIfAPositionCoordinateIsInside(self):
        # arrange
        region = self.CreateTestRegion()

        # assert
        self.assertFalse(region.IsInside(Vector2D(5, 25)), "Expected position vector to be outside region")
        self.assertTrue(region.IsInside(Vector2D(15, 25)), "Expected position vector to be inside region")

        self.assertFalse(region.IsInside(Vector2D(5, 55), RegionModifier.HalfSize), "Expected position vector to be outside half-size region")
        self.assertTrue(region.IsInside(Vector2D(35, 55), RegionModifier.HalfSize), "Expected position vector to be inside half-size region")

        self.assertRaises(ValueError, region.IsInside, Vector2D(35, 55), "invalid modifier")

    @staticmethod
    def CreateTestRegion():
        return Region(left=10, top=20, right=60, bottom=90, regionId=101)
