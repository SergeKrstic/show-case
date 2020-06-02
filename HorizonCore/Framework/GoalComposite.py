from HorizonCore.Framework.Goal import Goal, GoalStatus


class GoalComposite(Goal):
    def __init__(self, owner, goalType):
        super().__init__(owner, goalType)

        # Composite goals may have any number of sub-goals
        self._subGoalList = []

    # Methods
    # ==================================================================================================================

    def Activate(self):
        """
        Logic to run when the goal is activated.
        """
        raise NotImplementedError

    def Process(self):
        """
        Logic to run each update-step.
        """
        raise NotImplementedError

    def Terminate(self):
        """
        Logic to run prior to the goal's destruction
        """
        raise NotImplementedError

    def HandleTelegram(self, telegram):
        """
        If a child class of Goal_Composite does not define a message handler
        the default behavior is to forward the message to the front-most sub-goal
        :param telegram: the telegram to process
        """
        return self._forwardMessageToFrontMostSubGoal(telegram)

    def AddSubGoal(self, goal):
        """
        Adds a sub-goal to the front of the sub-goal list
        :param goal: the goal to add
        """
        self._subGoalList.insert(0, goal)

    def RemoveAllSubGoals(self):
        """
        This method iterates through the sub-goals and calls each one's Terminate
        method before deleting the sub-goal and removing it from the sub-goal list
        """
        for subGoal in self._subGoalList:
            subGoal.Terminate()

        self._subGoalList = []

    def HasSubGoals(self):
        return len(self._subGoalList) > 0

    @property
    def CurrentSubGoal(self):
        if self.HasSubGoals():
            return self._subGoalList[0]
        else:
            raise Exception("No sub-goals are available")

    # Helper methods
    # ==================================================================================================================

    def _processSubGoals(self):
        """
        Processes any sub-goals that may be present
        """
        # Remove all completed and failed goals from the front of the sub-goal list
        while self.HasSubGoals() and (self.CurrentSubGoal.IsComplete() or self.CurrentSubGoal.HasFailed()):
            self.CurrentSubGoal.Terminate()
            del self._subGoalList[0]

        # If any sub-goals remain, process the one at the front of the list
        if self.HasSubGoals():
            # grab the status of the front-most sub-goal
            statusOfSubGoals = self.CurrentSubGoal.Process()

            # We have to test for the special case where the front-most sub-goal
            # reports 'completed' *and* the sub-goal list contains additional goals. When
            # this is the case, to ensure the parent keeps processing its sub-goal list
            # we must return the 'active' status.
            if statusOfSubGoals == GoalStatus.Completed and len(self._subGoalList) > 1:
                return GoalStatus.Active

            return statusOfSubGoals

        # no more sub-goals to process - return 'completed'
        else:
            return GoalStatus.Completed

    def _forwardMessageToFrontMostSubGoal(self, telegram):
        """
        Passes the message to the front-most sub-goal
        :param telegram: the telegram to process
        """
        if self.HasSubGoals():
            return self.CurrentSubGoal.HandleTelegram(telegram)

        # return false if the message has not been handled
        return False
