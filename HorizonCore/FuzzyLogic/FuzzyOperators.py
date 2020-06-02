"""
Classes to provide the fuzzy AND and OR operators to be used in
the creation of a fuzzy rule base
"""
import sys

from HorizonCore.FuzzyLogic.FuzzyTerm import FuzzyTerm

MAX_FLOAT = sys.float_info.max
MIN_FLOAT = sys.float_info.min


class FzAND(FuzzyTerm):
    """
    A fuzzy AND operator class
    """
    def __init__(self, *operands):
        if len(operands) < 2:
            raise ValueError("Two or operand required")

        self._terms = operands

    def Clone(self):
        return FzAND(*self._terms)

    def GetDOM(self):
        # The AND operator returns the minimum DOM of the sets it is operating on
        smallest = MAX_FLOAT

        for term in self._terms:
            if term.GetDOM() < smallest:
                smallest = term.GetDOM()

        return smallest

    def ORwithDOM(self, value):
        for term in self._terms:
            term.ORwithDOM(value)

    def ClearDOM(self):
        for term in self._terms:
            term.ClearDOM()


class FzOR(FuzzyTerm):
    """
    A fuzzy OR operator class
    """
    def __init__(self, *operands):
        if len(operands) < 2:
            raise ValueError("Two or operand required")

        self._terms = operands

    def Clone(self):
        return FzOR(*self._terms)

    def GetDOM(self):
        largest = MIN_FLOAT

        for term in self._terms:
            if term.GetDOM() > largest:
                largest = term.GetDOM()

        return largest

    def ORwithDOM(self, val):
        raise Exception("FzOR.ORwithDOM should not to be used")

    def ClearDOM(self):
        raise Exception("FzOR.ClearDOM should not to be used")
