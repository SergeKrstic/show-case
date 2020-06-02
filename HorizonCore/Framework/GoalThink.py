from HorizonCore.Framework.Goal import GoalStatus
from HorizonCore.Framework.GoalComposite import GoalComposite


class GoalThink(GoalComposite):
    def __init__(self, owner, goalType, evaluators=None):
        super().__init__(owner, goalType)
        self._evaluators = []
        if evaluators is not None:
            self._evaluators = evaluators
        self._owner = owner

    def Arbitrate(self):
        """
        This method iterates through each goal evaluator and selects the one
        that has the highest score as the current goal
        :return:
        """
        best = 0
        mostDesirableEvaluator = None

        # Iterate through all the evaluators to see which produces the highest score
        for evaluator in self._evaluators:
            desirability = evaluator.CalculateDesirability(self._owner)

            if desirability >= best:
                best = desirability
                mostDesirableEvaluator = evaluator

        if mostDesirableEvaluator is None:
            raise Exception("No evaluator selected")

        mostDesirableEvaluator.SetGoal(self._owner)

    def IsGoalPresent(self, goalType):
        """
        returns true if the given goal is at the front of the sub-goal list
        :param goalType:
        :return: return true or false
        """
        if self.HasSubGoals():
            return self._subGoalList[0].Type == goalType

        return False

    def Activate(self):
        self.Arbitrate()

    def Process(self):
        """
        Processes the sub-goals
        """
        self._activateIfInactive()

        subGoalStatus = self._processSubGoals()

        if subGoalStatus == GoalStatus.Completed or subGoalStatus == GoalStatus.Failed:
            self._status = GoalStatus.Inactive

        return self._status

    def Terminate(self):
        pass
