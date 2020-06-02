import unittest

from HorizonCore.FuzzyLogic.FuzzySet import FuzzySet


class FuzzySetSpecifications(unittest.TestCase):
    def test_SpecifyThatFuzzySetCanBeConstructed(self):
        fuzzySet = FuzzySet(representativeValue=100)

        self.assertEqual(0, fuzzySet.DOM, "DOM")
        self.assertEqual(100, fuzzySet.RepresentativeValue, "RepresentativeValue")

    def test_SpecifyThatTheDegreeOfMembershipCanBeSetAndCleared(self):
        fuzzySet = FuzzySet(representativeValue=100)
        fuzzySet.DOM = 0.5

        self.assertEqual(0.5, fuzzySet.DOM, "DOM 1")

        fuzzySet.ClearDOM()

        self.assertEqual(0, fuzzySet.DOM, "DOM 2")

    def test_SpecifyThatAnExceptionIsRaiseWhenSettingToDomInvalidValue(self):
        fuzzySet = FuzzySet(representativeValue=100)

        with self.assertRaises(ValueError):
            fuzzySet.DOM = 1.5

        with self.assertRaises(ValueError):
            fuzzySet.DOM = -1.5

    def test_SpecifyThatCalculateDOMRaisesNotImplemented(self):
        fuzzySet = FuzzySet(representativeValue=100)
        self.assertRaises(NotImplementedError, fuzzySet.CalculateDOM, None)

    def test_SpecifyFuzzySetSupportsOrFunctionality(self):
        fuzzySet = FuzzySet(representativeValue=100)
        self.assertEqual(0, fuzzySet.DOM, "DOM 1")
        fuzzySet.ORwithDOM(0.5)
        self.assertEqual(0.5, fuzzySet.DOM, "DOM 2")
        fuzzySet.ORwithDOM(0.2)
        self.assertEqual(0.5, fuzzySet.DOM, "DOM 3")
        fuzzySet.ORwithDOM(0.8)
        self.assertEqual(0.8, fuzzySet.DOM, "DOM 3")
        with self.assertRaises(ValueError):
            fuzzySet.ORwithDOM(1.5)
