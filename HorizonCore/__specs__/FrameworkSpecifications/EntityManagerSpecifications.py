import unittest
from enum import Enum

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.EntityManager import EntityManager


class EntityManagerSpecifications(unittest.TestCase):

    def setUp(self):
        EntityManager.Reset()

    def tearDown(self):
        EntityManager.Reset()
        BaseEntity.ResetNextValidId()

    def test_SpecifyThatEntityManagerCanBeConstructed(self):
        # assert
        self.assertEqual(len(EntityManager._getEntityMap()), 0)

    def test_SpecifyThatAnEntityCanAdded(self):
        # act
        entity = DummyEntityOne(1)
        EntityManager.RegisterEntity(entity)

        # assert
        self.assertEqual(len(EntityManager._getEntityMap()), 1)

    def test_SpecifyThatTwoEntitiesCanAdded(self):
        # act
        entity1 = DummyEntityOne(1)
        entity2 = DummyEntityTwo(2)
        EntityManager.RegisterEntity(entity1)
        EntityManager.RegisterEntity(entity2)

        # assert
        self.assertEqual(len(EntityManager._getEntityMap()), 2)

    def test_SpecifyThatAnEntityCanBeRetrievedFromItsId(self):
        # arrange
        entity1 = DummyEntityOne(1)
        entity2 = DummyEntityTwo(2)

        # act
        EntityManager.RegisterEntity(entity1)
        EntityManager.RegisterEntity(entity2)

        # assert
        self.assertEqual(len(EntityManager._getEntityMap()), 2)
        self.assertEqual(EntityManager.GetEntityFromID(1).__class__.__name__, 'DummyEntityOne')
        self.assertEqual(EntityManager.GetEntityFromID(2).__class__.__name__, 'DummyEntityTwo')

    def test_SpecifyThatAnEntityCanBeRetrievedFromItsIdAsAnEnum(self):
        entity = DummyEntityOne(TestEntity.DummyEntityOne)

        # act
        EntityManager.RegisterEntity(entity)

        # assert
        self.assertEqual(len(EntityManager._getEntityMap()), 1)
        self.assertEqual(EntityManager.GetEntityFromID(TestEntity.DummyEntityOne).__class__.__name__, 'DummyEntityOne')

    def test_SpecifyThatAnEntityCanBeDeletedFromTheMap(self):
        # arrange
        entity1 = DummyEntityOne(1)
        entity2 = DummyEntityTwo(2)

        # act
        EntityManager.RegisterEntity(entity1)
        EntityManager.RegisterEntity(entity2)

        # assert
        self.assertEqual(len(EntityManager._getEntityMap()), 2)
        self.assertEqual(EntityManager.GetEntityFromID(1).__class__.__name__, 'DummyEntityOne')
        self.assertEqual(EntityManager.GetEntityFromID(2).__class__.__name__, 'DummyEntityTwo')

        # act
        EntityManager.RemoveEntity(entity1)

        # assert
        self.assertEqual(len(EntityManager._getEntityMap()), 1)
        self.assertRaises(Exception, EntityManager.GetEntityFromID, 1)
        self.assertEqual(EntityManager.GetEntityFromID(2).__class__.__name__, 'DummyEntityTwo')


class TestEntity(Enum):
    DefaultType = -1
    DummyEntityOne = 0
    DummyEntityTwo = 1


class DummyEntityOne(BaseEntity):
    def HandleTelegram(self, telegram):
        pass

    def Update(self):
        pass


class DummyEntityTwo(BaseEntity):
    def HandleTelegram(self, telegram):
        pass

    def Update(self):
        pass
