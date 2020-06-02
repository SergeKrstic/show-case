class GoalEvaluator:
    """
    Class template that defines an interface for objects that are able to evaluate the desirability
    of a specific strategy level goal

    The desirability or "pull" that an item or feature exerts can be similar to that of the force
    experienced by a spring (linear, 1/x) or that of a magnet (squared, 1/x^2). The "pull"
    can be either "inversely" (1/x) or "directly" (x) proportional. A constant tweak factor (k)
    can be included to tailor the desirability. Note that desirability of a feature can also
    be set a low constant value, only to come into effect when the other features do not have
    a strong enough pull
    """

    def __init__(self, characterBias):
        """
        When the desirability score for a goal has been evaluated it is multiplied
        by this value. It can be used to create bots with preferences based upon
        their personality
        :param characterBias:
        """

        self._characterBias = characterBias

    def CalculateDesirability(self, bot):
        """
        Returns a score between 0 and 1 representing the desirability of the
        strategy the concrete subclass represents
        :param bot:
        :return:
        """
        raise NotImplementedError

    def SetGoal(self, bot):
        """
        Adds the appropriate goal to the given bot's brain
        :param bot:
        """
        raise NotImplementedError
