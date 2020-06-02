import unittest

from HorizonCore.FuzzyLogic.FuzzySetSingleton import FuzzySetSingleton


class FuzzySetSingletonSpecifications(unittest.TestCase):
    def test_SpecifyThatFuzzySetSingletonCanBeConstructed(self):
        fuzzySetSingleton = FuzzySetSingleton(50, 5, 6)

        self.assertEqual(50, fuzzySetSingleton._midPoint, "_midPoint")
        self.assertEqual(5, fuzzySetSingleton._leftOffset, "_leftOffset")
        self.assertEqual(6, fuzzySetSingleton._rightOffset, "_rightOffset")

    def test_SpecifyThatDomCanBeCalculated(self):
        fuzzySetSingleton = FuzzySetSingleton(50, 5, 5)

        self.assertEqual(0, fuzzySetSingleton.CalculateDOM(44), "Dom 1")
        self.assertEqual(1, fuzzySetSingleton.CalculateDOM(45), "Dom 2")
        self.assertEqual(1, fuzzySetSingleton.CalculateDOM(50), "Dom 3")
        self.assertEqual(1, fuzzySetSingleton.CalculateDOM(55), "Dom 4")
        self.assertEqual(0, fuzzySetSingleton.CalculateDOM(56), "Dom 5")
