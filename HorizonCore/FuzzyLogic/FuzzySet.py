class FuzzySet:
    """
    class to define an interface for a fuzzy set
    """
    def __init__(self, representativeValue):
        # this will hold the degree of membership of a given value in this set
        self._degreeOfMembership = 0

        # This is the maximum of the set's membership function. For instance, if
        # the set is triangular then this will be the peak point of the triangular.
        # if the set has a plateau then this value will be the mid point of the
        # plateau. This value is set in the constructor to avoid run-time
        # calculation of mid-point values.
        self._representativeValue = representativeValue

    @property
    def RepresentativeValue(self):
        return self._representativeValue

    @property
    def DOM(self):
        return self._degreeOfMembership

    @DOM.setter
    def DOM(self, value):
        if (value < 0) or (value > 1):
            raise ValueError("DOM must be between 0 and 1")

        self._degreeOfMembership = value

    def ClearDOM(self):
        self._degreeOfMembership = 0

    # Methods
    # ==================================================================================================================

    def CalculateDOM(self, value):
        """
        Return the degree of membership in this set of the given value. NOTE,
        this does not set m_dDOM to the DOM of the value passed as the parameter.
        This is because the centroid defuzzification method also uses this method
        to determine the DOMs of the values it uses as its sample points.
        :param value:
        :return:
        """
        raise NotImplementedError

    def ORwithDOM(self, value):
        """
        If this fuzzy set is part of a consequent FLV, and it is fired by a rule
        then this method sets the DOM (in this context, the DOM represents a
        confidence level) to the maximum of the parameter value or the set's
        existing DOM value
        :param value:
        :return:
        """
        if value > self._degreeOfMembership:
            self.DOM = value
