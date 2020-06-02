from enum import Enum


class GoalStatus(Enum):
    Active = 1
    Inactive = 2
    Completed = 3
    Failed = 4


class Goal:
    def __init__(self, owner, goalType):
        """
        Initialise the goal with owner and goal type
        """

        """A reference to the entity that owns this goal"""
        self._owner = owner

        """An enumerated type specifying the type of goal"""
        self._type = goalType

        """An enumerated value indicating the goal's status (active, inactive, completed, failed)
           note how goals start off in the inactive state"""
        self._status = GoalStatus.Inactive

    @property
    def Owner(self):
        """
        :return: return the owner of the goal
        """
        return self._owner

    @property
    def Type(self):
        """
        :return: the type of goal
        """
        return self._type

    @property
    def Status(self):
        """
        :return: the status of the goal (active, inactive, completed, failed)
        """
        return self._status

    def IsComplete(self):
        """
        :return: has the goal been completed
        """
        return self.Status == GoalStatus.Completed

    def IsActive(self):
        """
        :return: is the goal currently active
        """
        return self.Status == GoalStatus.Active

    def IsInactive(self):
        """
        :return: is the goal currently inactive
        """
        return self.Status == GoalStatus.Inactive

    def HasFailed(self):
        """"
        :return: has the goal failed
        """
        return self.Status == GoalStatus.Failed

    # Methods
    # ==================================================================================================================

    def Activate(self):
        """
        Logic to run when the goal is activated.
        """
        raise NotImplementedError

    def Process(self):
        """
        Logic to run each update-step
        """
        raise NotImplementedError

    def Terminate(self):
        """
        Logic to run when the goal is satisfied. (typically used to switch
        off any active steering behaviors)
        """
        raise NotImplementedError

    def HandleTelegram(self, telegram):
        """
        Goals can handle messages. Many don't though, so this defines a default behavior
        :param telegram: the telegram to process
        :return: true is the telegram was process, otherwise false
        """
        return False

    def AddSubGoal(self, goal):
        """
        A Goal is atomic and cannot aggregate sub-goals yet we must implement
        this method to provide the uniform interface required for the goal hierarchy.
        :param goal: parameter is ignored
        """
        raise Exception("Cannot add goals to atomic goals")

    # Helper methods
    # ==================================================================================================================

    def _activateIfInactive(self):
        """
        If 'Status == Inactive' this method sets it to 'Active' and calls Activate()
        """
        if self.IsInactive():
            self.Activate()

    def _reactivateIfFailed(self):
        """
        If 'Status == Failed' this method sets it to 'Inactive' so that the goal
        will be reactivated (and therefore re-planned) on the next update-step.
        """
        if self.HasFailed():
            self._status = GoalStatus.Inactive
