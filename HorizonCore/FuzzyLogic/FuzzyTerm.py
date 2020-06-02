class FuzzyTerm:
    """
    Abstract class to provide an interface for classes able to be
    used as terms in a fuzzy if-then rule base.
    """

    def Clone(self):
        """
        All terms must implement a virtual constructor
        """
        raise NotImplementedError

    def GetDOM(self):
        """
        Retrieves the degree of membership of the term
        :return:
        """
        raise NotImplementedError

    def ClearDOM(self):
        """
        Clears the degree of membership of the term
        :return:
        """
        raise NotImplementedError

    def ORwithDOM(self, val):
        """
        Method for updating the DOM of a consequent when a rule fires
        :param val:
        :return:
        """
        raise NotImplementedError