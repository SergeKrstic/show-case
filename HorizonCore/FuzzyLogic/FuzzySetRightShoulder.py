from HorizonCore.FuzzyLogic.FuzzySet import FuzzySet
from HorizonCore.ToolBox.Utils import Utils


class FuzzySetRightShoulder(FuzzySet):
    """
    Definition of a fuzzy set that has a right shoulder shape. (the maximum
    value this variable can accept is *any* value greater than the midpoint.
    """
    def __init__(self, peak, leftOffset, rightOffset):
        super().__init__(((peak + rightOffset) + peak) / 2)
        self._peakPoint = peak
        self._leftOffset = leftOffset
        self._rightOffset = rightOffset

    def CalculateDOM(self, value):
        """
        This method calculates the degree of membership for a particular value
        :param value:
        :return:
        """

        # Test for the case where the left or right offsets are zero
        # (to prevent divide by zero errors below)
        if (Utils.IsEqual(self._rightOffset, 0.0) and (Utils.IsEqual(self._peakPoint, value))) or \
                (Utils.IsEqual(self._leftOffset, 0.0) and (Utils.IsEqual(self._peakPoint, value))):
            return 1.0

        # Find DOM if left of center
        elif (value <= self._peakPoint) and (value > (self._peakPoint - self._leftOffset)):
            grad = 1.0 / self._leftOffset
            return grad * (value - (self._peakPoint - self._leftOffset))

        # Find DOM if right of center and less than center + right offset
        elif (value > self._peakPoint) and (value <= self._peakPoint + self._rightOffset):
            return 1.0

        # out of range of this FLV, return zero
        else:
            return 0.0
