import unittest

from HorizonCore.FuzzyLogic.FuzzyModule import FuzzyModule, DefuzzifyMethod
from HorizonCore.FuzzyLogic.FuzzyOperators import FzAND
from HorizonCore.FuzzyLogic.FuzzyVariable import FuzzyVariable


class FuzzyModuleSpecifications(unittest.TestCase):
    def test_SpecifyThatFuzzyModuleCanBeConstructed(self):
        fuzzyModule = FuzzyModule()

        self.assertEqual(0, len(fuzzyModule._variables), "_variables")
        self.assertEqual(0, len(fuzzyModule._rules), "_rules")

    def test_SpecifyThatAFuzzyLinguisticVariableCanBeCreatedAndAddedToTheModule(self):
        fuzzyModule = FuzzyModule()

        fuzzyVariable = fuzzyModule.CreateFLV("Intelligence")

        self.assertEqual(FuzzyVariable, type(fuzzyVariable), "fuzzyVariable")
        self.assertEqual(1, len(fuzzyModule._variables), "_variables")
        self.assertEqual(0, len(fuzzyModule._rules), "_rules")

    def test_SpecifyThatAFuzzyRuleCanBeCreatedAndAddedToTheModule(self):
        fuzzyModule = self.CreateFuzzyModule()

        self.assertEqual(3, len(fuzzyModule._variables), "_variables")
        self.assertEqual(9, len(fuzzyModule._rules), "_rules")

    def test_SpecifyThatFuzzifyingANonExistentVariableRaisesAndException(self):
        fuzzyModule = self.CreateFuzzyModule()

        self.assertRaises(Exception, fuzzyModule.Fuzzify, "non-existent-var", 100)

    def test_SpecifyThatDefuzzifyingANonExistentVariableRaisesAndException(self):
        fuzzyModule = self.CreateFuzzyModule()

        self.assertRaises(Exception, fuzzyModule.Defuzzify, "non-existent-var", DefuzzifyMethod.Centroid)

    def test_SpecifyThatVariableCanBeFuzzified(self):
        fuzzyModule = self.CreateFuzzyModule()

        fuzzyModule.Fuzzify("Intelligence", 115)
        fuzzyModule.Fuzzify("SkillLevel", 70)

        self.assertAlmostEqual(0.0000, fuzzyModule._variables["Intelligence"]._memberSets["dumb"].DOM, 3, "dumb")
        self.assertAlmostEqual(0.2500, fuzzyModule._variables["Intelligence"]._memberSets["average"].DOM, 3, "average")
        self.assertAlmostEqual(0.7500, fuzzyModule._variables["Intelligence"]._memberSets["smart"].DOM, 3, "smart")

        self.assertAlmostEqual(0.0000, fuzzyModule._variables["SkillLevel"]._memberSets["lowSkill"].DOM, 3, "lowSkill")
        self.assertAlmostEqual(0.1999, fuzzyModule._variables["SkillLevel"]._memberSets["mediumSkill"].DOM, 3, "mediumSkill")
        self.assertAlmostEqual(0.8000, fuzzyModule._variables["SkillLevel"]._memberSets["highSkill"].DOM, 3, "highSkill")

    def test_SpecifyThatAVariableCanBeDefuzzifiedUsingCentroidMethod(self):
        fuzzyModule = self.CreateFuzzyModule()
        fuzzyModule.Fuzzify("Intelligence", 115)
        fuzzyModule.Fuzzify("SkillLevel", 70)

        result = fuzzyModule.Defuzzify("Productivity", DefuzzifyMethod.Centroid)

        self.assertAlmostEqual(59.9245, result, 3)

    def test_SpecifyThatAVariableCanBeDefuzzifiedUsingMaxAvMethod(self):
        fuzzyModule = self.CreateFuzzyModule()
        fuzzyModule.Fuzzify("Intelligence", 115)
        fuzzyModule.Fuzzify("SkillLevel", 70)

        result = fuzzyModule.Defuzzify("Productivity", DefuzzifyMethod.MaxAv)

        self.assertAlmostEqual(67.1875, result, 3)

    def test_SpecifyThatAnExceptionIsRaisedWhenDefuzzifyingUsingAnInvalidMethod(self):
        fuzzyModule = self.CreateFuzzyModule()
        fuzzyModule.Fuzzify("Intelligence", 115)
        fuzzyModule.Fuzzify("SkillLevel", 70)

        self.assertRaises(Exception, fuzzyModule.Defuzzify, "Productivity", "invalid")

    def test_SpecifyThatAllDomsCanBeWrittenToConsole(self):
        fuzzyModule = self.CreateFuzzyModule()
        fuzzyModule.Fuzzify("Intelligence", 115)
        fuzzyModule.Fuzzify("SkillLevel", 70)

        outputString = fuzzyModule.WriteAllDOMs()

        self.assertTrue(outputString, "Ignore this string, not really important, just want 100% coverage")

    @staticmethod
    def CreateFuzzyModule():
        fuzzyModule = FuzzyModule()

        intelligence = fuzzyModule.CreateFLV("Intelligence")
        dumb = intelligence.AddLeftShoulderSet("dumb", 0, 80, 100)
        average = intelligence.AddTriangularSet("average", 80, 100, 120)
        smart = intelligence.AddRightShoulderSet("smart", 100, 120, 200)

        skillLevel = fuzzyModule.CreateFLV("SkillLevel")
        lowSkill = skillLevel.AddLeftShoulderSet("lowSkill", 0, 25, 50)
        mediumSkill = skillLevel.AddTriangularSet("mediumSkill", 25, 50, 75)
        highSkill = skillLevel.AddRightShoulderSet("highSkill", 50, 75, 100)

        productivity = fuzzyModule.CreateFLV("Productivity")
        lowProducing = productivity.AddLeftShoulderSet("lowProducing", 0, 25, 50)
        mediumProducing = productivity.AddTriangularSet("mediumProducing", 25, 50, 75)
        highProducing = productivity.AddRightShoulderSet("highProducing", 50, 75, 100)

        fuzzyModule.AddRule(FzAND(dumb, lowSkill), lowProducing)
        fuzzyModule.AddRule(FzAND(dumb, mediumSkill), lowProducing)
        fuzzyModule.AddRule(FzAND(dumb, highSkill), lowProducing)

        fuzzyModule.AddRule(FzAND(average, lowSkill), lowProducing)
        fuzzyModule.AddRule(FzAND(average, mediumSkill), lowProducing)
        fuzzyModule.AddRule(FzAND(average, highSkill), mediumProducing)

        fuzzyModule.AddRule(FzAND(smart, lowSkill), mediumProducing)
        fuzzyModule.AddRule(FzAND(smart, mediumSkill), highProducing)
        fuzzyModule.AddRule(FzAND(smart, highSkill), highProducing)

        return fuzzyModule
