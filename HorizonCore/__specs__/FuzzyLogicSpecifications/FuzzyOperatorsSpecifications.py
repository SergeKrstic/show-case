import unittest

from HorizonCore.FuzzyLogic.FuzzyHedges import FzSet
from HorizonCore.FuzzyLogic.FuzzyOperators import FzAND, FzOR
from HorizonCore.FuzzyLogic.FuzzySetTriangle import FuzzySetTriangle


class FuzzyOperatorsSpecifications(unittest.TestCase):

    # FzAND Specifications
    # ==================================================================================================================

    def test_SpecifyThatFzANDCanBeConstructed(self):
        fzAnd = self.CreateFzAND()
        self.assertEqual(2, len(fzAnd._terms))

    def test_SpecifyThatConstructingFzANDOnlyOneTermRaisesAnException(self):
        fzVar1 = FuzzySetTriangle(10, 5, 5)
        self.assertRaises(ValueError, FzAND, fzVar1)

    def test_SpecifyThatFzANDCanGetTheDom(self):
        fzAnd = self.CreateFzAND()
        self.assertEqual(0.5, fzAnd.GetDOM())

    def test_SpecifyThatFzANDCanClearTheDom(self):
        fzAnd = self.CreateFzAND()
        self.assertEqual(0.5, fzAnd.GetDOM())
        fzAnd.ClearDOM()
        self.assertEqual(0.0, fzAnd.GetDOM())

    def test_SpecifyThatFzVeryCanOrWithDom(self):
        fzAnd = self.CreateFzAND()
        self.assertEqual(0.5, fzAnd.GetDOM())
        fzAnd.ORwithDOM(0.8)
        self.assertAlmostEqual(0.8, fzAnd.GetDOM(), 3)

    def test_SpecifyThatFzVeryCanBeCloned(self):
        fzAnd = self.CreateFzAND()
        fzAndClone = fzAnd.Clone()
        self.assertNotEqual(fzAnd, fzAndClone)
        self.assertEqual(fzAnd.GetDOM(), fzAndClone.GetDOM())

    @staticmethod
    def CreateFzAND():
        fzVar1 = FuzzySetTriangle(10, 5, 5)
        fzVar1.DOM = fzVar1.CalculateDOM(12.5)
        fzVar2 = FuzzySetTriangle(15, 5, 5)
        fzVar2.DOM = fzVar2.CalculateDOM(12.5)
        return FzAND(FzSet(fzVar1), FzSet(fzVar2))

    # FzOR Specifications
    # ==================================================================================================================

    def test_SpecifyThatFzORCanBeConstructed(self):
        fzOr = self.CreateFzOR()
        self.assertEqual(2, len(fzOr._terms))

    def test_SpecifyThatConstructingFzOROnlyOneTermRaisesAnException(self):
        fzVar1 = FuzzySetTriangle(10, 5, 5)
        self.assertRaises(ValueError, FzOR, fzVar1)

    def test_SpecifyThatFzORCanGetTheDom(self):
        fzOr = self.CreateFzOR()
        self.assertEqual(0.5, fzOr.GetDOM())

    def test_SpecifyThatMethodClearDOMOnFzORRaisesAnException(self):
        fzOr = self.CreateFzOR()
        self.assertRaises(Exception, fzOr.ClearDOM)

    def test_SpecifyThatMethodORwithDOMOnFzORRaisesAnException(self):
        fzOr = self.CreateFzOR()
        self.assertRaises(Exception, fzOr.ORwithDOM, 0.5)

    def test_SpecifyThatFzOFCanBeCloned(self):
        fzOr = self.CreateFzOR()

        fzOrClone = fzOr.Clone()
        self.assertNotEqual(fzOr, fzOrClone)
        self.assertEqual(fzOr.GetDOM(), fzOrClone.GetDOM())

    @staticmethod
    def CreateFzOR():
        fzVar1 = FuzzySetTriangle(10, 5, 5)
        fzVar1.DOM = fzVar1.CalculateDOM(12.5)
        fzVar2 = FuzzySetTriangle(15, 5, 5)
        fzVar2.DOM = fzVar2.CalculateDOM(12.5)
        return FzOR(FzSet(fzVar1), FzSet(fzVar2))
