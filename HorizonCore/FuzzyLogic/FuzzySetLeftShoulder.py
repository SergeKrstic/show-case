from HorizonCore.FuzzyLogic.FuzzySet import FuzzySet
from HorizonCore.ToolBox.Utils import Utils


class FuzzySetLeftShoulder(FuzzySet):
    """
    Definition of a fuzzy set that has a left shoulder shape. (the minimum  
    value this variable can accept is *any* value less than the midpoint.
    """
    def __init__(self, peak, leftOffset, rightOffset):
        super().__init__(((peak - leftOffset) + peak) / 2)
        self._peakPoint = peak
        self._leftOffset = leftOffset
        self._rightOffset = rightOffset

    def CalculateDOM(self, value):
        """
        this method calculates the degree of membership for a particular value
        :param value:
        :return:
        """

        # Test for the case where the left or right offsets are zero
        # (to prevent divide by zero errors below)
        if (Utils.IsEqual(self._rightOffset, 0.0) and (Utils.IsEqual(self._peakPoint, value))) or \
                (Utils.IsEqual(self._leftOffset, 0.0) and (Utils.IsEqual(self._peakPoint, value))):
            return 1.0

        # Find DOM if right of center
        elif (value >= self._peakPoint) and (value < (self._peakPoint + self._rightOffset)):
            grad = 1.0 / -self._rightOffset
            return grad * (value - self._peakPoint) + 1.0

        # Find DOM if left of center
        elif (value < self._peakPoint) and (value >= self._peakPoint - self._leftOffset):
            return 1.0

        # out of range of this FLV, return zero
        else:
            return 0.0
