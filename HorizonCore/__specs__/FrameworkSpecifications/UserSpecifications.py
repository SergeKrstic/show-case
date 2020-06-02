import unittest

from HorizonCore.Framework.BaseEntity import BaseEntity
from HorizonCore.Framework.User import User
from HorizonCore.Framework.UserFeatureMap import UserFeatureMap


class UserSpecifications(unittest.TestCase):

    def test_SpecifyThatUserCanBeConstructed(self):
        # arrange
        user = self.CreateUser()

        # assert
        self.assertEqual(type(user.Features), UserFeatureMap)

    def test_SpecifyThatUpdateRaisesNotImplementedError(self):
        # arrange
        user = self.CreateUser()

        # assert
        self.assertRaises(NotImplementedError, user.Update)

    def test_SpecifyThatHandleTelegramRaisesNotImplementedError(self):
        # arrange
        user = self.CreateUser()

        # assert
        self.assertRaises(NotImplementedError, user.HandleTelegram, None)

    @staticmethod
    def CreateUser():
        BaseEntity.ResetNextValidId()
        return User(entityId=1)
