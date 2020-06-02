import unittest

from HorizonCore.FuzzyLogic.FuzzyHedges import FzSet, FzVery, FzFairly
from HorizonCore.FuzzyLogic.FuzzySetTriangle import FuzzySetTriangle


class FuzzyHedgesSpecifications(unittest.TestCase):

    # FzSet Specifications
    # ==================================================================================================================

    def test_SpecifyThatFzSetCanBeConstructed(self):
        fzSet = self.CreateFzSet()
        self.assertEqual(type(fzSet._fuzzySet), FuzzySetTriangle)

    def test_SpecifyThatFzSetCanGetTheDom(self):
        fzSet = self.CreateFzSet()
        self.assertEqual(0.5, fzSet.GetDOM())

    def test_SpecifyThatFzSetCanClearTheDom(self):
        fzSet = self.CreateFzSet()
        self.assertEqual(0.5, fzSet.GetDOM())
        fzSet.ClearDOM()
        self.assertEqual(0.0, fzSet.GetDOM())

    def test_SpecifyThatFzSetCanOrWithDom(self):
        fzSet = self.CreateFzSet()
        self.assertEqual(0.5, fzSet.GetDOM())
        fzSet.ORwithDOM(0.7)
        self.assertEqual(0.7, fzSet.GetDOM())

    def test_SpecifyThatFzSetCanBeCloned(self):
        fzSet = self.CreateFzSet()
        fzSetClone = fzSet.Clone()
        self.assertNotEqual(fzSet, fzSetClone)
        self.assertEqual(fzSet.GetDOM(), fzSetClone.GetDOM())

    @staticmethod
    def CreateFzSet():
        fuzzySet = FuzzySetTriangle(10, 5, 5)
        fuzzySet.DOM = fuzzySet.CalculateDOM(7.5)
        return FzSet(fuzzySet)

    # FzVery Specifications
    # ==================================================================================================================

    def test_SpecifyThatFzVeryCanBeConstructed(self):
        fzVery = self.CreateFzVery()
        self.assertEqual(type(fzVery._fuzzySet), FuzzySetTriangle)

    def test_SpecifyThatFzVeryCanGetTheDom(self):
        fzVery = self.CreateFzVery()
        self.assertEqual(0.25, fzVery.GetDOM())

    def test_SpecifyThatFzVeryCanClearTheDom(self):
        fzVery = self.CreateFzVery()
        self.assertEqual(0.25, fzVery.GetDOM())
        fzVery.ClearDOM()
        self.assertEqual(0.0, fzVery.GetDOM())

    def test_SpecifyThatFzVeryCanOrWithDom(self):
        fzVery = self.CreateFzVery()
        self.assertEqual(0.25, fzVery.GetDOM())
        fzVery.ORwithDOM(0.8)
        self.assertAlmostEqual(0.4096, fzVery.GetDOM(), 3)

    def test_SpecifyThatFzVeryCanBeCloned(self):
        fzVery = self.CreateFzVery()
        fzSetClone = fzVery.Clone()
        self.assertNotEqual(fzVery, fzSetClone)
        self.assertEqual(fzVery.GetDOM(), fzSetClone.GetDOM())

    @staticmethod
    def CreateFzVery():
        fuzzySet = FuzzySetTriangle(10, 5, 5)
        fuzzySet.DOM = fuzzySet.CalculateDOM(7.5)
        return FzVery(FzSet(fuzzySet))

    # FzFairly Specifications
    # ==================================================================================================================

    def test_SpecifyThatFzFairlyCanBeConstructed(self):
        fzFairly = self.CreateFzFairly()
        self.assertEqual(type(fzFairly._fuzzySet), FuzzySetTriangle)

    def test_SpecifyThatFzFairlyCanGetTheDom(self):
        fzFairly = self.CreateFzFairly()
        self.assertAlmostEqual(0.7071, fzFairly.GetDOM(), 3)

    def test_SpecifyThatFzFairlyCanClearTheDom(self):
        fzFairly = self.CreateFzFairly()
        self.assertAlmostEqual(0.7071, fzFairly.GetDOM(), 3)
        fzFairly.ClearDOM()
        self.assertEqual(0.0, fzFairly.GetDOM())

    def test_SpecifyThatFzFairlyCanOrWithDom(self):
        fzFairly = self.CreateFzFairly()
        self.assertAlmostEqual(0.7071, fzFairly.GetDOM(), 3)
        fzFairly.ORwithDOM(0.8)
        self.assertAlmostEqual(0.9457, fzFairly.GetDOM(), 3)

    def test_SpecifyThatFzFairlyCanBeCloned(self):
        fzFairly = self.CreateFzFairly()
        fzSetClone = fzFairly.Clone()
        self.assertNotEqual(fzFairly, fzSetClone)
        self.assertEqual(fzFairly.GetDOM(), fzSetClone.GetDOM())

    @staticmethod
    def CreateFzFairly():
        fuzzySet = FuzzySetTriangle(10, 5, 5)
        fuzzySet.DOM = fuzzySet.CalculateDOM(7.5)
        return FzFairly(FzSet(fuzzySet))
