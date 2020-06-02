from HorizonCore.FuzzyLogic.FuzzyHedges import FzSet
from HorizonCore.FuzzyLogic.FuzzySetLeftShoulder import FuzzySetLeftShoulder
from HorizonCore.FuzzyLogic.FuzzySetRightShoulder import FuzzySetRightShoulder
from HorizonCore.FuzzyLogic.FuzzySetSingleton import FuzzySetSingleton
from HorizonCore.FuzzyLogic.FuzzySetTriangle import FuzzySetTriangle


EPSILON = 0.000001


class FuzzyVariable:
    def __init__(self):
        # A map of the fuzzy sets that comprise this variable
        self._memberSets = {}

        # The minimum and maximum value of the range of this variable
        self._minRange = 0
        self._maxRange = 0

    # The following methods create instances of the sets named in the method
    # name and adds them to the member set map. Each time a set of any type is
    # added the _minRange and _maxRange are adjusted accordingly. All of the
    # methods return a proxy class representing the newly created instance. This
    # proxy set can be used as an operand when creating the rule base.
    def AddLeftShoulderSet(self, name, minBound, peak, maxBound):
        self._memberSets[name] = FuzzySetLeftShoulder(peak, peak - minBound, maxBound - peak)

        # adjust range if necessary
        self._adjustRangeToFit(minBound, maxBound)

        return FzSet(self._memberSets[name])

    def AddRightShoulderSet(self, name, minBound, peak, maxBound):
        self._memberSets[name] = FuzzySetRightShoulder(peak, peak - minBound, maxBound - peak)

        # adjust range if necessary
        self._adjustRangeToFit(minBound, maxBound)

        return FzSet(self._memberSets[name])

    def AddTriangularSet(self, name, minBound, peak, maxBound):
        self._memberSets[name] = FuzzySetTriangle(peak, peak - minBound, maxBound - peak)

        # adjust range if necessary
        self._adjustRangeToFit(minBound, maxBound)

        return FzSet(self._memberSets[name])

    def AddSingletonSet(self, name, minBound, peak, maxBound):
        self._memberSets[name] = FuzzySetSingleton(peak, peak - minBound, maxBound - peak)

        # adjust range if necessary
        self._adjustRangeToFit(minBound, maxBound)

        return FzSet(self._memberSets[name])

    def Fuzzify(self, value):
        """
        Fuzzify a value by calculating its DOM in each of this variable's subsets

        Takes a crisp value and calculates its degree of membership for each set
        in the variable.

        :param value:
        :return:
        """

        # Make sure the value is within the bounds of this variable
        if (value < self._minRange) or (value > self._maxRange):
            raise ValueError("<FuzzyVariable.Fuzzify>: value out of range")

        # for each set in the flv calculate the DOM for the given value
        for currentSet in self._memberSets.values():
            currentSet.DOM = currentSet.CalculateDOM(value)

    def DefuzzifyMaxAv(self):
        """
        Defuzzify the variable using the max average method
        :return:
        """
        bottom = 0.0
        top = 0.0

        for key, currentSet in self._memberSets.items():
            bottom += currentSet.DOM
            top += currentSet.RepresentativeValue * currentSet.DOM

        # Make sure bottom is not equal to zero
        if bottom < EPSILON:
            return 0.0

        return top / bottom

    # Defuzzify the variable using the centroid method
    def DefuzzifyCentroid(self, numberOfSamples):
        # Calculate the step size
        stepSize = (self._maxRange - self._minRange) / float(numberOfSamples)

        totalArea = 0.0
        sumOfMoments = 0.0

        # Step through the range of this variable in increments equal to StepSize
        # adding up the contribution (lower of CalculateDOM or the actual DOM of this
        # variable's fuzzified value) for each subset. This gives an approximation of
        # the total area of the fuzzy manifold.(This is similar to how the area under
        # a curve is calculated using calculus... the heights of lots of 'slices' are
        # summed to give the total area.)
        #
        # In addition the moment of each slice is calculated and summed. Dividing
        # the total area by the sum of the moments gives the centroid. (Just like
        # calculating the center of mass of an object)
        for sample in range(numberOfSamples):
            # For each set get the contribution to the area. This is the lower of the
            # value returned from CalculateDOM or the actual DOM of the fuzzified
            # value itself
            for currentSet in self._memberSets.values():
                contribution = min(currentSet.CalculateDOM(self._minRange + sample * stepSize), currentSet.DOM)

                totalArea += contribution

                sumOfMoments += (self._minRange + sample * stepSize) * contribution

        # Make sure total area is not equal to zero
        if abs(totalArea) < EPSILON:
            return 0.0

        return sumOfMoments / totalArea

    # Helper Methods
    # ==================================================================================================================

    def _adjustRangeToFit(self, minBound, maxBound):
        """
        This method is called with the upper and lower bound of a set each time a
        new set is added to adjust the upper and lower range values accordingly
        """
        if minBound < self._minRange:
            self._minRange = minBound

        if maxBound > self._maxRange:
            self._maxRange = maxBound

    def __repr__(self):
        description = ""

        for key, fuzzySet in self._memberSets.items():
            description += "\n{} is {}".format(key, fuzzySet.DOM)

        description += "\nMin Range: {}\nMax Range: {}".format(self._minRange, self._maxRange)

        return description
