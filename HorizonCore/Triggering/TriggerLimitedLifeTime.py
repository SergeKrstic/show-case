from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Triggering.Trigger import Trigger


class TriggerLimitedLifetime(Trigger):
    """
    Defines a trigger that only remains in the game for a specified
    number of update steps
    """

    def __init__(self, lifeTimeInNumberOfUpdates):
        super().__init__(BaseEntity.GetNextValidId())

        # the lifetime of this trigger in update-steps
        self._lifetime = lifeTimeInNumberOfUpdates

    def Update(self):
        """
        Children of this class should always make sure this is called from within
        their own update method
        """
        # If the lifetime counter expires set this trigger to be removed from the game
        self._lifetime -= 1
        if self._lifetime <= 0:
            self.SetToBeRemovedFromWorld()

    def Try(self, entity):
        """
        To be implemented by child classes
        :param entity:
        """
        raise NotImplementedError

    def HandleTelegram(self, telegram):
        raise NotImplementedError
