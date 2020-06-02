from HorizonCore.Framework.Box2D import Box2D
from HorizonCore.Framework.Vector2D import Vector2D


class TriggerRegion:
    """
    Class to define a region of influence for a trigger. A TriggerRegion has one
    method, isTouching, which returns true if a given position is inside the region
    """

    def IsTouching(self, entityPosition, entityRadius):
        """
        Returns true if an entity of the given size and position is intersecting
        the trigger region.
        :param entityPosition:
        :param entityRadius:
        :return:
        """
        raise NotImplementedError


class TriggerRegionCircle(TriggerRegion):
    """
    Class to define a circular region of influence
    """

    def __init__(self, position, radius):
        self._position = position
        self._radius = radius

    def IsTouching(self, entityPosition, entityRadius):
        return Vector2D.Vec2DDistanceSq(self._position, entityPosition) < \
               (entityRadius + self._radius) * (entityRadius + self._radius)


class TriggerRegionRectangle(TriggerRegion):
    """
    Class to define a rectangular region of influence
    """

    def __init__(self, topLeft, bottomRight):
        self._box = Box2D(topLeft, bottomRight)

    def IsTouching(self, entityPosition, entityRadius):
        entityBox = Box2D(Vector2D(entityPosition.X - entityRadius, entityPosition.Y - entityRadius),
                          Vector2D(entityPosition.X + entityRadius, entityPosition.Y + entityRadius))

        return entityBox.IsOverlappedWith(self._box)

