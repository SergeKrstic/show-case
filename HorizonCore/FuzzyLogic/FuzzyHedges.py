import math

from HorizonCore.FuzzyLogic.FuzzyTerm import FuzzyTerm


class FzSet(FuzzyTerm):
    """
    Class to provide a proxy for a fuzzy set. The proxy inherits from
    FuzzyTerm and therefore can be used to create fuzzy rules
    """

    def __init__(self, fuzzySet):
        # A reference to the fuzzy set this proxy represents
        self._fuzzySet = fuzzySet

    def GetDOM(self):
        return self._fuzzySet.DOM

    def ClearDOM(self):
        self._fuzzySet.ClearDOM()

    def ORwithDOM(self, value):
        self._fuzzySet.ORwithDOM(value)

    def Clone(self):
        return FzSet(self._fuzzySet)


class FzVery(FuzzyTerm):
    def __init__(self, fuzzyTerm):
        self._fuzzySet = fuzzyTerm._fuzzySet

    def GetDOM(self):
        return self._fuzzySet.DOM * self._fuzzySet.DOM

    def ClearDOM(self):
        self._fuzzySet.ClearDOM()

    def ORwithDOM(self, value):
        self._fuzzySet.ORwithDOM(value * value)

    def Clone(self):
        return FzVery(self)


class FzFairly(FuzzyTerm):
    def __init__(self, fuzzyTerm):
        self._fuzzySet = fuzzyTerm._fuzzySet

    def GetDOM(self):
        return math.sqrt(self._fuzzySet.DOM)

    def ClearDOM(self):
        self._fuzzySet.ClearDOM()

    def ORwithDOM(self, value):
        self._fuzzySet.ORwithDOM(math.sqrt(value))

    def Clone(self):
        return FzFairly(self)
