from enum import Enum

from HorizonCore.FuzzyLogic.FuzzyRule import FuzzyRule
from HorizonCore.FuzzyLogic.FuzzyVariable import FuzzyVariable


# You must pass one of these values to the defuzzify method. This module
# only supports the MaxAv and centroid methods.
class DefuzzifyMethod(Enum):
    MaxAv = 0
    Centroid = 1


class FuzzyModule:
    """
    this class describes a fuzzy module: a collection of fuzzy variables
    and the rules that operate on them.
    """

    # When calculating the centroid of the fuzzy manifold this value is used
    # to determine how many cross-sections should be sampled
    NumberOfSamples = 15

    def __init__(self):
        # A dictionary of all the fuzzy variables this module uses
        self._variables = {}

        # A list containing all the fuzzy rules
        self._rules = []

    def CreateFLV(self, variableName):
        """
        Creates a new 'empty' fuzzy variable and returns a reference to it.
        :param variableName:
        :return:
        """
        self._variables[variableName] = FuzzyVariable()

        return self._variables[variableName]

    def AddRule(self, antecedent, consequence):
        """
        Adds a rule to the module
        :param antecedent:
        :param consequence:
        """
        self._rules.append(FuzzyRule(antecedent, consequence))

    def Fuzzify(self, nameOfFLV, value):
        """
        This method calls the Fuzzify method of the variable with the same name as the key
        :param nameOfFLV:
        :param value:
        """
        # First make sure the key exists
        if nameOfFLV not in self._variables:
            raise Exception("<FuzzyModule.Fuzzify>:key not found")

        self._variables[nameOfFLV].Fuzzify(value)

    def Defuzzify(self, nameOfFLV, method=DefuzzifyMethod.MaxAv):
        """
        given a fuzzy variable and a defuzification method this returns a crisp value
        :param nameOfFLV:
        :param method:
        :return:
        """
        # First make sure the key exists
        if nameOfFLV not in self._variables:
            raise Exception("<FuzzyModule.Fuzzify>:key not found")

        # Clear the DOMs of all the consequents of all the rules
        self._setConfidencesOfConsequentsToZero()

        # Process the rules
        for rule in self._rules:
            rule.Calculate()

        # Now defuzzify the resultant conclusion using the specified method
        if method == DefuzzifyMethod.Centroid:
            return self._variables[nameOfFLV].DefuzzifyCentroid(self.NumberOfSamples)

        elif method == DefuzzifyMethod.MaxAv:
            return self._variables[nameOfFLV].DefuzzifyMaxAv()

        else:
            raise Exception("DefuzzifyMethod not recognised")

    def WriteAllDOMs(self):
        """
        Writes the DOMs of all the variables in the module to an output stream
        :return:
        """
        outputString = "\n\n"

        for name, variable in self._variables.items():
            outputString += "\n--------------------------- " + name
            outputString += str(variable) + "\n"

        return outputString

    def _setConfidencesOfConsequentsToZero(self):
        """
        Zeros the DOMs of the consequents of each rule. Used by Defuzzify()
        """
        for rule in self._rules:
            rule.SetConfidenceOfConsequentToZero()

