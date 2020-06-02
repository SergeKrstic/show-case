import unittest

from HorizonCore.Framework.Singleton import Singleton


class SingletonSpecifications(unittest.TestCase):
    def test_SpecifyThatASingletonCanBeConstructed(self):
        singleton = TestSingleton()
        self.assertEqual(singleton.__class__._instances[TestSingleton], TestSingleton())


class TestSingleton(metaclass=Singleton):
    pass
