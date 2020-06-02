from enum import Enum

from HorizonCore.Framework.Vector2D import Vector2D


class RegionModifier(Enum):
    Normal = 1
    HalfSize = 2


class Region:
    """
    Defines a rectangular region. A region has an identifying number, and four corners.
    """

    def __init__(self, left, top, right, bottom, regionId=-1):
        self._left = left
        self._top = top
        self._right = right
        self._bottom = bottom
        self._regionId = regionId
        self._width = abs(right - left)
        self._height = abs(bottom - top)
        self._center = Vector2D((left + right) * 0.5, (top + bottom) * 0.5)

    @property
    def Left(self):
        return self._left

    @property
    def Top(self):
        return self._top

    @property
    def Right(self):
        return self._right

    @property
    def Bottom(self):
        return self._bottom

    @property
    def Width(self):
        return self._width

    @property
    def Height(self):
        return self._height

    @property
    def Length(self):
        return max(self.Width, self.Height)

    @property
    def Breadth(self):
        return min(self.Width, self.Height)

    @property
    def Center(self):
        return self._center

    @property
    def ID(self):
        return self._regionId

    def IsInside(self, position, regionModifier=RegionModifier.Normal):
        """
        Returns true if the given position lays inside the region. The
        region modifier can be used to contract the region boundaries
        :param position: Position vector to test
        :param regionModifier: contracts the regions boundaries
        :return: Returns true if the given position lays inside the region
        """
        if regionModifier == RegionModifier.Normal:
            return ((position.X > self.Left) and (position.X < self.Right) and
                    (position.Y > self.Top) and (position.Y < self.Bottom))

        elif regionModifier == RegionModifier.HalfSize:
            marginX = self.Width * 0.25
            marginY = self.Height * 0.25

            return ((position.X > (self.Left + marginX)) and (position.X < (self.Right - marginX)) and
                    (position.Y > (self.Top + marginY)) and (position.Y < (self.Bottom - marginY)))

        else:
            raise ValueError("Unrecognised region modifier")

