class Box2D:
    def __init__(self, topLeft, bottomRight):
        self._topLeft = topLeft
        self._bottomRight = bottomRight
        self._center = (topLeft + bottomRight) / 2

    @property
    def TopLeft(self):
        return self._topLeft

    @property
    def BottomRight(self):
        return self._bottomRight

    @property
    def Center(self):
        return self._center

    @property
    def Top(self):
        return self._topLeft.Y

    @property
    def Left(self):
        return self._topLeft.X

    @property
    def Bottom(self):
        return self._bottomRight.Y

    @property
    def Right(self):
        return self._bottomRight.X

    def IsOverlappedWith(self, other):
        """
        returns true if the box described by other intersects with this one
        :param other:
        :return:
        """
        return not ((other.Top > self.Bottom) or
                    (other.Bottom < self.Top) or
                    (other.Left > self.Right) or
                    (other.Right < self.Left))
