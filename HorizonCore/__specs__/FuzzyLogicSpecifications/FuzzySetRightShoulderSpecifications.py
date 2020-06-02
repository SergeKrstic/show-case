import unittest

from HorizonCore.FuzzyLogic.FuzzySetRightShoulder import FuzzySetRightShoulder


class FuzzySetRightShoulderSpecifications(unittest.TestCase):
    def test_SpecifyThatFuzzySetRightShoulderCanBeConstructed(self):
        fuzzySetRightShoulder = FuzzySetRightShoulder(50, 5, 6)

        self.assertEqual(50, fuzzySetRightShoulder._peakPoint, "_peakPoint")
        self.assertEqual(5, fuzzySetRightShoulder._leftOffset, "_leftOffset")
        self.assertEqual(6, fuzzySetRightShoulder._rightOffset, "_rightOffset")

    def test_SpecifyThatDomCanBeCalculated(self):
        fuzzySetRightShoulder = FuzzySetRightShoulder(50, 10, 10)

        self.assertEqual(0, fuzzySetRightShoulder.CalculateDOM(61), "Dom 1")
        self.assertEqual(1, fuzzySetRightShoulder.CalculateDOM(60), "Dom 2")
        self.assertEqual(1, fuzzySetRightShoulder.CalculateDOM(55), "Dom 3")
        self.assertEqual(1, fuzzySetRightShoulder.CalculateDOM(50), "Dom 4")
        self.assertEqual(0.5, fuzzySetRightShoulder.CalculateDOM(45), "Dom 5")
        self.assertEqual(0, fuzzySetRightShoulder.CalculateDOM(40), "Dom 6")

        fuzzySetRightShoulder = FuzzySetRightShoulder(50, 10, 0)
        self.assertEqual(0, fuzzySetRightShoulder.CalculateDOM(40), "Dom 7")
        self.assertEqual(0.5, fuzzySetRightShoulder.CalculateDOM(45), "Dom 8")
        self.assertEqual(1, fuzzySetRightShoulder.CalculateDOM(50), "Dom 9")
        self.assertEqual(0, fuzzySetRightShoulder.CalculateDOM(51), "Dom 10")

        fuzzySetRightShoulder = FuzzySetRightShoulder(50, 00, 10)
        self.assertEqual(0, fuzzySetRightShoulder.CalculateDOM(49), "Dom 11")
        self.assertEqual(1, fuzzySetRightShoulder.CalculateDOM(50), "Dom 12")
        self.assertEqual(1, fuzzySetRightShoulder.CalculateDOM(60), "Dom 13")
        self.assertEqual(0, fuzzySetRightShoulder.CalculateDOM(61), "Dom 14")
