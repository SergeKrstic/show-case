import unittest

from HorizonCore.Framework.ComparableMixin import ComparableMixin


class ComparableMixinSpecifications(unittest.TestCase):

    def test_SpecifyThatLogicalComparisonsCanBeMade(self):
        self.assertEqual(Number(2) == Number(2), True, "2 == 2")
        self.assertEqual(Number(2) == Number(3), False, "2 == 3")

        self.assertEqual(Number(3) != Number(2), True, "3 != 2")
        self.assertEqual(Number(2) != Number(2), False, "2 != 2")

        self.assertEqual(Number(2) < Number(3), True, "2 < 3")
        self.assertEqual(Number(2) < Number(1), False, "2 < 1")
        self.assertEqual(Number(2) < Number(2), False, "2 < 2")

        self.assertEqual(Number(2) <= Number(2), True, "2 <= 2")
        self.assertEqual(Number(2) <= Number(3), True, "2 <= 3")
        self.assertEqual(Number(2) <= Number(1), False, "2 <= 1")

        self.assertEqual(Number(3) > Number(2), True, "3 > 2")
        self.assertEqual(Number(1) > Number(2), False, "1 > 2")
        self.assertEqual(Number(2) > Number(2), False, "2 > 2")

        self.assertEqual(Number(2) >= Number(2), True, "2 >= 2")
        self.assertEqual(Number(3) >= Number(2), True, "3 >= 2")
        self.assertEqual(Number(1) >= Number(2), False, "1 >= 2")

    def test_SpecifyThatAnExceptionIsRaiseWhenCompareDifferentType(self):
        self.assertRaises(ValueError, Number(2).__eq__, "Not a number")

    def test_SpecifyThatAnExceptionIsRaiseWhenCompareKeyIsNotImplemented(self):
        self.assertRaises(ValueError, BrokenNumber(2).__eq__, 3)


class Number(ComparableMixin):
    def __init__(self, value):
        self.value = value

    def _compareKey(self):
        return self.value


class BrokenNumber(ComparableMixin):
    def __init__(self, value):
        self.value = value
