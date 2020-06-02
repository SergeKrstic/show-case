import math
from enum import Enum

MinDouble = 0.000000000001
Epsilon = MinDouble


def isEqual(val1, val2):
    return abs(val1 - val2) < MinDouble


class Sign(Enum):
    Clockwise = 1,
    Anticlockwise = -1


class Vector2D:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def X(self):
        return self._x

    @X.setter
    def X(self, value):
        self._x = value

    @property
    def Y(self):
        return self._y

    @Y.setter
    def Y(self, value):
        self._y = value

    def Zero(self):
        """
        Sets x and y to zero
        """
        self.X = 0.0
        self.Y = 0.0

    def IsZero(self):
        """
        :return: returns true if both x and y are zero
        """
        return (self.X * self.X) + (self.Y * self.Y) < MinDouble

    def Length(self):
        """
        :return: returns the length of the vector
        """
        return math.sqrt((self.X * self.X) + (self.Y * self.Y))

    def LengthSq(self):
        """
        :return: returns the squared length of the vector (thereby avoiding the sqrt)
        """
        return (self.X * self.X) + (self.Y * self.Y)

    def Normalize(self):
        vectorLength = self.Length()

        if vectorLength > Epsilon:
            self.X /= vectorLength
            self.Y /= vectorLength

    def Dot(self, other):
        """
        Calculates the dot product
        :param other:
        :return:
        """
        return self.X * other.X + self.Y * other.Y

    def Sign(self, other):
        """
        :return: returns positive if other is clockwise of this vector,
                 negative if anticlockwise (assuming the Y axis is pointing down,
                 X axis to right like a Window app)
        """
        if (self.Y * other.X) > (self.X * other.Y):
            return Sign.Anticlockwise
        else:
            return Sign.Clockwise

    def Prep(self):
        """
        :return: returns the vector that is perpendicular to this one.
        """
        return Vector2D(-self.Y, self.X)

    def Truncate(self, maxLength):
        """
        Adjusts x and y so that the length of the vector does not exceed max
        :param maxLength:
        :return:
        """
        if self.Length() > maxLength:
            self.Normalize()
            self.X *= maxLength
            self.Y *= maxLength

    def Distance(self, other):
        """
        :param other:
        :return: returns the distance between this vector and th one passed as a parameter
        """
        ySeparation = other.Y - self.Y
        xSeparation = other.X - self.X

        return math.sqrt((ySeparation * ySeparation) + (xSeparation * xSeparation))

    def DistanceSq(self, other):
        """
        squared version of above.
        :param other:
        :return:
        """
        ySeparation = other.Y - self.Y
        xSeparation = other.X - self.X

        return (ySeparation * ySeparation) + (xSeparation * xSeparation)

    def Reflect(self, norm):
        """
        Given a normalized vector this method reflects the vector it
        is operating upon. (like the path of a ball bouncing off a wall)
        :param norm:
        """
        w = Vector2D(self.X, self.Y)
        w += norm.GetReverse() * self.Dot(norm) * 2.0
        self.X = w.X
        self.Y = w.Y

    def GetReverse(self):
        """
        :return: returns the vector that is the reverse of this vector
        """
        return Vector2D(-self.X, -self.Y)

    # Operate overloads
    # ==================================================================================================================

    def __add__(self, other):
        x = self.X + other.X
        y = self.Y + other.Y
        return Vector2D(x, y)

    def __sub__(self, other):
        x = self.X - other.X
        y = self.Y - other.Y
        return Vector2D(x, y)

    def __mul__(self, other):
        x = self.X * other
        y = self.Y * other
        return Vector2D(x, y)

    def __truediv__(self, other):
        x = self.X / other
        y = self.Y / other
        return Vector2D(x, y)

    def __eq__(self, other):
        return isEqual(self.X, other.X) and isEqual(self.Y, other.Y)

    def __ne__(self, other):
        return self.X != other.X or self.Y != other.Y

    # Static methods
    # ==================================================================================================================

    @staticmethod
    def Vec2DNormalize(v):
        vectorLength = v.Length()

        if vectorLength > Epsilon:
            v.X /= vectorLength
            v.Y /= vectorLength

        return v

    @staticmethod
    def Vec2DDistance(v1, v2):
        ySeparation = v2.Y - v1.Y
        xSeparation = v2.X - v1.X

        return math.sqrt(ySeparation * ySeparation + xSeparation * xSeparation)

    @staticmethod
    def Vec2DDistanceSq(v1, v2):
        ySeparation = v2.Y - v1.Y
        xSeparation = v2.X - v1.X

        return ySeparation * ySeparation + xSeparation * xSeparation

    @staticmethod
    def Vec2DLength(v):
        return math.sqrt(v.X * v.X + v.Y * v.Y)

    @staticmethod
    def Vec2DLengthSq(v):
        return v.X * v.X + v.Y * v.Y

    @staticmethod
    def WrapAround(pos, maxX, maxY):
        """
        Treats a window as a toroid
        :param pos:
        :param maxX:
        :param maxY:
        :return:
        """
        if pos.X > maxX:
            pos.X = 0.0

        if pos.X < 0:
            pos.X = maxX

        if pos.Y < 0:
            pos.Y = maxY

        if pos.Y > maxY:
            pos.Y = 0.0

    @staticmethod
    def NotInsideRegion(p, topLeft, bottomRight):
        """
        :param p:
        :param topLeft:
        :param bottomRight:
        :return: returns true if the point p is not inside the region defined by topLeft and bottomRight
        """
        return (p.X < topLeft.X) or (p.X > bottomRight.X) or (p.Y < topLeft.Y) or (p.Y > bottomRight.Y)

    @staticmethod
    def InsideRegion(p, topLeft, bottomRight):
        return not((p.X < topLeft.X) or (p.X > bottomRight.X) or (p.Y < topLeft.Y) or (p.Y > bottomRight.Y))

    @staticmethod
    def InsideRegion2(p, left, top, right, bottom):
        return not((p.X < left) or (p.X > right) or (p.Y < top) or (p.Y > bottom))

    @staticmethod
    def IsSecondInFovOfFirst(posFirst, facingFirst, posSecond, fov):
        """
        returns true if the target position is in the field of view of the entity
        positioned at posFirst facing in facingFirst
        :param posFirst:
        :param facingFirst:
        :param posSecond:
        :param fov:
        :return:
        """
        toTarget = Vector2D.Vec2DNormalize(posSecond - posFirst)

        return facingFirst.Dot(toTarget) >= math.cos(fov/2.0)
