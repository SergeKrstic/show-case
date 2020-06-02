from HorizonCore.FuzzyLogic.FuzzySet import FuzzySet


class FuzzySetSingleton(FuzzySet):
    """
    This defines a fuzzy set that is a singleton (a range over which the DOM is always 1.0)
    """
    def __init__(self, midPoint, leftOffset, rightOffset):
        super().__init__(midPoint)
        self._midPoint = midPoint
        self._leftOffset = leftOffset
        self._rightOffset = rightOffset

    def CalculateDOM(self, value):
        """
        This method calculates the degree of membership for a particular value
        :param value:
        :return:
        """

        if (value >= self._midPoint - self._leftOffset) and (value <= self._midPoint + self._rightOffset):
            return 1.0

        # out of range of this FLV, return zero
        else:
            return 0.0
