from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Triggering.TriggerRegion import TriggerRegionCircle, TriggerRegionRectangle


class Trigger(BaseEntity):
    """
    Base class for a trigger. A trigger is an object that is
    activated when an entity moves within its region of influence.
    """

    def __init__(self, entityId):
        super().__init__(entityId)

        # Every trigger owns a trigger region. If an entity comes within this
        # region the trigger is activated
        self._regionOfInfluence = None

        # If this is true the trigger will be removed from the world
        self._removeFromWorld = False

        # It's convenient to be able to deactivate certain types of triggers
        # on an event. Therefore a trigger can only be triggered when this
        # value is true (respawning triggers make good use of this facility)
        self._active = True

    def Try(self, entityType):
        """
        When this is called the trigger determines if the entity is within the
        trigger's region of influence. If it is then the trigger will be
        triggered and the appropriate action will be taken.

        :param entityType:
        """
        raise NotImplementedError

    def Update(self):
        """
        Called each update-step of the game. This methods updates any internal
        state the trigger may have
        """
        raise NotImplementedError

    def HandleTelegram(self, telegram):
        raise NotImplementedError

    def SetToBeRemovedFromWorld(self):
        self._removeFromWorld = True

    def IsToBeRemoved(self):
        return self._removeFromWorld

    def SetInactive(self):
        self._active = False

    def SetActive(self):
        self._active = True

    def IsActive(self):
        return self._active

    def IsTouchingTrigger(self, entityGpsPosition, entityRadius):
        """
        Returns true if the entity given by a position and bounding radius is
        overlapping the trigger region
        :param entityGpsPosition: GPS coordinates of entity
        :param entityRadius: radius of trigger region
        :return: true if entity is within trigger region, otherwise false
        """
        if self._regionOfInfluence is not None:
            return self._regionOfInfluence.IsTouching(entityGpsPosition, entityRadius)

        return False

    def AddCircularTriggerRegion(self, center, radius):
        """
        Child classes use one of these methods to initialize the trigger region
        :param center: GPS coordinate of center of trigger region
        :param radius: radius of trigger region
        """
        self._regionOfInfluence = TriggerRegionCircle(center, radius)

    def AddRectangularTriggerRegion(self, topLeft, bottomRight):
        """
        Child classes use one of these methods to initialize the trigger region
        :param topLeft: top-left GPS coordinate of trigger region
        :param bottomRight: bottom-right GPS coordinate of trigger region
        """
        self._regionOfInfluence = TriggerRegionRectangle(topLeft, bottomRight)

