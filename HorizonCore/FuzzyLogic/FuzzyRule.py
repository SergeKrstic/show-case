class FuzzyRule:
    """
    This class implements a fuzzy rule of the form:  
        IF fzVar1 AND fzVar2 AND ... fzVarN THEN fzVar
    """
    def __init__(self, antecedentTerm, consequenceTerm):
        # Antecedent (usually a composite of several fuzzy sets and operators)
        self._antecedentTerm = antecedentTerm

        # Consequence (usually a single fuzzy set, but can be several ANDed together)
        self._consequenceTerm = consequenceTerm

    def SetConfidenceOfConsequentToZero(self):
        self._consequenceTerm.ClearDOM()

    def Calculate(self):
        """
        This method updates the DOM (the confidence) of the consequent term with
        the DOM of the antecedent term.
        :return:
        """
        self._consequenceTerm.ORwithDOM(self._antecedentTerm.GetDOM())
