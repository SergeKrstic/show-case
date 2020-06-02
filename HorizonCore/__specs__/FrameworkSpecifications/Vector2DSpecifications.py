import unittest

from HorizonCore.Framework.Vector2D import Vector2D, MinDouble, Sign


class Vector2DSpecifications(unittest.TestCase):

    def test_SpecifyThatVector2DCanBeConstructed(self):
        v = Vector2D(5, 10)

        # assert
        self.assertEqual((5, 10), (v.X, v.Y))

    def test_SpecifyThatPropertyMethodsWorkCorrectly(self):
        v = Vector2D(5, 10)

        self.assertEqual((5, 10), (v.X, v.Y))

        v.X = 20
        v.Y = 30

        self.assertEqual((20, 30), (v.X, v.Y))

    def test_SpecifyThatVectorCanBeZeroed(self):
        v = Vector2D(5, 10)

        self.assertEqual((5, 10), (v.X, v.Y))

        v.Zero()

        self.assertEqual((0, 0), (v.X, v.Y))

    def test_SpecifyThatAVectorCanDetermineIfItIsZero(self):
        self.assertTrue(Vector2D(0, 0).IsZero(), "(0, 0)")
        self.assertFalse(Vector2D(3, 3).IsZero(), "(3, 3)")
        self.assertTrue(Vector2D(MinDouble, MinDouble).IsZero(), "(MinDouble, MinDouble)")

    def test_SpecifyThatAVectorCanReturnItsLength(self):
        self.assertAlmostEqual(3.1622, Vector2D(1, 3).Length(), places=3)

    def test_SpecifyThatAVectorCanReturnItsLengthSquared(self):
        self.assertAlmostEqual(10, Vector2D(1, 3).LengthSq(), places=3)

    def test_SpecifyThatAVectorCanBeNormalized(self):
        v = Vector2D(1, 3)
        v.Normalize()

        self.assertAlmostEqual(0.3162, v.X, places=3)
        self.assertAlmostEqual(0.9486, v.Y, places=3)

    def test_SpecifyThatAVectorCanCalculateItsDotProductAgainstAnotherVector(self):
        v1 = Vector2D(1, 3)
        v2 = Vector2D(4, 2)

        self.assertAlmostEqual(10, v1.Dot(v2))

    def test_SpecifyThatRotationSignCanBeDeterminedAgainstAnotherVector(self):
        v1 = Vector2D(1, 3)
        v2 = Vector2D(4, 2)

        self.assertEqual(Sign.Anticlockwise, v1.Sign(v2))
        self.assertEqual(Sign.Clockwise, v2.Sign(v1))

    def test_SpecifyThatThePerpendicularVectorCanBeCalculated(self):
        v = Vector2D(1, 3).Prep()

        self.assertEqual((-3, 1), (v.X, v.Y))

    def test_SpecifyThatAVectorsLengthCanBeTruncated(self):
        v = Vector2D(4, 5)
        v.Truncate(2)

        self.assertAlmostEqual(1.2493, v.X, places=3)
        self.assertAlmostEqual(1.5617, v.Y, places=3)

    def test_SpecifyThatTheDistanceBetweenTwoVectorsCanBeCalculated(self):
        v1 = Vector2D(1, 0)
        v2 = Vector2D(1, 3)

        self.assertAlmostEqual(3.0, v1.Distance(v2), places=3)

    def test_SpecifyThatTheDistanceSquaredBetweenTwoVectorsCanBeCalculated(self):
        v1 = Vector2D(1, 0)
        v2 = Vector2D(1, 3)

        self.assertAlmostEqual(9.0, v1.DistanceSq(v2), places=3)

    def test_SpecifyThatAVectorCanReflected(self):
        v = Vector2D(4, 5)
        n = Vector2D(1, 0)
        v.Reflect(n)

        self.assertAlmostEqual(-4, v.X, places=3)
        self.assertAlmostEqual(5, v.Y, places=3)

    def test_SpecifyThatAVectorCanBeReversed(self):
        v = Vector2D(4, 5)
        w = v.GetReverse()
        self.assertEqual((-4, -5), (w.X, w.Y))

    def test_SpecifyThatAVectorCanBeComparedForEquality(self):
        v1 = Vector2D(1, 3)
        v2 = Vector2D(1, 3)
        v3 = Vector2D(2, 4)

        print(v1 == v2)

        self.assertTrue(v1 == v2)
        self.assertTrue(v1 == v1)
        self.assertTrue(v1 != v3)

    def test_SpecifyThatVectorOperationCanBePerformed(self):
        v1 = Vector2D(1, 0)
        v2 = Vector2D(1, 3)

        w = v1 + v2
        self.assertEqual((2, 3), (w.X, w.Y), "add 1")

        w = v2 + v1
        self.assertEqual((2, 3), (w.X, w.Y), "add 2")

        w = v1 - v2
        self.assertEqual((0, -3), (w.X, w.Y), "sub 1")

        w = v2 - v1
        self.assertEqual((0, 3), (w.X, w.Y), "sub 2")

        w = v2 * 2
        self.assertEqual((2, 6), (w.X, w.Y), "mul 1")

        # Doesn't work
        # w = 2 * v2
        # self.assertEqual((0, 3), (w.X, w.Y), "mul 2")

        w = Vector2D(4, 2) / 2
        self.assertEqual((2, 1), (w.X, w.Y), "div 1")

        w = Vector2D(4, 2)
        w /= 2
        self.assertEqual((2, 1), (w.X, w.Y), "idiv 1")

        w = Vector2D(4, 2)
        w *= 2
        self.assertEqual((8, 4), (w.X, w.Y), "imul 1")

        v1 = Vector2D(1, 0)
        v2 = Vector2D(1, 3)
        v1 += v2
        self.assertEqual((2, 3), (v1.X, v1.Y), "iadd 1")

        v1 = Vector2D(5, 4)
        v2 = Vector2D(1, 3)
        v1 -= v2
        self.assertEqual((4, 1), (v1.X, v1.Y), "isub 1")

    def test_SpecifyThatAVectorCanBeNormalizedUsingAStaticMethod(self):
        v = Vector2D(1, 3)
        Vector2D.Vec2DNormalize(v)

        self.assertAlmostEqual(0.3162, v.X, places=3)
        self.assertAlmostEqual(0.9486, v.Y, places=3)

    def test_SpecifyThatTheDistanceBetweenTwoVectorsCanBeCalculatedUsingAStaticMethod(self):
        v1 = Vector2D(1, 0)
        v2 = Vector2D(1, 3)

        self.assertAlmostEqual(3.0, Vector2D.Vec2DDistance(v1, v2), places=3)

    def test_SpecifyThatTheDistanceSquaredBetweenTwoVectorsCanBeCalculatedUsingAStaticMethod(self):
        v1 = Vector2D(1, 0)
        v2 = Vector2D(1, 3)

        self.assertAlmostEqual(9.0, Vector2D.Vec2DDistanceSq(v1, v2), places=3)

    def test_SpecifyThatAVectorCanReturnItsLengthUsingAStaticMethod(self):
        v = Vector2D(1, 3)
        self.assertAlmostEqual(3.1622, Vector2D.Vec2DLength(v), places=3)

    def test_SpecifyThatAVectorCanReturnItsLengthSquaredUsingAStaticMethod(self):
        v = Vector2D(1, 3)
        self.assertAlmostEqual(10, Vector2D.Vec2DLengthSq(v), places=3)

    def test_SpecifyThatAVectorCanWrappedAroundWhenItExceedsTheBoundingBox(self):
        v = Vector2D(1, 3)
        Vector2D.WrapAround(v, 10, 20)
        self.assertEqual((1, 3), (v.X, v.Y))

        v = Vector2D(11, 3)
        Vector2D.WrapAround(v, 10, 20)
        self.assertEqual((0, 3), (v.X, v.Y))

        v = Vector2D(-1, 3)
        Vector2D.WrapAround(v, 10, 20)
        self.assertEqual((10, 3), (v.X, v.Y))

        v = Vector2D(1, 23)
        Vector2D.WrapAround(v, 10, 20)
        self.assertEqual((1, 0), (v.X, v.Y))

        v = Vector2D(1, -23)
        Vector2D.WrapAround(v, 10, 20)
        self.assertEqual((1, 20), (v.X, v.Y))

    def test_SpecifyThatAVectorCanBeDeterminedIfItIsWithinASpecifiedRegion(self):
        topLeft = Vector2D(1, 1)
        bottomRight = Vector2D(10, 10)

        self.assertTrue(Vector2D.InsideRegion(Vector2D(2, 3), topLeft, bottomRight))
        self.assertFalse(Vector2D.InsideRegion(Vector2D(0, 3), topLeft, bottomRight))
        self.assertFalse(Vector2D.InsideRegion(Vector2D(15, 3), topLeft, bottomRight))
        self.assertFalse(Vector2D.InsideRegion(Vector2D(2, 0), topLeft, bottomRight))
        self.assertFalse(Vector2D.InsideRegion(Vector2D(2, 20), topLeft, bottomRight))

    def test_SpecifyThatAVectorCanBeDeterminedIfItIsWithinASpecifiedRegion2(self):
        left = 1
        top = 1
        bottom = 10
        right = 10

        self.assertTrue(Vector2D.InsideRegion2(Vector2D(2, 3), left, top, right, bottom))
        self.assertFalse(Vector2D.InsideRegion2(Vector2D(0, 3), left, top, right, bottom))
        self.assertFalse(Vector2D.InsideRegion2(Vector2D(15, 3), left, top, right, bottom))
        self.assertFalse(Vector2D.InsideRegion2(Vector2D(2, 0), left, top, right, bottom))
        self.assertFalse(Vector2D.InsideRegion2(Vector2D(2, 20), left, top, right, bottom))

    def test_SpecifyThatAVectorCanBeDeterminedIfItIsNotWithinASpecifiedRegion(self):
        topLeft = Vector2D(1, 1)
        bottomRight = Vector2D(10, 10)

        self.assertFalse(Vector2D.NotInsideRegion(Vector2D(2, 3), topLeft, bottomRight))
        self.assertTrue(Vector2D.NotInsideRegion(Vector2D(0, 3), topLeft, bottomRight))
        self.assertTrue(Vector2D.NotInsideRegion(Vector2D(15, 3), topLeft, bottomRight))
        self.assertTrue(Vector2D.NotInsideRegion(Vector2D(2, 0), topLeft, bottomRight))
        self.assertTrue(Vector2D.NotInsideRegion(Vector2D(2, 20), topLeft, bottomRight))

    def test_SpecifyThatVector2DCanDetermineIfOneVectorIsFacingAnother(self):
        pos = Vector2D(0, 0)
        v1 = Vector2D(0, 1)
        v2 = Vector2D(0, 10)
        fov = 0.5

        self.assertTrue(Vector2D.IsSecondInFovOfFirst(pos, v1, v2, fov))
