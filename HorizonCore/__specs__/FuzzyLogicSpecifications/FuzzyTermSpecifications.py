import unittest

from HorizonCore.FuzzyLogic.FuzzyTerm import FuzzyTerm


class FuzzyTermSpecifications(unittest.TestCase):
    def test_SpecifyThatCloneRaisesNotImplemented(self):
        self.assertRaises(NotImplementedError, FuzzyTerm().Clone)

    def test_SpecifyThatGetDOMRaisesNotImplemented(self):
        self.assertRaises(NotImplementedError, FuzzyTerm().GetDOM)

    def test_SpecifyThatClearDOMRaisesNotImplemented(self):
        self.assertRaises(NotImplementedError, FuzzyTerm().ClearDOM)

    def test_SpecifyThatORwithDOMRaisesNotImplemented(self):
        self.assertRaises(NotImplementedError, FuzzyTerm().ORwithDOM, None)
