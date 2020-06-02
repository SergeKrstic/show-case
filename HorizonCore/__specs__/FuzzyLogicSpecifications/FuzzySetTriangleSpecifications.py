import unittest

from HorizonCore.FuzzyLogic.FuzzySetTriangle import FuzzySetTriangle


class FuzzySetTriangleSpecifications(unittest.TestCase):
    def test_SpecifyThatFuzzySetTriangleCanBeConstructed(self):
        fuzzySetTriangle = FuzzySetTriangle(50, 5, 6)

        self.assertEqual(50, fuzzySetTriangle._peakPoint, "_peakPoint")
        self.assertEqual(5, fuzzySetTriangle._leftOffset, "_leftOffset")
        self.assertEqual(6, fuzzySetTriangle._rightOffset, "_rightOffset")

    def test_SpecifyThatDomCanBeCalculated(self):
        fuzzySetTriangle = FuzzySetTriangle(50, 10, 10)

        self.assertEqual(0.0, fuzzySetTriangle.CalculateDOM(40), "Dom 1")
        self.assertEqual(0.5, fuzzySetTriangle.CalculateDOM(45), "Dom 2")
        self.assertEqual(1.0, fuzzySetTriangle.CalculateDOM(50), "Dom 3")
        self.assertEqual(0.5, fuzzySetTriangle.CalculateDOM(55), "Dom 4")
        self.assertEqual(0.0, fuzzySetTriangle.CalculateDOM(60), "Dom 5")

        fuzzySetTriangle = FuzzySetTriangle(50, 10, 0)
        self.assertEqual(0.0, fuzzySetTriangle.CalculateDOM(40), "Dom 6")
        self.assertEqual(0.5, fuzzySetTriangle.CalculateDOM(45), "Dom 7")
        self.assertEqual(1.0, fuzzySetTriangle.CalculateDOM(50), "Dom 8")
        self.assertEqual(0.0, fuzzySetTriangle.CalculateDOM(51), "Dom 9")

        fuzzySetTriangle = FuzzySetTriangle(50, 00, 10)
        self.assertEqual(0.0, fuzzySetTriangle.CalculateDOM(49), "Dom 10")
        self.assertEqual(1.0, fuzzySetTriangle.CalculateDOM(50), "Dom 11")
        self.assertEqual(0.5, fuzzySetTriangle.CalculateDOM(55), "Dom 12")
        self.assertEqual(0.0, fuzzySetTriangle.CalculateDOM(60), "Dom 13")
