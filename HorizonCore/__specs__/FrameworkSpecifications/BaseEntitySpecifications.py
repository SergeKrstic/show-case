import unittest
from enum import Enum

from HorizonCore.Framework.BaseEntity import BaseEntity


class BaseEntitySpecifications(unittest.TestCase):

    EntityId = 0

    def tearDown(self):
        BaseEntity.ResetNextValidId()

    def test_SpecifyThatBaseEntityCanBeConstructed(self):
        # arrange
        baseEntity = BaseEntity(self.EntityId)

        # assert
        self.assertEqual(baseEntity.Id, self.EntityId)
        self.assertEqual(baseEntity.EntityType.value, -1)
        self.assertEqual(baseEntity.IsTagged(), False)

    def test_SpecifyThatAnExceptionIsThrownWhenConstructingABaseEntityWithAnInvalidId(self):
        # arrange
        InvalidId = -1

        # assert
        self.assertRaises(ValueError, BaseEntity, InvalidId)

    def test_SpecifyThatUpdateThrowsNotImplementedError(self):
        # arrange
        baseEntity = BaseEntity(self.EntityId)

        # assert
        self.assertRaises(NotImplementedError, baseEntity.Update)

    def test_SpecifyThatHandleMessageThrowsNotImplementedError(self):
        # arrange
        baseEntity = BaseEntity(self.EntityId)

        # assert
        self.assertRaises(NotImplementedError, baseEntity.HandleTelegram, None)

    def test_SpecifyThatActionMapThrowsNotImplementedError(self):
        # arrange
        baseEntity = BaseEntity(self.EntityId)

        # assert
        self.assertRaises(NotImplementedError, lambda: baseEntity.ActionMap)

    def test_SpecifyThatNextValidIdCanBeReset(self):
        newBaseEntity = None

        # arrange
        for i in range(0, 5):
            newBaseEntity = BaseEntity(i)

        # assert
        self.assertEqual(newBaseEntity.Id, 4)
        self.assertEqual(BaseEntity.GetNextValidId(), 5)

        # act
        BaseEntity.ResetNextValidId()

        # assert
        self.assertEqual(BaseEntity.GetNextValidId(), 0)

    def test_SpecifyThatTagCanBeSetAndCleared(self):
        # arrange
        baseEntity = BaseEntity(self.EntityId)

        # assert
        self.assertEqual(baseEntity.IsTagged(), False)

        baseEntity.Tag()
        self.assertEqual(baseEntity.IsTagged(), True)

        baseEntity.UnTag()
        self.assertEqual(baseEntity.IsTagged(), False)

    def test_SpecifyThatEntityTypeCanBeModify(self):
        # arrange
        baseEntity = BaseEntity(self.EntityId)

        # act
        baseEntity.EntityType = TestEntity.TestEntityOne

        # assert
        self.assertEqual(baseEntity.EntityType, TestEntity.TestEntityOne)


class TestEntity(Enum):
    DefaultType = -1
    TestEntityOne = 0
