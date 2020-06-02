from HorizonCore.FuzzyLogic.FuzzySet import FuzzySet
from HorizonCore.ToolBox.Utils import Utils


class FuzzySetTriangle(FuzzySet):
    """
    This is a simple class to define fuzzy sets that have a triangular shape and  
    can be defined by a mid point, a left displacement and a right displacement.
    """
    def __init__(self, peakPoint, leftOffset, rightOffset):
        super().__init__(peakPoint)
        self._peakPoint = peakPoint
        self._leftOffset = leftOffset
        self._rightOffset = rightOffset

    def CalculateDOM(self, value):
        """
        this method calculates the degree of membership for a particular value
        :param value:
        :return:
        """
        # test for the case where the triangle's left or right offsets are zero
        # (to prevent divide by zero errors below)
        if ((Utils.IsEqual(self._rightOffset, 0.0) and (Utils.IsEqual(self._peakPoint, value))) or
                (Utils.IsEqual(self._leftOffset, 0.0) and (Utils.IsEqual(self._peakPoint, value)))):
            return 1.0

        # Find DOM if left of center
        if (value <= self._peakPoint) and (value >= (self._peakPoint - self._leftOffset)):
            grad = 1.0 / self._leftOffset

            return grad * (value - (self._peakPoint - self._leftOffset))

        # find DOM if right of center
        elif (value > self._peakPoint) and (value < (self._peakPoint + self._rightOffset)):
            grad = 1.0 / -self._rightOffset

            return grad * (value - self._peakPoint) + 1.0

        # out of range of this FLV, return zero
        else:
            return 0.0
