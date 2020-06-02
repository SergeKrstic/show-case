import unittest

from mock import Mock

from HorizonCore.FuzzyLogic.FuzzyHedges import FzSet
from HorizonCore.FuzzyLogic.FuzzyOperators import FzAND
from HorizonCore.FuzzyLogic.FuzzyRule import FuzzyRule
from HorizonCore.FuzzyLogic.FuzzySetTriangle import FuzzySetTriangle


class FuzzyRuleSpecifications(unittest.TestCase):
    def test_SpecifyThatFuzzyRuleCanBeConstructed(self):
        fuzzyRule = self.CreateFuzzyRule()
        self.assertEqual(FzAND, type(fuzzyRule._antecedentTerm))
        self.assertEqual(FzSet, type(fuzzyRule._consequenceTerm))

    def test_SpecifyThatConfidenceOfConsequentCanBeSetToZero(self):
        fuzzyRule = self.CreateFuzzyRule()
        self.assertEqual(0.5, fuzzyRule._consequenceTerm.GetDOM())
        fuzzyRule.SetConfidenceOfConsequentToZero()
        self.assertEqual(0.0, fuzzyRule._consequenceTerm.GetDOM())

    def test_SpecifyThatFuzzyRuleCanCalculate(self):
        fuzzyRule = self.CreateFuzzyRule()
        fuzzyRule._antecedentTerm.GetDOM = Mock()
        fuzzyRule._consequenceTerm.ORwithDOM = Mock()
        fuzzyRule.Calculate()
        fuzzyRule._antecedentTerm.GetDOM.assert_called()
        fuzzyRule._consequenceTerm.ORwithDOM.assert_called()

    @staticmethod
    def CreateFuzzyRule():
        smart = FzSet(FuzzySetTriangle(10, 5, 5))
        skilled = FzSet(FuzzySetTriangle(15, 5, 5))
        productive = FzSet(FuzzySetTriangle(20, 5, 5))
        productive.ORwithDOM(0.5)
        return FuzzyRule(FzAND(smart, skilled), productive)
