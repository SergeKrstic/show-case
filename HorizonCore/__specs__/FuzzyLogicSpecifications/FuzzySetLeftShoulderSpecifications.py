import unittest

from HorizonCore.FuzzyLogic.FuzzySetLeftShoulder import FuzzySetLeftShoulder


class FuzzySetLeftShoulderSpecifications(unittest.TestCase):
    def test_SpecifyThatFuzzySetLeftShoulderCanBeConstructed(self):
        fuzzySetLeftShoulder = FuzzySetLeftShoulder(50, 5, 6)

        self.assertEqual(50, fuzzySetLeftShoulder._peakPoint, "_peakPoint")
        self.assertEqual(5, fuzzySetLeftShoulder._leftOffset, "_leftOffset")
        self.assertEqual(6, fuzzySetLeftShoulder._rightOffset, "_rightOffset")

    def test_SpecifyThatDomCanBeCalculated(self):
        fuzzySetLeftShoulder = FuzzySetLeftShoulder(50, 10, 10)

        self.assertEqual(0, fuzzySetLeftShoulder.CalculateDOM(39), "Dom 0")
        self.assertEqual(1, fuzzySetLeftShoulder.CalculateDOM(40), "Dom 1")
        self.assertEqual(1, fuzzySetLeftShoulder.CalculateDOM(45), "Dom 2")
        self.assertEqual(1, fuzzySetLeftShoulder.CalculateDOM(50), "Dom 3")
        self.assertEqual(0.5, fuzzySetLeftShoulder.CalculateDOM(55), "Dom 4")
        self.assertEqual(0, fuzzySetLeftShoulder.CalculateDOM(60), "Dom 5")

        fuzzySetLeftShoulder = FuzzySetLeftShoulder(50, 0, 10)
        self.assertEqual(0, fuzzySetLeftShoulder.CalculateDOM(49), "Dom 6")
        self.assertEqual(1, fuzzySetLeftShoulder.CalculateDOM(50), "Dom 7")
        self.assertEqual(0.5, fuzzySetLeftShoulder.CalculateDOM(55), "Dom 8")

        fuzzySetLeftShoulder = FuzzySetLeftShoulder(50, 10, 0)
        self.assertEqual(0, fuzzySetLeftShoulder.CalculateDOM(39), "Dom 9")
        self.assertEqual(1, fuzzySetLeftShoulder.CalculateDOM(40), "Dom 10")
        self.assertEqual(1, fuzzySetLeftShoulder.CalculateDOM(50), "Dom 11")
        self.assertEqual(0, fuzzySetLeftShoulder.CalculateDOM(51), "Dom 12")
