import unittest

from HorizonCore.FuzzyLogic.FuzzyHedges import FzSet
from HorizonCore.FuzzyLogic.FuzzyVariable import FuzzyVariable


class FuzzyVariableSpecifications(unittest.TestCase):
    def test_SpecifyThatFuzzyVariableCanBeConstructed(self):
        fuzzyVariable = FuzzyVariable()

        self.assertEqual(0, len(fuzzyVariable._memberSets), "_memberSets")
        self.assertEqual(0, fuzzyVariable._minRange, "_minRange")
        self.assertEqual(0, fuzzyVariable._maxRange, "_maxRange")

    def test_SpecifyThatLeftShoulderSetCanBeAdded(self):
        fuzzyVariable = FuzzyVariable()

        fuzzySet = fuzzyVariable.AddLeftShoulderSet("leftShoulder", 0, 50, 100)

        self.assertEqual(1, len(fuzzyVariable._memberSets), "_memberSets")
        self.assertIn("leftShoulder", fuzzyVariable._memberSets, "_memberSets")
        self.assertEqual(0, fuzzyVariable._minRange, "_minRange")
        self.assertEqual(100, fuzzyVariable._maxRange, "_maxRange")
        self.assertEqual(type(fuzzySet), FzSet)

    def test_SpecifyThatRightShoulderSetCanBeAdded(self):
        fuzzyVariable = FuzzyVariable()

        fuzzySet = fuzzyVariable.AddRightShoulderSet("rightShoulder", 0, 50, 100)

        self.assertEqual(1, len(fuzzyVariable._memberSets), "_memberSets")
        self.assertIn("rightShoulder", fuzzyVariable._memberSets, "_memberSets")
        self.assertEqual(0, fuzzyVariable._minRange, "_minRange")
        self.assertEqual(100, fuzzyVariable._maxRange, "_maxRange")
        self.assertEqual(type(fuzzySet), FzSet)

    def test_SpecifyThatTriangularSetCanBeAdded(self):
        fuzzyVariable = FuzzyVariable()

        fuzzySet = fuzzyVariable.AddTriangularSet("triangle", 0, 50, 100)

        self.assertEqual(1, len(fuzzyVariable._memberSets), "_memberSets")
        self.assertIn("triangle", fuzzyVariable._memberSets, "_memberSets")
        self.assertEqual(0, fuzzyVariable._minRange, "_minRange")
        self.assertEqual(100, fuzzyVariable._maxRange, "_maxRange")
        self.assertEqual(type(fuzzySet), FzSet)

    def test_SpecifyThatSingletonSetCanBeAdded(self):
        fuzzyVariable = FuzzyVariable()

        fuzzySet = fuzzyVariable.AddSingletonSet("singleton", 0, 50, 100)

        self.assertEqual(1, len(fuzzyVariable._memberSets), "_memberSets")
        self.assertIn("singleton", fuzzyVariable._memberSets, "_memberSets")
        self.assertEqual(0, fuzzyVariable._minRange, "_minRange")
        self.assertEqual(100, fuzzyVariable._maxRange, "_maxRange")
        self.assertEqual(type(fuzzySet), FzSet)

    def test_SpecifyThatMultipleFuzzySetsCanBeAddedToCreateACompleteFuzzyVariable(self):
        fuzzyVariable = self.CreateTestFuzzyVariable()

        self.assertEqual(3, len(fuzzyVariable._memberSets), "_memberSets")
        self.assertIn("Dumb", fuzzyVariable._memberSets, "Dumb")
        self.assertIn("Average", fuzzyVariable._memberSets, "Average")
        self.assertIn("Smart", fuzzyVariable._memberSets, "Smart")
        self.assertEqual(0, fuzzyVariable._minRange, "_minRange")
        self.assertEqual(200, fuzzyVariable._maxRange, "_maxRange")

    def test_SpecifyThatTheFuzzyVariableCanCalculateTheDomInEachSet(self):
        fuzzyVariable = self.CreateTestFuzzyVariable()

        fuzzyVariable.Fuzzify(115)

        self.assertAlmostEqual(0.000, fuzzyVariable._memberSets["Dumb"].DOM, 3, "Dumb")
        self.assertAlmostEqual(0.250, fuzzyVariable._memberSets["Average"].DOM, 3, "Average")
        self.assertAlmostEqual(0.750, fuzzyVariable._memberSets["Smart"].DOM, 3, "Smart")

    def test_SpecifyThatAnExceptionIsRaisedWhenTryingFuzzifyAValueOutOfRange(self):
        fuzzyVariable = self.CreateTestFuzzyVariable()

        self.assertRaises(Exception, fuzzyVariable.Fuzzify, 250)

    def test_SpecifyThatFuzzyVariableCanWriteOutItsContentsToConsole(self):
        fuzzyVariable = self.CreateTestFuzzyVariable()
        fuzzyVariable.Fuzzify(115)
        stringOutput = str(fuzzyVariable)

        self.assertEqual(stringOutput, "\nDumb is 0.0\nAverage is 0.25\nSmart is 0.75\nMin Range: 0\nMax Range: 200")

    def test_SpecifyThatFuzzyVariableCanBeDefuzzifiedUsingMaxAvMethod(self):
        fuzzyVariable = self.CreateTestFuzzyVariable()
        fuzzyVariable.Fuzzify(115)
        self.assertAlmostEqual(145.000, fuzzyVariable.DefuzzifyMaxAv(), 3)

        fuzzyVariable = FuzzyVariable()
        fuzzyVariable.AddTriangularSet("Spike", 0, 5, 10)
        fuzzyVariable.Fuzzify(0)
        self.assertAlmostEqual(0, fuzzyVariable.DefuzzifyMaxAv(), 3)

    def test_SpecifyThatFuzzyVariableCanBeDefuzzifiedUsingCentroidMethod(self):
        fuzzyVariable = self.CreateTestFuzzyVariable()
        fuzzyVariable.Fuzzify(115)
        self.assertAlmostEqual(146.2068, fuzzyVariable.DefuzzifyCentroid(20), 3)

        fuzzyVariable = FuzzyVariable()
        fuzzyVariable.AddTriangularSet("Spike", 0, 5, 10)
        fuzzyVariable.Fuzzify(0)
        self.assertAlmostEqual(0, fuzzyVariable.DefuzzifyCentroid(20), 3)

    @staticmethod
    def CreateTestFuzzyVariable():
        fuzzyVariable = FuzzyVariable()
        fuzzyVariable._minRange = 99999999
        fuzzyVariable.AddLeftShoulderSet("Dumb", 0, 80, 100)
        fuzzyVariable.AddTriangularSet("Average", 80, 100, 120)
        fuzzyVariable.AddRightShoulderSet("Smart", 100, 120, 200)

        return fuzzyVariable
