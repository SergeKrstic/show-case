from HorizonCore.Triggering.Trigger import Trigger


class TriggerRespawning(Trigger):
    """
    base class to create a trigger that is capable of respawning
    after a period of inactivity
    """

    def __init__(self, entityId):
        super().__init__(entityId)

        # When a bot comes within this trigger's area of influence it is triggered
        # but then becomes inactive for a specified amount of time. These values
        # control the amount of time required to pass before the trigger becomes
        # active once more.
        self._numberOfUpdatesBetweenRespawns = 0
        self._numberOfUpdatesRemainingUntilRespawn = 0

        # Note:
        # Time is determined by the number of updates multiplied by the
        # number of seconds between updates. Consider if its better to
        # datetime instead

    def Deactivate(self):
        """
        Sets the trigger to be inactive for numberUpdatesBetweenRespawns update-steps
        """
        self.SetInactive()
        self._numberOfUpdatesRemainingUntilRespawn = self._numberOfUpdatesBetweenRespawns

    def Try(self, entity):
        """
        To be implemented by child classes
        :param entity:
        """
        raise NotImplementedError

    def Update(self):
        """
        This is called each game-tick to update the trigger's internal state
        """
        self._numberOfUpdatesRemainingUntilRespawn -= 1
        if self._numberOfUpdatesRemainingUntilRespawn <= 0 and not self.IsActive():
            self.SetActive()

    def HandleTelegram(self, telegram):
        raise NotImplementedError

    def SetRespawnDelay(self, numberOfTicks):
        self._numberOfUpdatesBetweenRespawns = numberOfTicks
